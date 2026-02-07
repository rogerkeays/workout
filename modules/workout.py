# vim: foldmethod=expr foldtext=getline(v\:foldstart) foldexpr=indent(v\:lnum)\|\|indent(v\:lnum+1)\|\|getline(v\:lnum)[0]=='@'?1\:'<1' fillchars=fold\:\ 

# dependencies
import sys, os, inspect, tempfile, math, shutil
from dataclasses import dataclass

# configuration: all durations are in seconds
MAKE_MP3S = True if "WORKOUT_SKIP_MP3S" not in os.environ else False
CACHE_DIR = os.environ["HOME"] + "/.cache/workout"
VIDEO_TYPE="3gp"
VIDEO_SIZE="176:144"
VIDEO_FPS="10"
VIDEO_CODEC="h263"
AUDIO_CODEC="aac"
AUDIO_RATE="48000"
NUM_PADDING = 5
DRILL_LENGTH = 180
METRONOME_INSTRUMENT = 116 - 1 # woodblock
GUNSHOT_INSTRUMENT = 128 - 1   # gunshot
DRONE_INSTRUMENT = 57 - 1      # trumpet (closest to perfect pitch)
FADE_LENGTH = 2.5
DELAY = 5
REPS = 5

# output preparation
TARGET_DIR = "target"
DRILLS_DIR = "02.drills"
PRACTISE_DIR = "03.practise"

# global state
drills = {}
phrases = {}

# data structures
@dataclass # Note
class Note:
  beat: str
  degree: str
  attack: str
  vol_start: str
  vol_stop: str
  sustain: str
  label: str

@dataclass # Phrase
class Phrase:
  start: float
  label: str
  notes: list[Note]
  stop: float
  skip: bool

@dataclass # Section
class Section:
  id: str
  label: str
  phrases: list[Phrase]

@dataclass # Piece
class Piece:
  instrument: str
  number: int
  name: str
  video_id: str
  meter: int
  tempo: int
  tonic: str
  sections: list[Section]
  speeds: list[float]


# constructors
def phrase(start, label, notes=[], stop=0, skip=False):
  "constructor for phrases, which keeps a reference to the phrases created"
  p = Phrase(start, label, notes, stop, skip)
  phrases[label] = p
  return p

def piece(number, name, video_id, meter, tempo, tonic, sections, speeds=[0.5, 1.0]):
  "construct and process a piece in one step)"
  process_piece(Piece("workout", number, name, video_id, meter, tempo, tonic, sections, speeds), None, None, None, None)

def repeat(start, id, stop=0, skip=True):
  """
    Create a new phrase with the same notes as the phrase with the given id.
    New mp3 start and stop times can be provided if desired. This function
    does not clone the notes.
  """
  return Phrase(start, id, phrases[id].notes, stop, skip)

def section(id, label, phrases):
  return Section(id, label, phrases)


# functions
def add(note, interval):
  "add base-12 notes and intervals"
  return decimal_to_note(note_to_decimal(note) + note_to_decimal(interval))

def cut_audio_chunk(source, start, stop, outfile, speed=1.0):
  if MAKE_MP3S and not os.path.exists(outfile):
    to = stop + FADE_LENGTH
    fade_start = stop - start
    os.system(f"""
    ffmpeg -nostdin -loglevel error -ss {start} -to {to} -i {source} -ac 1 -ar {AUDIO_RATE} -q 4 \
           -af volume=replaygain=track:replaygain_noclip=0,afade=out:st={fade_start}:d={FADE_LENGTH},atempo={speed} \
           "{outfile}" """)

def cut_video_chunk(source, start, stop, outfile, speed=1.0):
  if MAKE_MP3S and not os.path.exists(outfile):
    to = stop + FADE_LENGTH
    fade_start = stop - start
    os.system(f"""
      ffmpeg -nostdin -loglevel error -ss {start} -to {to} -i {source} -ac 1 -ar {AUDIO_RATE} -q 4 \
             -af volume=replaygain=track:replaygain_noclip=0,afade=out:st={fade_start}:d={FADE_LENGTH},atempo={speed} \
             -vf scale="{VIDEO_SIZE}:force_original_aspect_ratio=decrease,pad={VIDEO_SIZE}:(ow-iw)/2:(oh-ih)/2,fade=out:st={fade_start}:d={FADE_LENGTH},setpts=PTS/{speed}" \
             -r {VIDEO_FPS} -vcodec {VIDEO_CODEC} -acodec {AUDIO_CODEC} "{outfile}" """)

