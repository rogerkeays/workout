# vim: foldmethod=marker foldmarker=Phrase,), foldtext=getline(v\:foldstart)

import sys; sys.path.append("..")
from violin import *

process_piece(Piece("the-crawl", "01.the-crawl.mp3", [
  Section(4, 90, "37", [
    Phrase(10.16, 15.38, parse_violin_notes("""
      1 0 0N0 43LM li-
      2 = === =5== ttle
      3 7 === 33== ba-
      4 = === =5== by
      1 2 === 23== crawls
      2 = === =5== to
      3 9 === 13== dan-
      4 = === =5== ger""")
    ),
    Phrase(15.38, 21.53, parse_violin_notes("""
      1 2 0N0 23LM scared
      2 = === =5== he
      3 7 === 33== turns
      4 = === =5== round
      1 2 === 23== in
      2 = === =5== a
      3 7 === 33== cir-
      4 = === =5== cle""")
    ),
  ])
]))

