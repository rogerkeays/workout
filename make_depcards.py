#!/usr/bin/env python3

import inspect, os

#
# Add a card to the queue, using the stacktrace to determine its depth in
# the dependency tree. Cards deeper in the dependency hierarchy get higher
# priority.
#
drills = []
def push(name, **p): 
  drills.append((-len(inspect.stack()), (name, p)))

#
# Sort and write cards to text files.
#
def write_cards(dir):
  seen = set()
  os.makedirs(dir, exist_ok=True)
  drills.sort(key = lambda x: x[0])
  for drill in drills:
    name = drill[1][0]
    params = drill[1][1]
    key = name + str(params)
    if key not in seen:
      seen.add(key)
      num = str(len(seen)).zfill(4)
      with open(dir + "/" + num + ".txt", "w") as f:
        f.writelines(name + "\n")
        for key in params:
          f.write(key + "=" + str(params[key]) + "\n")
  drills.clear()

