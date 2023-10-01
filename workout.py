#!/usr/bin/env python3

import os, inspect, re

# global state
goalnum = 1
outdir="drills"
cards = set()
mp3s = set()

def goal(name):
  global outdir, goalnum
  outdir="00." + str(goalnum).zfill(2) + "." + name
  os.makedirs(outdir, exist_ok=True)
  goalnum += 1
  cards.clear()
  mp3s.clear()

def piece(tempo, name, reps=2):
  make_card(locals())

def phrase(tempo, lyrics, rhythm, melody, mechanics="", reps=5):
  make_card(locals())

def make_card(params = {}):
  name = inspect.stack()[1].function
  key = name + str(params)
  if key not in cards:
    cards.add(key)
    drillnum = str(len(cards)).zfill(4)
    with open(outdir + "/" + drillnum + "A.txt", "w") as f:
      f.writelines(name + "\n")
      for key in params:
        f.write(key + "=" + str(params[key]) + "\n")

#
# convert an abc score to an mp3 file
#
def make_mp3(score, transpose=0, tempo_percent=100):
  global outdir
  key = str(locals())
  if key not in mp3s:
    mp3s.add(key)
    outfile = outdir + "/" + str(len(cards)).zfill(4) + "B.mp3"
    os.system("""echo '{score}' \
          | abc2midi /dev/stdin -o /dev/stdout \
          | timidity - --quiet --output-24bit -A800 -K{transpose} -T{tempo_percent} -Ow -o - \
          | ffmpeg -loglevel error -i - -ac 1 -ab 64k "{outfile}"
          """.format(**locals()))

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
  """, 0, tempo)

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

