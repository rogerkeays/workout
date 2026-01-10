# vim: foldmethod=marker foldmarker=phrase,)) foldtext=getline(v\:foldstart)

import sys; sys.path.append("..")
from violin import *

# @siem reap river
process(Piece(35, "musette", 4, 120, "42", [
  Section("bank", "A", [
    phrase("fishing", 9.77, 14.07, notes("""
      1 7 L44= 32W4 3 i'm
      3 5 ==== ===3 5 go-
      e 4 ==== ===2 3 ing
      4 2 ==== ===1 5 fish-
      o 0 ==== ===0 3 ing,
      1 7 ==== ===4 5 i'm
      3 5 ==== ===3 3 go-
      e 4 ==== ===2 5 ing
      4 2 ==== ===1 3 fish-
      o 0 ==== ===0 5 ing
      1 Z ==== ==== 3 ."""
    )),
    phrase("tackle", 14.07, 17.87, notes("""
      1 4 L44= 32W2 3 go-
      a 5 ==== ===3 5 nna
      2 7 S=== ===4 3 sit
      3 5 ==== ===3 5 down
      4 4 ==== ===2 ^ and
      1 2 L=== ===1 3 choose
      2 7 ==== ===4 5 some
      3 4 S=== ===2 3 ta-
      4 0 ==== ===0 5 ckle
      1 Z ==== ==== 3 ."""
    )),
    repeat("fishing", 17.87, 21.93),
    phrase("bait", 21.93, 25.84, notes("""
      1 4 L44= 32W2 3 go-
      a 5 ==== ===3 5 nna
      2 7 S=== ===4 3 sit
      3 5 ==== ===3 5 down
      4 4 ==== ===2 ^ and
      1 2 L=== ===1 3 choose
      2 7 ==== ===4 5 some
      3 0 ==== ===0 3 bait
      w Z ==== ==== 5 ."""
    )),
  ]),
  Section("water", "B", [
    phrase("food", 25.84, 29.69, notes("""
      1 Y D44= 22W2 3 here
      a 0 ==== ===3 5 it
      2 2 S=== ===4 3 comes,
      3 Y D=== ===2 5 here
      e 0 ==== ===3 3 it
      4 2 S=== ===4 5 comes,
      1 4 ==== 1==0 3 more
      2 9 ==== ===3 5 free
      3 4 L=== ===0 3 food
      1 Z ==== 2=== 5 ."""
    )),
    phrase("steal", 29.69, 33.59, notes("""
      1 Y D44= 22W2 5 care-
      a 0 ==== ===3 3 ful-
      2 2 S=== ===4 5 ly,
      3 Y D=== ===2 3 care-
      e 0 ==== ===3 5 ful-
      4 2 S=== ===4 3 ly,
      1 Y ==== ===3 5 ste-
      2 9 ==== ===2 3 al
      3 7 L=== ===0 5 it
      1 Z ==== ==== 3 ."""
    )),
    repeat("food", 33.59, 37.43),
    phrase("strike", 37.43, 41.55, notes("""
      1 4 S44= 12W0 5 big
      2 9 ==== ===4 ^ strike,
      3 2 ==== ===0 3 think
      e Y ==== 2==2 5 it
      4 9 ==== ===1 3 got
      o 7 ==== ===0 5 a-
      1 4 ==== 3==2 3 way
      1 Z ==== ==== 5 ."""
    )),
  ]),
  Section("bank", "A", [
    repeat("fishing", 9.77, 14.07),
    repeat("tackle", 14.07, 17.87),
    repeat("fishing", 17.87, 21.93),
    repeat("bait", 21.93, 25.84)
  ]),
]))

