#!/usr/bin/env python3

import os

#
# Add a card to the queue, indexed by the number of descendants in the
# dependency hierarchy. Returns the total number of descendants of the
# new card.
#
seen = set()
drills = []
def append(name, params = {}, *deps):
  numdeps = sum(deps)
  key = name + str(params)
  if key not in seen:
    seen.add(key)
    drills.append((name, params, numdeps))
  return numdeps + 1

#
# Sort and write cards to text files.
#
def write_cards(dir):
  os.makedirs(dir, exist_ok=True)
  drills.sort(key = lambda x: x[2])
  for i, drill in enumerate(drills):
    name = drill[0]
    params = drill[1]
    numdeps = str(drill[2]).zfill(4)
    print(numdeps + " " + name + " " + str(params))
    with open(dir + "/" + str(i).zfill(4) + ".txt", "w") as f:
      f.writelines(name + "\n")
      for key in params:
        f.write(key + "=" + str(params[key]) + "\n")
  drills.clear()

