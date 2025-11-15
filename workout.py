# vim: foldmethod=expr foldtext=getline(v\:foldstart) foldexpr=indent(v\:lnum)\|\|indent(v\:lnum+1)\|\|getline(v\:lnum)[0]=='@'?1\:'<1' fillchars=fold\:\ 

# dependencies
import sys, os, inspect, tempfile, math, shutil
from dataclasses import dataclass

# configuration
MP3_DIR = os.environ['HOME'] + "/library/workout/violin/04.pieces"
MAKE_MP3S = False if (len(sys.argv) > 1 and sys.argv[1] == "txt") else True
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
os.mkdir(TARGET_DIR)
os.chdir(TARGET_DIR)
os.mkdir(DRILLS_DIR)
os.mkdir(PHRASES_DIR)
os.mkdir(SECTIONS_DIR)
os.mkdir(PIECES_DIR)

# global state
all_phrases = {}
drills = {}
phrases = set()
sections = set()
pieces = set()

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
  notes: list[Note]
  start_secs: float
  stop_secs: float

@dataclass # Section
class Section:
  label: str
  function: str
  phrases: list[Phrase]

@dataclass # Piece
class Piece:
  name: str
  meter: int
  tempo: int
  tonic: str
  sections: list[Section]
  mp3: str


# functions
def add(note, interval):
  "add base-12 notes and intervals"
  return decimal_to_note(note_to_decimal(note) + note_to_decimal(interval))

def create_phrase(label, tempo, notes):
  "start a new phrase as long as it is not a duplicate"

  # check for duplicates
  hashed_notes = list(map(lambda n: n.hash(), notes))
  hash = make_hash("phrase", { "tempo":tempo, "notes":hashed_notes })
  if hash in phrases: return False
  phrases.add(hash)

  # create one folder per phrase
  mcd(PHRASES_DIR + "/" + str(len(phrases)).zfill(NUM_PADDING) + "." + label)
  return True

def create_section(label, tempo, notes):
  "start a new section as long as it is not a duplicate"

  # check for duplicates
  hashed_notes = list(map(lambda n: n.hash(), notes))
  hash = make_hash("section", { "tempo":tempo, "notes":hashed_notes })
  if hash in sections: return False
  sections.add(hash)

  # create one folder per phrase
  mcd(SECTIONS_DIR + "/" + str(len(sections)).zfill(NUM_PADDING) + "." + label)
  return True

def create_piece_bracket(mp3, label):
  "create a practise bracket for the whole piece"

  # one directory per bracket
  pieces.add(label)
  piecenum = str(len(pieces)).zfill(NUM_PADDING)
  dir = PIECES_DIR + "/" + piecenum + "." + label
  os.mkdir(dir)

  # copy mp3 instead of remixing it
  shutil.copy(mp3, dir + "/" + piecenum + "B.mp3")

def cut_chunk(mp3, start_secs, stop_secs, outfile, speed=1.0):
  if MAKE_MP3S and stop_secs > 0:
    padding = CHUNK_FADE_SECS
    delay = CHUNK_DELAY_SECS
    ss = start_secs - padding
    to = stop_secs + padding
    st = stop_secs - start_secs + padding
    os.system(f"""
    ffmpeg -nostdin -loglevel error -ss {ss} -to {to} -i {mp3} -ac 1 -ar 48000 -q 4 \
           -af afade=d={padding},afade=t=out:st={st}:d={padding},atempo={speed},adelay={delay}s:all=true \
           "{outfile}"
           """)

def cut_mixed_chunk(mp3, start_secs, stop_secs, outfile):
  if MAKE_MP3S and stop_secs > 0:
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

def cut_repeating_chunk(mp3, start_secs, stop_secs, outfile, speed=1.0, reps=BRACKET_REPS):
  if MAKE_MP3S and stop_secs > 0:
    with tempfile.TemporaryDirectory() as tmpdir:

      # generate chunks for repetition
      cut_chunk(mp3, start_secs, stop_secs, tmpdir + "/chunk.mp3", speed);
      make_gunshot(tmpdir + "/gunshot.mp3")

      # repeat for the duration of the drill
      with open(tmpdir + "/list", "w") as f:
        for i in range(reps):
          f.write(f"file {tmpdir}/chunk.mp3\n")
        f.write(f"file {tmpdir}/gunshot.mp3\n")

      # concatenate the chunks
      os.system(f"""ffmpeg -nostdin -loglevel error -f concat -safe 0 -i "{tmpdir}/list" \
                           -codec copy "{outfile}" """)

