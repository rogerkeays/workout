
import os, inspect, re

# constants 
SLOW = 60
MAKE_MP3S = False
GOALDIR = "practise"

# global state
os.mkdir(GOALDIR)
os.chdir(GOALDIR)
seen = set()

#
# Make a new directory of cards and change into that directory.
# The caller of this function is responsible for changing back
# to the original directory when the cards have been generated.
# This function resets the set of seen cards.
#
def mcd(dirname):
  os.makedirs(dirname)
  os.chdir(dirname)
  seen.clear()

#
# make a drill card, ensuring it is unique, and formatting
# it appropriately as a text file
#
def make_card(params={}, reps=5):

  # check for duplicates
  name = inspect.stack()[1].function
  hash = make_hash(name, params)
  if hash in seen: return False
  seen.add(hash)

  # build card text
  score = ""
  legend = ""
  for key in params:
    if params[key]:
      letter = key[0].upper()
      score += letter + " "
      legend += letter + " " + key + "\n"
      if isinstance(params[key], list):
        score += " ".join(params[key]) + "\n"
      else:
        score += str(params[key]) + "\n"

  # write card
  with open(cardnum() + "A.txt", "w") as f:
    f.write(name + " x" + str(reps) + "\n" + score + "\n" + legend + "\n")

  return True

#
# hash a drill with the given parameters, such that combinations
# resulting in the same physics result in the same value
#
def make_hash(name, params):
  keys = params.copy()
  if "lyrics" in keys: del keys["lyrics"]
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
def cardnum():
  return str(len(seen)).zfill(2)

def make_metronome(tempo):
  make_mp3("""
  X:0
  M:4/4
  L:1/4
  Q:100
  K:C
  %%MIDI program 115
  |:cccc|cccc|cccc|cccc|cccc|cccc|cccc|cccc:|
  |:cccc|cccc|cccc|cccc|cccc|cccc|cccc|cccc:|
  """, 0, tempo, "T" + str(tempo).zfill(3) + ".mp3")

#
# use MIDI instrument number (abc instrument number is zero-based)
# default to trumpet (57), because it is closest to perfect pitch
#
def make_drone(note, instrument=57):
  make_mp3("""
  X:0
  M:1/1
  L:1/1
  Q:10
  K:C transpose={transpose}
  %%MIDI program {instrument}
  |C,,,,|
  """.format(transpose=note_to_decimal(note), instrument=instrument - 1), 
  0, 100, "../../../P0" + note + ".mp3")

#
# convert an abc score to an mp3 file
#
def make_mp3(score, transpose=0, tempo_percent=100, filename=""):
  if MAKE_MP3S:
    key = str(locals())
    outfile = filename if filename else cardnum() + "B.mp3"
    os.system("""echo '{score}' \
        | abc2midi /dev/stdin -o /dev/stdout \
        | timidity - --quiet --quiet --output-24bit -A800 -K{transpose} -T{tempo_percent} -Ow -o - \
        | ffmpeg -loglevel error -i - -ac 1 -ab 64k "{outfile}"
        """.format(**locals()))

def make_chunk(mp3, speed, start_secs, stop_secs, padding=2.5, silence=5):
  if MAKE_MP3S and stop_secs > 0:
    ss = start_secs - padding
    to = stop_secs + padding
    st = stop_secs - start_secs + padding
    outfile = cardnum() + "B.mp3"
    os.system("""
    ffmpeg -nostdin -loglevel error -ss {ss} -to {to} -i {mp3} -ac 1 -ar 48000 -q 4 \
           -af afade=d={padding},afade=t=out:st={st}:d={padding},atempo={speed},adelay={silence}s:all=true \
           "{outfile}"
           """.format(**locals()))

def make_whole(mp3, speed, silence=0):
  if MAKE_MP3S:
    outfile = cardnum() + "B.mp3"
    os.system("""
    ffmpeg -nostdin -loglevel error -i {mp3} -ac 1 -ar 48000 -q 4 \
           -af atempo={speed},adelay={silence}s:all=true "{outfile}"
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

