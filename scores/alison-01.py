# vim: foldmethod=marker foldmarker=Phrase,\ ) foldtext=getline(v\:foldstart)

import sys; sys.path.append("..")
from violin import *

process_piece(Piece("the-crawl", 4, 90, "37", [
  Section("table", "V", [
    Phrase("crawls", parse_violin_notes("""
      1= 0 04N0 3v=LM li-
      2= = ==== 5^=== ttle
      3= 7 =3== 3v=== ba-
      4= = ==== 5^=== by
      1= 2 =2== 3v=== crawls
      2= = ==== 5^=== to
      3= 9 =1== 3v=== dan-
      41 = ==== 5^3== ger"""), 10.16, 15.38
    ),
    Phrase("scared", parse_violin_notes("""
      1= 2 02N0 3v=LM scared
      2= = ==== 5^=== he
      3= 7 =3== 3v=== turns
      4= = ==== 5^=== round
      1= 2 =2== 3v=== in
      2= = ==== 5^=== a
      3= 7 =3== 3v=== cir-
      41 = ==== 5^3== cle"""), 15.38, 21.53
    ),
  ])
], "01.the-crawl.mp3"))

