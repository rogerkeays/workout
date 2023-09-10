#!/usr/bin/env python3

from dataclasses import dataclass
from queue import PriorityQueue

@dataclass
class Goal: name: str; params: dict; deps: list;

def open_strings(string, **p):
  return Goal("open strings", { **p, "string": string }, [])

def string_xings(frm, to, **p):
  return Goal("string crossings", { **p, "from": frm, "to": to }, [
      open_strings(frm, **p),
      open_strings(to, **p)
  ])

def single_string_xings(**p):
  return Goal("", {}, [
      string_xings(frm=1, to=2, **p),
      string_xings(frm=2, to=3, **p),
      string_xings(frm=3, to=4, **p)
  ])

#def the_crawl():
#  single_string_xings(tempo=90, bow="middle", motion="detache", rhythm="ma")

queue = PriorityQueue(0)
def build_queue(goal, depth = 0):
  queue.put((depth, goal))
  for dep in goal.deps:
    build_queue(dep, depth + 1)

seen = set()
def print_deps():
  for goal in queue:
    if goal.name:
      key = goal.name + " " + str(goal.params)
      if key not in seen:
        print(key)
        seen.add(key)

build_queue(single_string_xings())
print_deps()

