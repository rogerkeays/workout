# vim: foldmethod=expr foldtext=getline(v\:foldstart) foldexpr=indent(v\:lnum)\|\|indent(v\:lnum+1)\|\|getline(v\:lnum)[0]=='@'?1\:'<1' fillchars=fold\:\ 

# dependencies
import sys, os, inspect, tempfile, math, shutil
from dataclasses import dataclass

# configuration
MAKE_MP3S = True if ("WORKOUT_SKIP_MP3S" not in os.environ) else False
MP3_DIR = "."
NUM_PADDING = 5
DRILL_LENGTH_MINS = 2.5
BRACKET_REPS = 5
METRONOME_INSTRUMENT = 116 - 1 # woodblock
GUNSHOT_INSTRUMENT = 128 - 1   # gunshot
DRONE_INSTRUMENT = 57 - 1      # trumpet (closest to perfect pitch)
CHUNK_FADE_SECS = 2.5
CHUNK_DELAY_SECS = 5

# output preparation
TARGET_DIR = "target"
DRILLS_DIR = "02.drills"
PHRASES_DIR = "03.phrases"
SECTIONS_DIR = "04.sections"
PIECES_DIR = "05.pieces"
os.makedirs(TARGET_DIR, exist_ok=True)
os.chdir(TARGET_DIR)
os.makedirs(DRILLS_DIR, exist_ok=True)
os.makedirs(PHRASES_DIR, exist_ok=True)
os.makedirs(SECTIONS_DIR, exist_ok=True)
os.makedirs(PIECES_DIR, exist_ok=True)

# global state
drills = {}
brackets = set()
all_phrases = {}

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
  label: str
  start_secs: float
  notes: list[Note]
  stop_secs: float

@dataclass # Section
class Section:
  label: str
  function: str
  phrases: list[Phrase]

@dataclass # Piece
class Piece:
  number: int
  name: str
  meter: int
  tempo: int
  tonic: str
  sections: list[Section]


# constructors
def phrase(label, start, notes=[], stop=0):
  "constructor for phrases, which keeps a reference to the phrases created"
  p = Phrase(label, start, notes, stop)
  all_phrases[label] = p
  return p

def repeat(id, start_secs=-1.0, stop_secs=-1.0):
  """
    Create a new phrase with the same notes as the phrase with the given id.
    New mp3 start and stop times can be provided if desired. This function
    does not clone the notes.
  """
  template = all_phrases[id]
  if start_secs == -1.0: start_secs = template.start_secs
  if stop_secs == -1.0: stop_secs = template.stop_secs
  return Phrase(id, start_secs, template.notes, stop_secs)

def section(label, function, phrases):
  return Section(label, function, phrases)


# functions
def add(note, interval):
  "add base-12 notes and intervals"
  return decimal_to_note(note_to_decimal(note) + note_to_decimal(interval))

def create_piece_bracket(piece):
  "create a practise bracket for the whole piece"

  # copy mp3 instead of remixing it
  outdir = PIECES_DIR + "/00." + str(piece.number).zfill(3) + "." + piece.name
  outfile = outdir + "/" + piece.name + ".mp3"
  os.makedirs(outdir, exist_ok=True)
  if not os.path.exists(outfile): shutil.copy(find_mp3(piece), outfile)

def cut_chunk(mp3, start_secs, stop_secs, outfile):
  if MAKE_MP3S and not os.path.exists(outfile):
    to = stop_secs + CHUNK_FADE_SECS
    fade_start = stop_secs - start_secs
    os.system(f"""
    ffmpeg -nostdin -loglevel error -ss {start_secs} -to {to} -i {mp3} -ac 1 -ar 48000 -q 4 \
           -af afade=t=out:st={fade_start}:d={CHUNK_FADE_SECS} "{outfile}" """)

