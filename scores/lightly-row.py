# vim: foldmethod=marker foldmarker=phrase,\ ) foldtext=getline(v\:foldstart)

import sys; sys.path.append("..")
from violin import *

# @oxford
process_piece(Piece("lightly-row", 4, 90, "49", "27.lightly-row.mp3", [
  Section("riverbank", "A", [
    phrase("flamingo", notes("""
      1 7 L4== 22W4 3 light-
      2 4 ==== ===2 5 ly
      3 = ==== ==== 3 row,
      1 5 ==== ===3 5 fla-
      2 2 ==== ===1 3 min-
      3 = ==== ==== 5 go
      1 Z ==== ==== 3 ."""), 6.92, 10.52
    ),
    phrase("river", notes("""
      1 0 L4== 22W0 3 down
      2 2 ==== ===1 5 the
      3 4 ==== ===2 3 ri-
      4 5 ==== ===3 5 ver
      1 7 ==== ===4 3 we
      2 = ==== ==== 5 will
      3 = ==== ==== 3 go
      1 Z ==== ==== 5 ."""), 10.52, 14.12
    ),
    phrase("rowing", notes("""
      1 7 L4== 22W4 5 al-
      2 4 ==== ===2 3 ways
      3 = ==== ==== 5 row-
      4 = ==== ==== 3 ing
      1 5 ==== ===3 5 ne-
      2 2 ==== ===1 3 ver
      3 = ==== ==== 5 slow-
      4 = ==== ==== 3 ing
      1 Z ==== ==== 5 ."""), 14.12, 17.60
    ),
    phrase("canoe", notes("""
      1 0 L4== 22W0 5 in
      2 2 ==== ===1 3 my
      3 7 ==== ===4 5 bright
      4 = ==== ==== 3 big
      1 4 ==== ===2 5 red
      2 = ==== ==== 3 ca-
      3 = ==== ==== 5 noe
      1 Z ==== ==== 3 ."""), 17.60, 21.23
    )
  ]),
  Section("bridge", "B", [
    phrase("fishes", notes("""
      1 2 L4== 22W1 3 see
      2 = ==== ==== 5 the
      3 = ==== ==== 3 fish-
      4 = ==== ==== 5 es
      1 = ==== ==== 3 swim-
      2 4 ==== ===2 5 ming
      3 5 ==== ===3 3 by
      1 Z ==== ==== 5 ."""), 21.23, 24.85
    ),
    phrase("birds", notes("""
      1 4 L4== 22W2 3 see
      2 = ==== ==== 5 the
      3 = ==== ==== 3 birds
      4 = ==== ==== 5 up
      1 = ==== ==== 3 in
      2 5 ==== ===3 5 the
      3 7 ==== ===4 3 sky
      1 Z ==== ==== 5 ."""), 24.85, 28.58
    ),
    repeat("rowing", 28.58, 32.13),
    repeat("canoe", 32.13, 38.05)
  ])
]))

