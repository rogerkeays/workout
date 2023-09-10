#!/usr/bin/env python3

import os

#
# Add a card to the queue, indexed by the number of descendants in the
# dependency hierarchy.
#
seen = set()
drills = []
def push(name, params = {}, *deps):
  numdeps = sum(deps)
  key = name + str(params)
  if key not in seen:
    seen.add(key)
    drills.append((numdeps, name, params))
  return numdeps + 1

#
# Sort and write cards to text files.
#
def write_cards(dir):
  os.makedirs(dir, exist_ok=True)
  drills.sort(key = lambda x: x[0])
  for i, drill in enumerate(drills):
    deps = str(drill[0]).zfill(4)
    name = drill[1]
    params = drill[2]
    print(deps + " " + name + " " + str(params))
    with open(dir + "/" + str(i).zfill(4) + ".txt", "w") as f:
      f.writelines(name + "\n")
      for key in params:
        f.write(key + "=" + str(params[key]) + "\n")
  drills.clear()

