#!/usr/bin/env python3

import os, inspect

#
# Add a card to the queue, indexed by the number of descendants in the
# dependency hierarchy. Returns the total number of descendants of the
# new card.
#
seen = set()
drills = []
def add_card(params = {}):
  name = inspect.stack()[1].function
  key = name + str(params)
  if key not in seen:
    seen.add(key)
    drills.append((name, params))

#
# Write cards to text files.
#
def write_cards(dir):
  os.makedirs(dir, exist_ok=True)
  for i, drill in enumerate(drills):
    name = drill[0]
    params = drill[1]
    idx = str(i).zfill(4)
    print(idx + " " + name + " " + str(params))
    with open(dir + "/" + idx + ".X00.txt", "w") as f:
      f.writelines(name + "\n")
      for key in params:
        f.write(key + "=" + str(params[key]) + "\n")
  drills.clear()

