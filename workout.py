#!/usr/bin/env python3

import os, inspect, re

seen = set()
drills = []
def make_card(params = {}, dir="drills"):
  name = inspect.stack()[1].function
  key = name + str(params)
  if key not in seen:
    seen.add(key)
    os.makedirs(dir, exist_ok=True)
    drillnum = str(len(seen)).zfill(4)
    print(drillnum + " " + name + " " + str(params))
    with open(dir + "/" + drillnum + ".FROGS0.txt", "w") as f:
      f.writelines(name + "\n")
      for key in params:
        f.write(key + "=" + str(params[key]) + "\n")

def half(val): return int(val / 2)

def phrase(tempo, lyrics, rhythm, melody, mechanics="", reps=5):
  for w in lyrics.split(" "):
    word(tempo, w, lyrics)
  del w
  make_card(locals())

def word(tempo, lyrics, phrase, reps=5):
  for n in re.split("[-. ]", lyrics):
    note(tempo, n, phrase)
  del n
  make_card(locals())

def note(tempo, lyrics, phrase, reps=5):
  make_card(locals())

def add(note, interval):
  return decimal_to_note(note_to_decimal(note) + note_to_decimal(interval))

def note_to_decimal(note):
  return int(str(note).replace("X", "A").replace("Y", "B"), 12)

def decimal_to_note(note):
  if not note:
    return "0"
  else:
    return decimal_to_note(note // 12).lstrip("0") + "0123456789XY"[note % 12]