def cut_mixed_chunk(mp3, start_secs, stop_secs, outfile):
  if MAKE_MP3S and not os.path.exists(outfile):
    with tempfile.TemporaryDirectory() as tmpdir:

      # generate chunks for repetition
      cut_chunk(mp3, start_secs, stop_secs, tmpdir + "/050.mp3", 0.5);
      cut_chunk(mp3, start_secs, stop_secs, tmpdir + "/100.mp3", 1.0);
      make_gunshot(tmpdir + "/gunshot.mp3")

      # repeat for the duration of the drill
      chunk_length = CHUNK_FADE_SECS + stop_secs - start_secs + CHUNK_FADE_SECS
      combo_length = CHUNK_DELAY_SECS + chunk_length + CHUNK_DELAY_SECS + 2 * chunk_length
      reps = math.ceil(DRILL_LENGTH_MINS * 60 / combo_length)
      with open(tmpdir + "/list", "w") as f:
        for i in range(reps):
          f.write("file {tmpdir}/050.mp3\nfile {tmpdir}/100.mp3\n".format(tmpdir=tmpdir))
        f.write("file {tmpdir}/gunshot.mp3\n".format(tmpdir=tmpdir))

      # concatenate the chunks
      os.system(f"""
      ffmpeg -nostdin -loglevel error -f concat -safe 0 -i "{tmpdir}/list" \
             -codec copy "{outfile}" """)

def cut_repeating_chunk(mp3, start_secs, stop_secs, meter, tempo, outfile):
  if MAKE_MP3S and not os.path.exists(outfile):
    with tempfile.TemporaryDirectory() as tmpdir:

      # generate chunks for repetition
      make_intro(meter, tempo, tmpdir + "/intro.mp3")
      cut_chunk(mp3, start_secs, stop_secs, tmpdir + "/chunk.mp3")
      make_gunshot(tmpdir + "/gunshot.mp3")

      # repeat for the duration of the drill
      with open(tmpdir + "/list", "w") as f:
        for i in range(BRACKET_REPS):
          f.write(f"file {tmpdir}/intro.mp3\n")
          f.write(f"file {tmpdir}/chunk.mp3\n")
        f.write(f"file {tmpdir}/gunshot.mp3\n")

      # concatenate the chunks
      os.system(f"""ffmpeg -nostdin -loglevel error -f concat -safe 0 -i "{tmpdir}/list" \
                           -codec copy "{outfile}" """)

def cut_timed_chunk(mp3, start_secs, stop_secs, outfile, first=False, speed=1.0):
  "repeat a chunk for DRILL_LENGTH_MINS"
  length = CHUNK_DELAY_SECS + (CHUNK_FADE_SECS + stop_secs - start_secs + CHUNK_FADE_SECS) / speed
  reps = math.ceil(DRILL_LENGTH_MINS * 60 / length)
  cut_repeating_chunk(mp3, start_secs, stop_secs, outfile, first, speed, reps)

