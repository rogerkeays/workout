
# imports
true = True
false = False
import sys, os, inspect, tempfile, math, shutil
from dataclasses import dataclass

# configuration
MP3_DIR = os.environ['HOME'] + "/library/workout/violin/04.pieces"
MAKE_MP3S = False if (len(sys.argv) > 1 and sys.argv[1] == "txt") else True
TARGET_DIR = "target"
DRILLS_DIR = "02.drills"
BRACKETS_DIR = "03.brackets"
NUM_PADDING = 5
DRILL_LENGTH_MINS = 2.5
BRACKET_REPS = 8
METRONOME_INSTRUMENT = 116 - 1 # woodblock
GUNSHOT_INSTRUMENT = 128 - 1   # gunshot
DRONE_INSTRUMENT = 57 - 1      # trumpet (closest to perfect pitch)
CHUNK_FADE_SECS = 2.5
CHUNK_DELAY_SECS = 5

# global state
os.mkdir(TARGET_DIR)
os.chdir(TARGET_DIR)
os.mkdir(DRILLS_DIR)
os.mkdir(BRACKETS_DIR)
drills = {}
brackets = set()

@dataclass
class Note:
  start_beat: str
  stop_beat: str
  degree: str
  attack: str
  dynamics: str
  label: str

@dataclass
class Phrase:
  label: str
  notes: list[Note]
  start_secs: float
  stop_secs: float

# constructor for phrases, which keeps a reference to the phrases created
all_phrases = {}
def phrase(label, notes, start, stop):
  p = Phrase(label, notes, start, stop)
  all_phrases[label] = p
  return p

@dataclass
class Section:
  label: str
  function: str
  phrases: list[Phrase]

@dataclass
class Piece:
  name: str
  meter: int
  tempo: int
  tonic: str
  sections: list[Section]
  mp3: str

def parse_note(text: str):
  """
    field order: beat degree attack dynamic " " label
    example: "10LM twin- 10LM kl"
  """
  return Note(text[0], text[1], text[2], text[3], text[5:], {})

def mcd(dirname):
  os.makedirs(dirname)
  os.chdir(dirname)

def make_drill(num, params={}, reps=5):
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
    return false
  else:
    drills[text] = 1
    return true

def make_phrase_drill(num, name, tempo, notes, reps=5):
  if len(notes) == 0: return

  # format drill card
  text = f"{name} @{tempo} x{reps}\n"
  for note in notes: text += note.to_compact_string() + "\n"

  # add or increment the collection
  if text in drills:
    drills[text] += 1
    return false
  else:
    drills[text] = 1
    return true

def write_drill_cards():
  sorted_drills = dict(sorted(drills.items(), key=lambda x: x[1], reverse=true))
  num = 0
  for text in sorted_drills:
    with open(DRILLS_DIR + "/" + str(num).zfill(NUM_PADDING) + ".txt", "w") as f: f.write(text)
    num += 1

#
# hash a drill with the given parameters, such that combinations
# resulting in the same physics result in the same value
#
def make_hash(name, params):
  keys = params.copy()
  if "lyrics" in keys: del keys["lyrics"]
  if "index" in keys: del keys["index"]
  if "rhythm" in keys: keys["rhythm"] = shift_rhythm(keys["rhythm"])
  return name + str(keys)

# shift a rhythm pattern to start on the first beat
def shift_rhythm(rhythm):
  onsets = "1bar2dup3cet4mow"
  shift = int(onsets.index(rhythm[0]) / 4) * 4
  if shift == 0:
    return rhythm
  else:
    return "".join(map(lambda c: onsets[onsets.index(c) - shift], rhythm))

# format the current drill number as a zero-padded string
def drillnum(): return str(len(drills)).zfill(NUM_PADDING)

