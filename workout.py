
import os, inspect, re, tempfile, math
from dataclasses import dataclass

# configuration
MAKE_MP3S = True
TARGET_DIR = "target/"
DRILLS_DIR = "02.drills/"
PHRASES_DIR = "03.phrases/"
SECTIONS_DIR = "04.sections/"
NUM_PADDING = 5
DRILL_LENGTH_MINS = 3
METRONOME_INSTRUMENT = 116 - 1 # woodblock
ALARM_INSTRUMENT = 128 - 1     # gunshot
DRONE_INSTRUMENT = 57 - 1      # trumpet (closest to perfect pitch)
CHUNK_FADE_SECS = 2.5
CHUNK_DELAY_SECS = 5

# global state
os.mkdir(TARGET_DIR)
os.chdir(TARGET_DIR)
os.mkdir(DRILLS_DIR)
sections = 0
phrases = 0
drills = set()

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

#
# Make a new directory of cards and change into that directory.
# The caller of this function is responsible for changing back
# to the original directory when the cards have been generated.
#
def mcd(dirname):
  os.makedirs(dirname)
  os.chdir(dirname)

def make_section(label, tempo, notes):
  if len(notes) == 0: return
  global sections
  with open(label + ".txt", "w") as f:
    for note in notes: f.write(note.to_string() + "\n")
  sections += 1

def make_phrase(label, tempo, notes):
  if len(notes) == 0: return
  global phrases
  with open(label + ".txt", "w") as f:
    for note in notes: f.write(note.to_string() + "\n")
  phrases += 1

def make_phrase_drill(num, name, tempo, notes, reps=5):
  if len(notes) == 0: return

  # check for duplicates
  hash = make_hash(name, {"tempo":tempo, "notes":notes })
  if hash in drills: return False
  drills.add(hash)

  outdir = "../../../" + DRILLS_DIR + str(num).zfill(2) + "." + name
  os.makedirs(outdir, exist_ok=True)
  with open(outdir + "/" + drillnum() + "A.txt", "w") as f:
    f.write(f"{name} @{tempo} x{reps}\n")
    for note in notes: f.write(note.to_string() + "\n")

#
# make a drill card, ensuring it is unique, and formatting
# it appropriately as a text file
#
def make_drill(num, params={}, reps=5):

  # check for duplicates
  name = inspect.stack()[1].function
  hash = make_hash(name, params)
  if hash in drills: return False
  drills.add(hash)

  # write card text
  outdir = "../../../" + DRILLS_DIR + str(num).zfill(2) + "." + name
  os.makedirs(outdir, exist_ok=True)
  with open(outdir + "/" + drillnum() + "A.txt", "w") as f:
    f.write(name + " x" + str(reps) + "\n")
    for key in params:
      if params[key]:
        f.write(key[0:3].upper() + " ")
        if isinstance(params[key], list):
          f.write(" ".join(params[key]) + "\n")
        else:
          f.write(str(params[key]) + "\n")

  return True

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
def phrasenum(): return str(phrases).zfill(NUM_PADDING)
def sectionnum(): return str(sections).zfill(NUM_PADDING)

#
# make a metronome with the given tempo which goes for DRILL_LENGTH_MINS
# before sounding an alarm
#
# note: abc2midi miscalculates when tempo < 4, so we multiply the tempo by 4
# and set the midi speed to 25%
#
def make_metronome(tempo):
  if MAKE_MP3S:
    num_notes = int(DRILL_LENGTH_MINS * tempo)
    filename = "=T" + str(int(tempo)).zfill(NUM_PADDING - 1) + ".mp3"
    make_mp3(f"""
      X:0
      M:1/4
      L:1/4
      Q:{tempo*4}
      K:C
      %%MIDI program {METRONOME_INSTRUMENT}
      {"|c" * num_notes}
      %%MIDI program {ALARM_INSTRUMENT}
      Q:240
      |C|C|C|C|z|z|z|z""", DRILLS_DIR + filename, tempo_percent=25)

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
    {"|C,,,,C,,,,C,,,,C,,,," * DRILL_LENGTH_MINS}
    %%MIDI program {ALARM_INSTRUMENT}
    Q:60
    |CCCC|z4""", "../../../" + DRILLS_DIR + drillnum() + "B.mp3")

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
    outfile = PHRASES_DIR + phrasenum() + ".mp3"
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

def cut_mixed_chunk(mp3, start_secs, stop_secs, outfile):
  if MAKE_MP3S and stop_secs > 0:
    with tempfile.TemporaryDirectory() as tmpdir:

      # generate chunks for repetition
      cut_chunk(mp3, start_secs, stop_secs, tmpdir + "/050.mp3", 0.5);
      cut_chunk(mp3, start_secs, stop_secs, tmpdir + "/100.mp3", 1.0);
      cut_alarm(tmpdir + "/alarm.mp3")

      # repeat for the duration of the drill
      chunk_length = CHUNK_FADE_SECS + stop_secs - start_secs + CHUNK_FADE_SECS
      combo_length = CHUNK_DELAY_SECS + chunk_length + CHUNK_DELAY_SECS + 2 * chunk_length
      reps = math.ceil(DRILL_LENGTH_MINS * 60 / combo_length)
      with open(tmpdir + "/list", "w") as f:
        for i in range(reps):
          f.write("file {tmpdir}/050.mp3\nfile {tmpdir}/100.mp3\n".format(tmpdir=tmpdir))
        f.write("file {tmpdir}/alarm.mp3\n".format(tmpdir=tmpdir))

      # concatenate the chunks
      os.system(f"""
      ffmpeg -nostdin -loglevel error -f concat -safe 0 -i "{tmpdir}/list" \
             -codec copy "{outfile}" """)

def cut_timed_chunk(mp3, start_secs, stop_secs, outfile, speed=1.0):
  if MAKE_MP3S and stop_secs > 0:
    with tempfile.TemporaryDirectory() as tmpdir:

      # generate chunks for repetition
      cut_chunk(mp3, start_secs, stop_secs, tmpdir + "/chunk.mp3", speed);
      cut_alarm(tmpdir + "/alarm.mp3")

      # repeat for the duration of the drill
      length = CHUNK_DELAY_SECS + (CHUNK_FADE_SECS + stop_secs - start_secs + CHUNK_FADE_SECS) / speed
      reps = math.ceil(DRILL_LENGTH_MINS * 60 / length)
      with open(tmpdir + "/list", "w") as f:
        for i in range(reps):
          f.write(f"file {tmpdir}/chunk.mp3\n")
        f.write(f"file {tmpdir}/alarm.mp3\n")

      # concatenate the chunks
      os.system(f"""ffmpeg -nostdin -loglevel error -f concat -safe 0 -i "{tmpdir}/list" \
                           -codec copy "{outfile}" """)

def cut_alarm(outfile):
  make_mp3(f"""
    X:0
    M:4/4
    L:1/4
    Q:60
    K:C
    %%MIDI program {ALARM_INSTRUMENT}
    |cccc|z4""", outfile)

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

