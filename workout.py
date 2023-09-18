#!/usr/bin/env python3

import os, inspect

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

