
import os, inspect, re, tempfile, math

# constants 
MAKE_MP3S = True
TARGET_DIR = "target/"
DRILLS_DIR = "02.drills/"
BRACKETS_DIR = "03.practise/"
NUM_PADDING = 4
DRILL_LENGTH_MINS = 5
METRONOME_INSTRUMENT = 116 - 1 # woodblock
ALARM_INSTRUMENT = 128 - 1     # gunshot
DRONE_INSTRUMENT = 57 - 1      # trumpet (closest to perfect pitch)

# global state
os.mkdir(TARGET_DIR)
os.chdir(TARGET_DIR)
os.mkdir(DRILLS_DIR)
os.mkdir(BRACKETS_DIR)
drills = set()
brackets = 0

#
# Make a new directory of cards and change into that directory.
# The caller of this function is responsible for changing back
# to the original directory when the cards have been generated.
#
def mcd(dirname):
  os.makedirs(dirname)
  os.chdir(dirname)

def make_bracket(title, tempo, params={}, reps=5):
  global brackets
  brackets += 1
  if "title" in params: del params["title"]
  if "tempo" in params: del params["tempo"]

  # write card text
  with open(BRACKETS_DIR + bracketnum() + "A.txt", "w") as f:
    f.write("TIT " + title + " @" + str(int(tempo)) + "\n")
    for key in params:
      if params[key]:
        f.write(key[0:3].upper() + " ")
        if isinstance(params[key], list):
          f.write(" ".join(params[key]) + "\n")
        else:
          f.write(str(params[key]) + "\n")

#
# make a drill card, ensuring it is unique, and formatting
# it appropriately as a text file
#
def make_drill(params={}, reps=5):

  # check for duplicates
  name = inspect.stack()[1].function
  hash = make_hash(name, params)
  if hash in drills: return False
  drills.add(hash)

  # write card text
  with open(DRILLS_DIR + drillnum() + "A.txt", "w") as f:
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
def bracketnum():
  depth = len(inspect.stack()) - 5
  return str(depth) + str(brackets).zfill(NUM_PADDING - 1)

#
# make a metronome with the given tempo which goes for DRILL_LENGTH_MINS
# before sounding an alarm
#
# note: abc2midi miscalculates when tempo < 4, so we multiply the tempo by 4
# and set the midi speed to 25%
#
def make_metronome(tempo):
  num_notes = int(DRILL_LENGTH_MINS * tempo)
  filename = "=T" + str(int(tempo)).zfill(NUM_PADDING - 1) + ".mp3"
  make_mp3(("""
    X:0
    M:1/4
    L:1/4
    Q:{t}
    K:C
    %%MIDI program {M}
    """ + ("|c" * num_notes) + """"
    %%MIDI program {A}
    Q:240
    |C|C|C|C|z|z|z|z""").format(t=tempo*4, M=METRONOME_INSTRUMENT, A=ALARM_INSTRUMENT),
    DRILLS_DIR + filename, tempo_percent=25)

#
# make a drone of a single pitch which lasts for DRILL_LENGTH_MINS
# and finishes with an alarm
#
def make_drone(note):
  make_mp3(("""
    X:0
    M:4/4
    L:1/4
    Q:4
    K:C transpose={t}
    %%MIDI program {I}
    """ + ("|C,,,,C,,,,C,,,,C,,,," * DRILL_LENGTH_MINS) + """
    %%MIDI program {A}
    Q:60
    |CCCC|z4""").format(t=note_to_decimal(note), I=DRONE_INSTRUMENT, A=ALARM_INSTRUMENT),
    DRILLS_DIR + drillnum() + "B.mp3")

#
# convert an abc score to an mp3 file
#
def make_mp3(score, filename, transpose=0, tempo_percent=100):
  if MAKE_MP3S:
    key = str(locals())
    if not os.path.exists(filename):
      os.system("""echo '{score}' \
          | abc2midi /dev/stdin -o /dev/stdout \
          | timidity - --quiet --quiet --output-24bit -A800 -K{transpose} -T{tempo_percent} -Ow -o - \
          | ffmpeg -loglevel error -i - -ac 1 -ab 64k "{filename}"
          """.format(**locals()))

def make_whole(mp3, speed=1, silence=0, suffix="B"):
  if MAKE_MP3S:
    outfile = BRACKETS_DIR + bracketnum() + suffix + ".mp3"
    os.system("""
    ffmpeg -nostdin -loglevel error -i {mp3} -ac 1 -ar 48000 -q 4 \
           -af atempo={speed},adelay={silence}s:all=true "{outfile}"
           """.format(**locals()))

def make_chunk(mp3, start_secs, stop_secs, padding=2.5, silence=5):
  if MAKE_MP3S and stop_secs > 0:
    with tempfile.TemporaryDirectory() as tmpdir:

      # make chunks at different tempos
      cut_chunk(mp3, start_secs, stop_secs, 0.5, tmpdir + "/050.mp3", padding, silence);
      cut_chunk(mp3, start_secs, stop_secs, 1.0, tmpdir + "/100.mp3", padding, silence);
      make_mp3(("""
        X:0
        M:4/4
        L:1/4
        Q:4
        K:C
        %%MIDI program {A}
        Q:60
        |cccc|z4""").format(A=ALARM_INSTRUMENT), tmpdir + "/alarm.mp3")

      # repeat for five minutes
      chunk_length = padding + stop_secs - start_secs + padding
      combo_length = silence + chunk_length + silence + 2 * chunk_length
      reps = math.ceil(300 / combo_length)
      with open(tmpdir + "/list", "w") as f:
        for i in range(reps):
          f.write("file {tmpdir}/050.mp3\nfile {tmpdir}/100.mp3\n".format(tmpdir=tmpdir))
        f.write("file {tmpdir}/alarm.mp3\n".format(tmpdir=tmpdir))

      # concatenate the chunks
      outfile = BRACKETS_DIR + bracketnum() + "B.mp3"
      os.system("""
      ffmpeg -nostdin -loglevel error -f concat -safe 0 -i "{tmpdir}/list" \
             -codec copy "{outfile}"
             """.format(**locals()))

def cut_chunk(mp3, start_secs, stop_secs, speed, outfile, padding, silence):
  if MAKE_MP3S and stop_secs > 0:
    ss = start_secs - padding
    to = stop_secs + padding
    st = stop_secs - start_secs + padding
    os.system("""
    ffmpeg -nostdin -loglevel error -ss {ss} -to {to} -i {mp3} -ac 1 -ar 48000 -q 4 \
           -af afade=d={padding},afade=t=out:st={st}:d={padding},atempo={speed},adelay={silence}s:all=true \
           "{outfile}"
           """.format(**locals()))

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

