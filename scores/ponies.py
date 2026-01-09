# vim: foldmethod=marker foldmarker=phrase,)) foldtext=getline(v\:foldstart)

import sys; sys.path.append("..")
from violin import *

# @art class
process(Piece("ponies", 3, 95, "42", "34.ponies.mp3", [
  Section("desk", "A", [
    phrase("girls", 12.68, 20.28, notes("""
      1 0 L44= 32G0 3 li-
      3 7 ==== ===4 5 ttle
      1 = ==== ==== 3 girls
      1 5 ==== ===3 5 like
      3 3 ==== ===2 3 to
      1 5 ==== ===3 5 draw
      1 Z ==== 21== 3 ."""
    )),
    phrase("ponies", 20.28, 27.69, notes("""
      1 X L44= 21P2 3 all
      3 2 ==== ===4 5 the
      1 7 ==== ===0 3 pre-
      u 5 ==== 32G3 5 tty
      3 3 ==== ===2 3 li-
      e 2 ==== ===1 5 ttle
      1 0 ==== ===0 3 po-
      1 = ==== ==== 5 nies
      1 = ==== 4=== 3 ."""
    )),
  ]),
  Section("desk", "A", [
    repeat("girls"),
    repeat("ponies")
  ]),
  Section("reverie", "B", [
    phrase("dreams", 41.61, 50.63, notes("""
      1 = L44= 42G1 3 in
      3 = ==== ===3 5 her
      1 = ==== ==== 3 dreams,
      1 = ==== 3==0 5 she
      2 = ==== ==== 3 walks
      3 = ==== ===2 v a-
      1 = ==== ==== 5 mong
      1 = ==== 2=== 3 ."""
    )),
    repeat("ponies")
  ]),
  Section("desk", "A", [
    repeat("girls"),
    repeat("ponies")
  ])
]))