def create_bracket(mp3, start_secs, stop_secs, label, tempo, notes):

  # check for duplicates
  hashed_notes = list(map(lambda n: n.hash(), notes))
  hash = make_hash("bracket", { "tempo":tempo, "notes":hashed_notes })
  if hash in brackets: return False
  brackets.add(hash)

  # create one folder per bracket
  dir = BRACKETS_DIR + "/" + bracketnum() + "." + label
  os.mkdir(dir)

  # create bracket card and mp3 chunk
  with open(dir + "/" + bracketnum() + "A.txt", "w") as f:
    for note in notes: f.write(note.to_compact_string() + "\n")
  cut_timed_chunk(mp3, start_secs, stop_secs, dir + "/" + bracketnum() + "B.mp3")
  return True

def create_piece_bracket(mp3, label):
  "create a practise bracket for the whole piece"

  # one directory per bracket
  brackets.add(label)
  dir = BRACKETS_DIR + "/" + bracketnum() + "." + label
  os.mkdir(dir)

  # copy mp3 instead of remixing it
  shutil.copy(mp3, dir + "/" + bracketnum() + "B.mp3")

def bracketnum(): return str(len(brackets)).zfill(NUM_PADDING)

#
# make a metronome with the given tempo which goes for DRILL_LENGTH_MINS
# before sounding an alarm
#
# note: abc2midi miscalculates when tempo < 4, so we multiply the tempo by 4
# and set the midi speed to 25%
#
def make_metronome(tempo):
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

#
# make a drone of a single pitch which lasts for DRILL_LENGTH_MINS
# and finishes with an alarm
#
def make_drone(note):
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

#
# convert an abc score to an mp3 file
#
def make_mp3(score, filename, transpose=0, tempo_percent=100):
  if MAKE_MP3S:
    if not os.path.exists(filename):
      os.system(f"""echo '{score}' \
          | abc2midi /dev/stdin -o /dev/stdout \
          | timidity - --quiet --quiet --output-24bit -A800 -K{transpose} -T{tempo_percent} -Ow -o - \
          | ffmpeg -loglevel error -i - -ac 1 -ab 64k "{filename}"
          """)

def make_whole(mp3, speed=1, silence=0):
  if MAKE_MP3S:
    outfile = bracketnum() + "B.mp3"
    os.system(f"""
    ffmpeg -nostdin -loglevel error -i {mp3} -ac 1 -ar 48000 -q 4 \
           -af atempo={speed},adelay={silence}s:all=true "{outfile}"
           """)

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

# repeat a chunk for DRILL_LENGTH_MINS
def cut_timed_chunk(mp3, start_secs, stop_secs, outfile, speed=1.0):
  length = CHUNK_DELAY_SECS + (CHUNK_FADE_SECS + stop_secs - start_secs + CHUNK_FADE_SECS) / speed
  reps = math.ceil(DRILL_LENGTH_MINS * 60 / length)
  cut_repeating_chunk(mp3, start_secs, stop_secs, outfile, speed, reps)

def make_gunshot(outfile):
  make_mp3(f"""
    X:0
    M:4/4
    L:1/4
    Q:60
    K:C
    %%MIDI program {GUNSHOT_INSTRUMENT}
    |cccc|z4""", outfile)

def find_mp3(filename):
  return MP3_DIR + "/" + filename

# remove bar lines and spaces and replace repeat marks
def normalise_tab(x):
  raw = x.replace(" ", "").replace("|", "").replace("\n", "")
  result = []
  for i, letter in enumerate(raw):
    result.append(letter if letter != "=" else result[i-1])
  return ''.join(result)

# add base-12 notes and intervals
def add(note, interval):
  return decimal_to_note(note_to_decimal(note) + note_to_decimal(interval))

def note_to_decimal(note):
  return int(str(note).replace("X", "A").replace("Y", "B"), 12)

def decimal_to_note(note):
  if not note:
    return "0"
  else:
    return decimal_to_note(note // 12).lstrip("0") + "0123456789XY"[note % 12]

def half(val): return int(val / 2)