def decimal_to_note(note):
  if not note:
    return "0"
  else:
    return decimal_to_note(note // 12).lstrip("0") + "0123456789XY"[note % 12]

def get_video(id):
  video_file = f"{CACHE_DIR}/{id}.mp4"
  if MAKE_MP3S and not os.path.exists(video_file):
    os.makedirs(CACHE_DIR, exist_ok=True)
    os.system(f"yt-dlp --js-runtime node -f 'best[height<=480]' -t mp4 https://www.youtube.com/watch?v={id} -o '{video_file}'")
    os.system(f"loudgain --pregain=5 --clip --tagmode=i '{video_file}'")
  return video_file

def half(val):
  return int(val / 2)

def is_skipped(section):
  for p in section.phrases:
    if p.skip == False: return False
  return True

def make_bracket(piece, start, stop, label):
  source = get_video(piece.video_id)
  with tempfile.TemporaryDirectory() as tmpdir:
    for speed in piece.speeds:

      # create audio brackets
      speed_str = str(int(speed*100)).zfill(3)
      audio_intro = f"{tmpdir}/intro.{speed_str}.mp3"
      audio_chunk = f"{tmpdir}/audio.{speed_str}.mp3"
      gunshot_chunk = f"{tmpdir}/gunshot.mp3"
      audio_concat = f"{tmpdir}/audio.{speed_str}.txt"
      audio_output = f"{label}.{speed_str}.mp3"
      make_intro(piece.meter, piece.tempo * speed, audio_intro)
      if MAKE_MP3S and not os.path.exists(audio_output):

        # generate chunks for repetition
        make_intro(piece.meter, piece.tempo * speed, audio_intro)
        cut_audio_chunk(source, start, stop, audio_chunk, speed)
        make_gunshot(gunshot_chunk)

        # repeat for the duration of the drill
        with open(audio_concat, "w") as f:
          for i in range(REPS):
            f.write(f"file {audio_intro}\n")
            f.write(f"file {audio_chunk}\n")
          f.write(f"file {gunshot_chunk}\n")

        # concatenate the chunks
        os.system(f"""ffmpeg -nostdin -loglevel error -f concat -safe 0 -i "{audio_concat}" \
                             -acodec copy "{audio_output}" """)

      # create video brackets
      video_intro = f"{tmpdir}/intro.{speed_str}.{VIDEO_TYPE}"
      video_chunk = f"{tmpdir}/video.{speed_str}.{VIDEO_TYPE}"
      video_frame = f"{tmpdir}/video.{speed_str}.png"
      video_concat = f"{tmpdir}/video.{speed_str}.txt"
      video_output = f"{label}.{speed_str}.{VIDEO_TYPE}"
      if MAKE_MP3S and not os.path.exists(video_output):

        # cut video chunk and make an intro in the same format
        cut_video_chunk(source, start, stop, video_chunk, speed)
        os.system(f"""ffmpeg -nostdin -loglevel error -i "{video_chunk}" -frames 1 "{video_frame}" """)
        os.system(f"""ffmpeg -nostdin -loglevel error -i "{video_frame}" -i "{audio_intro}" \
                             -r {VIDEO_FPS} -vcodec {VIDEO_CODEC} -acodec {AUDIO_CODEC} "{video_intro}" """)

        # concatenate the chunks: re-encodes for buggy video players
        with open(video_concat, "w") as f:
          f.write(f"file {video_intro}\n")
          f.write(f"file {video_chunk}\n")
        os.system(f"""ffmpeg -nostdin -loglevel error -f concat -safe 0 -i "{video_concat}" \
                             -r {VIDEO_FPS} -vcodec {VIDEO_CODEC} -acodec {AUDIO_CODEC} "{video_output}" """)

def make_drill(instrument, params={}, reps=5):
  "make a drill card, ensuring it is unique, and formatting it appropriately as a text file"

  # format drill card
  name = inspect.stack()[1].function
  text = name + " x" + str(reps) + "\n"
  for key in params:
    if params[key]:
      text += key[0:3].upper() + " "
      if isinstance(params[key], list):
        text += " ".join(params[key]) + "\n"
      else:
        text += str(params[key]) + "\n"

  # add or increment the collection
  if instrument not in drills:
    drills[instrument] = {}
  if text in drills[instrument]:
    drills[instrument][text] += 1
    return False
  else:
    drills[instrument][text] = 1
    return True

def make_drone(instrument, note):
  """
    make a drone of a single pitch which lasts for DRILL_LENGTH seconds
    and finishes with an alarm
  """
  make_mp3(f"""
    X:0
    M:4/4
    L:1/4
    Q:4
    K:C transpose={note_to_decimal(note)}
    %%MIDI program {DRONE_INSTRUMENT}
    {"|C,,,," * int(4 * DRILL_LENGTH / 60)}
    %%MIDI program {GUNSHOT_INSTRUMENT}
    Q:60
    K:C
    |cccc|z4""", f"../../../{instrument}/{DRILLS_DIR}/=P0{note}.mp3")

def make_flashcard(num, name, tempo, notes, to_string, reps=1):
  if len(notes) == 0: return

  # format drill card
  text = f"{name} @{tempo} x{reps}\n"
  for note in notes: text += to_string(note) + "\n"
  with open(str(num).zfill(NUM_PADDING) + ".txt", "w") as f: f.write(text)

def make_intro(meter, tempo, outfile):
  make_mp3(f"""
    X:0
    M:1/4
    L:1/4
    K:C
    Q:60
    {"|z" * DELAY}
    %%MIDI program {METRONOME_INSTRUMENT}
    Q:{tempo}
    {"c|" * meter}
    """, outfile)

def make_gunshot(outfile):
  make_mp3(f"""
    X:0
    M:4/4
    L:1/4
    Q:60
    K:C
    %%MIDI program {GUNSHOT_INSTRUMENT}
    cccc|z4|""", outfile)

def make_hash(name, params):
  """
    hash a drill with the given parameters, such that combinations
    resulting in the same physics result in the same value
  """
  keys = params.copy()
  if "lyrics" in keys: del keys["lyrics"]
  if "index" in keys: del keys["index"]
  if "rhythm" in keys: keys["rhythm"] = shift_rhythm(keys["rhythm"])
  return name + str(keys)

def make_metronome(instrument, tempo):
  """
    make a metronome for the given piece which goes for DRILL_LENGTH seconds
    before sounding an alarm
  """
  if MAKE_MP3S:
    countdown_notes = int(tempo/8) # fifteen seconds at half tempo
    metronome_notes = int(tempo * DRILL_LENGTH / 60)
    filename = "=T" + str(int(tempo)).zfill(3) + ".mp3"
    make_mp3(f"""
      X:0
      M:1/4
      L:1/4
      K:C
      %%MIDI program {METRONOME_INSTRUMENT}
      Q:{half(tempo)}
      {"|C" * countdown_notes}
      %%MIDI program {DRONE_INSTRUMENT}
      |c
      Q:{tempo}
      %%MIDI program {METRONOME_INSTRUMENT}
      {"|c" * metronome_notes}
      %%MIDI program {GUNSHOT_INSTRUMENT}
      Q:60
      {"|c" * 4}
      """, f"{TARGET_DIR}/{instrument}/{DRILLS_DIR}/{filename}")

def make_mp3(score, filename):
  "convert an abc score to an mp3 file"
  if MAKE_MP3S and not os.path.exists(filename):
    with tempfile.TemporaryDirectory() as tmpdir:
      os.system(f"""echo '{strip_multiline(score)}' | \
          abc2midi /dev/stdin -quiet -silent -o {tmpdir}/out.midi
          fluidsynth --quiet --fast-render {tmpdir}/out.wav --gain 5 --sample-rate {AUDIO_RATE} {tmpdir}/out.midi
          ffmpeg -loglevel error -i {tmpdir}/out.wav -ac 1 -ar {AUDIO_RATE} -q 4 "{filename}"
          """)

def make_silence(seconds, outfile):
  os.system(f"ffmpeg -nostdin -loglevel error -f lavfi -i anullsrc=r=48000:cl=mono -t {seconds} {outfile}")

def make_whole(mp3, speed=1, silence=0):
  if MAKE_MP3S:
    outfile = bracketnum() + "B.mp3"
    os.system(f"""
    ffmpeg -nostdin -loglevel error -i {mp3} -ac 1 -ar 48000 -q 4 \
           -af atempo={speed},adelay={silence}s:all=true "{outfile}"
           """)

def mcd(dirname):
  os.makedirs(dirname, exist_ok=True)
  os.chdir(dirname)

def normalise_tab(tab):
  "remove bar lines and spaces and replace repeat marks"
  raw = tab.replace(" ", "").replace("|", "").replace("\n", "")
  result = []
  for i, letter in enumerate(raw):
    result.append(letter if letter != "=" else result[i-1])
  return ''.join(result)

def note_to_decimal(note):
  return int(str(note).replace("X", "A").replace("Y", "B"), 12)

def parse_note(text: str):
  """
    field order: beat (space) degree (space) attack vol_start vol_stop sustain (space) label
    example:
     1 0 L44= twin-
     2 = ==== kle
     3 7 ==== twin-
     4 = ==== kle
  """
  return Note(text[0], text[2], text[4], text[5], text[6], text[7], text[9:], {})

def process_piece(piece, defaults_function, phrase_function, transition_function, note_function):
  """
  scan the score of each piece and generate drills by calling the given functions during the scan:
    defaults_function(note, next)
    phrase_function(piece, section, phrase)
    transition_function(tempo, first_note, second_note, next_note)
    note_function(tempo, note, next)

  if there is nothing to do at a given step, pass the function as None
  """
  os.makedirs(f"{TARGET_DIR}/{piece.instrument}/{DRILLS_DIR}", exist_ok=True)

  # calculate defaults
  for s, section in enumerate(piece.sections):
    for p, phrase in enumerate(section.phrases):

      # infer missing stop timestamps
      if not phrase.stop:
        if p < len(section.phrases) - 1:
          phrase.stop = section.phrases[p + 1].start
        else:
          phrase.stop = piece.sections[s + 1].phrases[0].start

      # apply defaults to note fields
      if defaults_function != None:
        for n, note in enumerate(phrase.notes):
          if n < len(phrase.notes) - 1: defaults_function(note, phrase.notes[n + 1])

  # create piece practise bracket
  start = piece.sections[0].phrases[0].start
  stop = piece.sections[-1].phrases[-1].stop
  mcd(f"{TARGET_DIR}/{piece.instrument}/{PRACTISE_DIR}/00.{str(piece.number).zfill(4)}.{piece.name}")
  make_bracket(piece, start, stop, piece.name)

  # process sections in reverse
  section_num = 0
  for section in piece.sections:
    section_num += 1
    if not is_skipped(section):
      start = section.phrases[0].start
      stop = section.phrases[-1].stop
      mcd(f"{str(section_num).zfill(2)} ----- {section.label}")
      make_bracket(piece, start, stop, section.label)

      # process phrases in reverse
      phrase_num = 0
      for phrase in section.phrases:
        phrase_num += 1
        if not phrase.skip:
          mcd(f"{str(phrase_num).zfill(2)} ----- {phrase.label}")
          make_bracket(piece, phrase.start, phrase.stop, phrase.label)
          if phrase_function != None: phrase_function(piece, section, phrase)

          # process notes in reverse order
          notes = phrase.notes
          for i in reversed(range(len(notes))):
            if i < len(notes) - 2 and transition_function != None: transition_function(piece.tempo, notes[i], notes[i+1], notes[i+2])
            if i < len(notes) - 1 and note_function != None: note_function(piece.tempo, notes[i], notes[i+1])
          os.chdir("..")
      os.chdir("..")
  os.chdir("../../../..")

  make_metronome(piece.instrument, piece.tempo)

def shift_rhythm(rhythm):
  "shift a rhythm pattern to start on the first beat"
  onsets = "1bar2dup3cet4mow"
  shift = int(onsets.index(rhythm[0]) / 4) * 4
  if shift == 0:
    return rhythm
  else:
    return "".join(map(lambda c: onsets[onsets.index(c) - shift], rhythm))

def strip_multiline(string):
  return '\n'.join(line.strip() for line in string.splitlines())

def write_drill_cards():
  for instrument, counted_drills in drills.items():
    sorted_drills = dict(sorted(counted_drills.items(), key=lambda x: x[1], reverse=True))
    num = 0
    for text in sorted_drills:
      with open(f"{TARGET_DIR}/{instrument}/{DRILLS_DIR}/{str(num).zfill(NUM_PADDING)}.txt", "w") as f: f.write(text)
      num += 1