def decimal_to_note(note):
  if not note:
    return "0"
  else:
    return decimal_to_note(note // 12).lstrip("0") + "0123456789XY"[note % 12]

def find_mp3(piece):
  dir = MP3_DIR
  if "WORKOUT_MP3_DIR" in os.environ: dir = os.environ["WORKOUT_MP3_DIR"]
  return dir + "/" + str(piece.number).zfill(3) + "." + piece.name + ".mp3"

def half(val):
  return int(val / 2)

def is_unique(tempo, notes):
  """
    Check to see if a bracket has been seen before, based on the tempo and notes in the bracket.
    The notes are hashed before being compared, so the hash function determines what notes are
    considered to be duplicates (for example, lyrics might be ignored).
  """

  if notes:
    hashed_notes = list(map(lambda n: n.hash(), notes))
    hash = make_hash("phrase", { "tempo":tempo, "notes":hashed_notes })
    if hash in brackets: return False
    brackets.add(hash)

  return True

def make_drill(params={}, reps=5):
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
  if text in drills:
    drills[text] += 1
    return False
  else:
    drills[text] = 1
    return True

def make_drone(note):
  """
    make a drone of a single pitch which lasts for DRILL_LENGTH_MINS
    and finishes with an alarm
  """
  make_mp3(f"""
    X:0
    M:4/4
    L:1/4
    Q:4
    K:C transpose={note_to_decimal(note)}
    %%MIDI program {DRONE_INSTRUMENT}
    {"|C,,,," * int(DRILL_LENGTH_MINS * 4)}
    %%MIDI program {GUNSHOT_INSTRUMENT}
    Q:60
    K:C
    |cccc|z4""", DRILLS_DIR + "/=P0" + note + ".mp3")

def make_intro(meter, tempo, outfile):
  make_mp3(f"""
    X:0
    M:1/4
    L:1/4
    K:C
    Q:60
    {"|z" * CHUNK_DELAY_SECS}
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

def make_metronome(tempo):
  """
    make a metronome with the given tempo which goes for DRILL_LENGTH_MINS
    before sounding an alarm
  """
  if MAKE_MP3S:
    countdown_notes = int(tempo/8) # fifteen seconds at half tempo
    metronome_notes = int(DRILL_LENGTH_MINS * tempo)
    filename = "=T" + str(int(tempo)).zfill(NUM_PADDING - 2) + ".mp3"
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
      """, DRILLS_DIR + "/" + filename)

def make_mp3(score, filename):
  "convert an abc score to an mp3 file"
  if MAKE_MP3S and not os.path.exists(filename):
    with tempfile.TemporaryDirectory() as tmpdir:
      os.system(f"""echo '{strip_multiline(score)}' | \
          abc2midi /dev/stdin -quiet -silent -o {tmpdir}/out.midi
          fluidsynth --quiet --fast-render {tmpdir}/out.wav --gain 5 --sample-rate 48000 {tmpdir}/out.midi
          ffmpeg -loglevel error -i {tmpdir}/out.wav -ac 1 -q 4 "{filename}"
          """)

def make_phrase_drill(num, name, tempo, notes, to_string, reps=1):
  if len(notes) == 0: return

  # format drill card
  text = f"{name} @{tempo} x{reps}\n"
  for note in notes: text += to_string(note) + "\n"
  with open(str(num).zfill(NUM_PADDING) + ".txt", "w") as f: f.write(text)

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
  piece_numstr = str(piece.number).zfill(3)

  # calculate defaults
  for s, section in enumerate(piece.sections):
    for p, phrase in enumerate(section.phrases):

      # infer missing stop timestamps
      if not phrase.stop_secs:
        if p < len(section.phrases) - 1:
          phrase.stop_secs = section.phrases[p + 1].start_secs
        else:
          phrase.stop_secs = piece.sections[s + 1].phrases[0].start_secs

      # apply defaults to note fields
      if defaults_function != None:
        for n, note in enumerate(phrase.notes):
          if n < len(phrase.notes) - 1: defaults_function(note, phrase.notes[n + 1])

  # create piece practise chunks
  if len(piece.sections) > 1:
    create_piece_bracket(piece)

  # process sections in reverse
  section_num = 0
  for section in reversed(piece.sections):
    if is_unique(piece.tempo, [note for phrase in section.phrases for note in phrase.notes]):
      section_num += 1
      section_numstr = str(section_num).zfill(2)
      mcd(SECTIONS_DIR + "/00." + piece_numstr + section_numstr + "." + section.label)
      first = section.phrases[0]
      last = section.phrases[-1]
      cut_repeating_chunk(find_mp3(piece), first.start_secs, last.stop_secs, piece.meter, piece.tempo, "00000.mp3")
      os.chdir("../..")

      # process phrases in reverse
      phrase_num = 0
      for phrase in reversed(section.phrases):
        if is_unique(piece.tempo, phrase.notes):
          phrase_num += 1
          phrase_numstr = str(phrase_num).zfill(2)
          mcd(PHRASES_DIR + "/00." + piece_numstr + section_numstr + phrase_numstr + "." + phrase.label)
          cut_repeating_chunk(find_mp3(piece), phrase.start_secs, phrase.stop_secs, piece.meter, piece.tempo, "00000.mp3")
          if phrase_function != None: phrase_function(piece, section, phrase)
          os.chdir("../..")

          # process notes in reverse order
          notes = phrase.notes
          for i in reversed(range(len(notes))):
            if i < len(notes) - 2 and transition_function != None: transition_function(piece.tempo, notes[i], notes[i+1], notes[i+2])
            if i < len(notes) - 1 and note_function != None: note_function(piece.tempo, notes[i], notes[i+1])

  make_metronome(piece.tempo)

def process_scores(score_files, globals):
  """
    This is the main entry function to process one or more scores. It should be called after
    all the drill and processing functions have been declared.
  """
  for file in score_files:
    with open("../" + file) as score:
      exec(score.read(), globals)

  # output collected drills
  write_drill_cards()

def set_mp3_dir(dir):
  global MP3_DIR
  MP3_DIR = dir

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
  sorted_drills = dict(sorted(drills.items(), key=lambda x: x[1], reverse=True))
  num = 0
  for text in sorted_drills:
    with open(DRILLS_DIR + "/" + str(num).zfill(NUM_PADDING) + ".txt", "w") as f: f.write(text)
    num += 1


