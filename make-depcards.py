#!/usr/bin/env python3

import inspect

cards = []
def add(name, **p): 
  cards.append((-len(inspect.stack()), (name, p)))

def open_strings(string, **p):
  add("open strings", **p, string=string)

def string_xings(frm, to, **p):
  open_strings(string=frm, **p)
  open_strings(string=to, **p)
  add("string crossings", **p, frm=frm, to=to)

def single_string_xings(**p):
  string_xings(frm=1, to=2, **p)
  string_xings(frm=2, to=3, **p)
  string_xings(frm=3, to=4, **p)

def the_crawl():
  single_string_xings(tempo=90, bow="middle", motion="detache", rhythm="ma")

the_crawl()

seen = set()
cards.sort(key = lambda x: x[0])
for card in cards:
  key = card[1][0] + str(card[1][1])
  if key not in seen:
     print(str(card[1]))
     seen.add(key)

