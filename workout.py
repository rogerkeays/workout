#!/usr/bin/env python3

import os, inspect, re

seen = set()
drills = []
goalnum = 1
outdir="drills"
def goal(name):
  global outdir, goalnum
  outdir="000." + str(goalnum).zfill(2) + "." + name
  os.makedirs(outdir, exist_ok=True)
  drills.clear()
  seen.clear()
  goalnum += 1

def make_card(params = {}):
  name = inspect.stack()[1].function
  key = name + str(params)
  if key not in seen:
    seen.add(key)
    drillnum = str(len(seen)).zfill(4)
    with open(outdir + "/" + drillnum + ".FROGS0.txt", "w") as f:
      f.writelines(name + "\n")
      for key in params:
        f.write(key + "=" + str(params[key]) + "\n")

def piece(tempo, name, reps=2):
  make_card(locals())

def phrase(tempo, lyrics, rhythm, melody, mechanics="", reps=5):
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

def half(val): return int(val / 2)

