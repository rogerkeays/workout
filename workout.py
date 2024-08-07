
import os, inspect, re

# constants 
SLOW = 60
MAKE_MP3S = True

# global state
goaldir = "drills"
goaltempo = 90
goalmp3 = ""
cards = set()
mp3s = set()
counter = [0]
os.makedirs(goaldir, exist_ok=True)
os.chdir(goaldir)

def goal(name, tempo=90, mp3=""):
  global goaltempo, goalmp3
  goaltempo = tempo
  goalmp3 = mp3

def piece(tempo, name):
  make_card(locals(), 1, tempo)
  if goalmp3:
    make_whole(goalmp3, tempo / goaltempo)

#
# make a drill card, ensuring it is unique, and formatting
# it appropriately as a text file
#
def make_card(params={}, reps=5, tempo=0, start=0, stop=0):
  global counter
  name = inspect.stack()[1].function
  hash = make_hash(name, params)
  if hash in cards:
    return False
  cards.add(hash)

  drillnum = counter[-1] + 1
  dirname = pad2(drillnum) + "." + name + "/00"
  os.makedirs(dirname)
  os.chdir(dirname)
  counter[-1] = drillnum
  counter += [0]

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
        dirname += "." + letter + str(params[key])

  with open(strdrillnum() + ".txt", "w") as f:
    f.write(name + " x" + str(reps) + "\n" + score + "\n" + legend + "\n")

  if tempo > 0: make_metronome(tempo)
  if start > 0: make_chunk(tempo, start, stop)
  os.chdir("..")
  return True

def end_card():
  global counter
  os.chdir("..")
  counter = counter[0:-1]

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
def strdrillnum():
  return str(len(cards)).zfill(4)

def pad2(num): return str(num).zfill(2)

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
  """, 0, tempo, filename="01.metronome." + str(tempo).zfill(3) + ".mp3")

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
  """.format(transpose=note_to_decimal(note), instrument=instrument - 1))

#
# convert an abc score to an mp3 file
#
def make_mp3(score, transpose=0, tempo_percent=100, filename=""):
  if MAKE_MP3S:
    key = str(locals())
    if key not in mp3s:
      mp3s.add(key)
      outfile = filename if filename else "02.backing.mp3"
      os.system("""echo '{score}' \
          | abc2midi /dev/stdin -o /dev/stdout \
          | timidity - --quiet --quiet --output-24bit -A800 -K{transpose} -T{tempo_percent} -Ow -o - \
          | ffmpeg -loglevel error -i - -ac 1 -ab 64k "{outfile}"
          """.format(**locals()))

def make_chunk(tempo, start_secs, stop_secs, padding=2.5, silence=5):
  if MAKE_MP3S and goalmp3 and stop_secs > 0:
    filename = goalmp3
    ss = start_secs - padding
    to = stop_secs + padding
    st = stop_secs - start_secs + padding
    tempo_mult = tempo / goaltempo
    outfile = "02.backing.mp3"
    os.system("""
    ffmpeg -nostdin -loglevel error -ss {ss} -to {to} -i {filename} -ac 1 -ar 48000 -q 4 \
           -af afade=d={padding},afade=t=out:st={st}:d={padding},atempo={tempo_mult},adelay={silence}s:all=true \
           "{outfile}"
           """.format(**locals()))

def make_whole(filename, tempo_mult, silence=0):
  if MAKE_MP3S:
    outfile = "00/02.backing.mp3"
    os.system("""
    ffmpeg -nostdin -loglevel error -i {filename} -ac 1 -ar 48000 -q 4 \
           -af atempo={tempo_mult},adelay={silence}s:all=true \
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

