# vim: foldmethod=marker foldmarker=Phrase,), foldtext=getline(v\:foldstart)

import sys; sys.path.append("..")
from violin import *

process_piece(Piece("the-crawl", "01.the-crawl.mp3", [
  Section(4, 90, "37", [
    Phrase(10.16, 15.38, parse_violin_notes("""
      1= 0 40N0 3=LM li-
      2= = ==== 5=== ttle
      3= 7 3=== 3=== ba-
      4= = ==== 5=== by
      1= 2 2=== 3=== crawls
      2= = ==== 5=== to
      3= 9 1=== 3=== dan-
      41 = ==== 53== ger""")
    ),
    Phrase(15.38, 21.53, parse_violin_notes("""
      1= 2 20N0 3=LM scared
      2= = ==== 5=== he
      3= 7 3=== 3=== turns
      4= = ==== 5=== round
      1= 2 2=== 3=== in
      2= = ==== 5=== a
      3= 7 3=== 3=== cir-
      41 = ==== 53== cle""")
    ),
  ])
]))