def cut_timed_chunk(mp3, start_secs, stop_secs, outfile, speed=1.0):
  "repeat a chunk for DRILL_LENGTH_MINS"
  length = CHUNK_DELAY_SECS + (CHUNK_FADE_SECS + stop_secs - start_secs + CHUNK_FADE_SECS) / speed
  reps = math.ceil(DRILL_LENGTH_MINS * 60 / length)
  cut_repeating_chunk(mp3, start_secs, stop_secs, outfile, speed, reps)

def decimal_to_note(note):
  if not note:
    return "0"
  else:
    return decimal_to_note(note // 12).lstrip("0") + "0123456789XY"[note % 12]

def find_mp3(filename):
  return MP3_DIR + "/" + filename

def half(val):
  return int(val / 2)

def phrase(label, notes, start, stop):
  "constructor for phrases, which keeps a reference to the phrases created"
  p = Phrase(label, notes, start, stop)
  all_phrases[label] = p
  return p

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

def make_gunshot(outfile):
  make_mp3(f"""
    X:0
    M:4/4
    L:1/4
    Q:60
    K:C
    %%MIDI program {GUNSHOT_INSTRUMENT}
    |cccc|z4""", outfile)

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

    note: abc2midi miscalculates when tempo < 4, so we multiply the tempo by 4
    and set the midi speed to 25%
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
      Q:{tempo * 2}
      {"|C" * countdown_notes}
      %%MIDI program {DRONE_INSTRUMENT}
      |c
      Q:{tempo * 4}
      %%MIDI program {METRONOME_INSTRUMENT}
      {"|c" * metronome_notes}
      %%MIDI program {GUNSHOT_INSTRUMENT}
      Q:240
      {"|c" * 4}
      """, DRILLS_DIR + "/" + filename, tempo_percent=25)

def make_mp3(score, filename, transpose=0, tempo_percent=100):
  "convert an abc score to an mp3 file"
  if MAKE_MP3S:
    if not os.path.exists(filename):
      os.system(f"""echo '{score}' \
          | abc2midi /dev/stdin -o /dev/stdout \
          | timidity - --quiet --quiet --output-24bit -A800 -K{transpose} -T{tempo_percent} -Ow -o - \
          | ffmpeg -loglevel error -i - -ac 1 -ab 64k "{filename}"
          """)

def make_phrase_drill(num, name, tempo, notes, to_string, reps=1):
  if len(notes) == 0: return

  # format drill card
  text = f"{name} @{tempo} x{reps}\n"
  for note in notes: text += to_string(note) + "\n"
  with open(str(num).zfill(NUM_PADDING) + ".txt", "w") as f: f.write(text)

def make_whole(mp3, speed=1, silence=0):
  if MAKE_MP3S:
    outfile = bracketnum() + "B.mp3"
    os.system(f"""
    ffmpeg -nostdin -loglevel error -i {mp3} -ac 1 -ar 48000 -q 4 \
           -af atempo={speed},adelay={silence}s:all=true "{outfile}"
           """)

def mcd(dirname):
  os.makedirs(dirname)
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

def shift_rhythm(rhythm):
  "shift a rhythm pattern to start on the first beat"
  onsets = "1bar2dup3cet4mow"
  shift = int(onsets.index(rhythm[0]) / 4) * 4
  if shift == 0:
    return rhythm
  else:
    return "".join(map(lambda c: onsets[onsets.index(c) - shift], rhythm))

def write_drill_cards():
  sorted_drills = dict(sorted(drills.items(), key=lambda x: x[1], reverse=True))
  num = 0
  for text in sorted_drills:
    with open(DRILLS_DIR + "/" + str(num).zfill(NUM_PADDING) + ".txt", "w") as f: f.write(text)
    num += 1


