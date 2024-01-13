
import os, inspect, re

# constants 
SLOW = 60
MAKE_MP3S = True

# global state
goaldir = "practise"
goalnum = 0
goalname = ""
goaltempo = 90
goalmp3 = ""
cards = set()
mp3s = set()

def goal(name, tempo=90, mp3=""):
  global goalnum, goalname, goaltempo, goalmp3
  os.makedirs(goaldir, exist_ok=True)
  goalnum += 1
  goalname = name
  goaltempo = tempo
  goalmp3 = mp3

def piece(tempo, name, *deps):
  del deps
  make_card(locals(), 1)
  make_metronome(tempo)
  if goalmp3:
    make_whole(goalmp3, tempo / goaltempo)

def make_card(params = {}, reps=5):
  name = inspect.stack()[1].function
  key = name + str(params)
  if key not in cards:
    cards.add(key)
    with open(goaldir + "/" + drillnum() + "A.txt", "w") as f:
      f.writelines(goalname + "\n")
      f.writelines(name + "\n")
      for key in params:
        if params[key]: f.write(key + "=" + str(params[key]) + "\n")
      f.write("reps=" + str(reps))

def drillnum():
  return str(len(cards)).zfill(4)

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
  """, 0, tempo, filename="X." + str(tempo).zfill(3) + ".mp3")

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
      outfile = goaldir + "/" + (filename if filename else drillnum() + "B.mp3")
      os.system("""echo '{score}' \
          | abc2midi /dev/stdin -o /dev/stdout \
          | timidity - --quiet --quiet --output-24bit -A800 -K{transpose} -T{tempo_percent} -Ow -o - \
          | ffmpeg -loglevel error -i - -ac 1 -ab 64k "{outfile}"
          """.format(**locals()))

def make_chunk(start_secs, stop_secs, tempo, padding=2.5, silence=5):
  if MAKE_MP3S and goalmp3 and stop_secs > 0:
    filename = goalmp3
    ss = start_secs - padding
    to = stop_secs + padding
    st = stop_secs - start_secs + padding
    tempo_mult = tempo / goaltempo
    outfile = goaldir + "/" + drillnum() + "B.mp3"
    os.system("""
    ffmpeg -nostdin -loglevel error -ss {ss} -to {to} -i {filename} -ac 1 -ar 48000 -q 4 \
           -af afade=d={padding},afade=t=out:st={st}:d={padding},atempo={tempo_mult},adelay={silence}s:all=true \
           "{outfile}"
           """.format(**locals()))

def make_whole(filename, tempo_mult, silence=0):
  if MAKE_MP3S:
    outfile = goaldir + "/" + drillnum() + "C.mp3"
    os.system("""
    ffmpeg -nostdin -loglevel error -i {filename} -ac 1 -ar 48000 -q 4 \
           -af atempo={tempo_mult},adelay={silence}s:all=true \
           "{outfile}"
           """.format(**locals()))

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

