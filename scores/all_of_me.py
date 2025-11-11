# vim: foldmethod=marker foldmarker=\ phrase(,) foldtext=getline(v\:foldstart)

import sys; sys.path.append("..")
from violin import *

process_piece(Piece("all-of-me", 4, 126, "48", [
  Section("art-desk", "V1", [
    phrase("mouth", notes("""
      3 2 L4== 21W1 2 what
      e 4 ==== ===2 ^ would
      4 = ==== ==== 6 i
      1 = ==== ==== 2 do
      a = ==== ==== 4 with-
      2 2 ==== ===1 2 o-
      u 4 ==== ===2 4 ut
      3 = ===~ ==== 2 your
      4 0 ===~ 3=C4 6 smart
      1 = ===~ ==== 2 mouth?
      2 Z ==== ==== 6 ."""), 23.51, 27.31),
    phrase("drawin", notes("""
      3 2 L4== 21W1 2 draw-
      e 4 ==== ===2 v in
      4 = ==== ==== 6 me
      1 = ==== ==== 2 in
      a 2 ==== ===1 v a
      2 4 ==== ===2 6 you
      3 = ==== ==== 2 kick-
      e 2 ==== ===1 4 in
      4 0 ==== 3=C4 2 me
      o = ==== ==== 4 a-
      1 9 ==== ===2 2 out
      2 Z ==== ==== 6 ."""), 27.31, 31.12),
    phrase("spinnin", notes("""
      u 9 L4== 31C2 6 you've
      3 4 ==== 2=W= 4 got
      t = ==== ==== 7 my
      1 5 ==== ===3 2 head
      3 4 ==== ===2 v spin-
      e 0 ==== 3=C4 7 nin
      4 Z ==== ==== 2 ,
      1 5 ==== 2=W3 2 no
      3 4 ==== ===2 v kid-
      e 0 ==== 3=C4 7 din
      4 Z ==== ==== 3 ."""), 31.12, 35.85),
    phrase("pin", notes("""
      o 0 L4== 31C4 3 i
      1 2 ==== 2=W1 2 can't
      u Z ==== ==== 5 ,
      3 4 ==== ===2 v pin
      e 2 ==== ===1 7 yo-
      o 9 ==== 3=C2 ^ u
      1 = ==== ==== 2 down
      u Z ==== ==== 6 ."""),  35.85, 38.95)
  ]),
  Section("disneyland", "V2", [
    phrase("mind", notes("""
      3 2 L4== 21W1 2 what's
      e 4 ==== ===2 v go-
      4 = ==== ==== 6 in
      1 = ==== ==== 2 on
      a 2 ==== ===1 v in
      2 4 ==== ===2 6 that
      3 = ==== ==== 2 beau-
      e 2 ==== ===1 v ti-
      4 0 ==== 3=C4 6 ful
      w = ==== ==== 2 mind
      2 Z ==== ==== 6 ?"""), 38.95, 42.67),
    phrase("ride", notes("""
      3 4 L4== 21W2 6 i'm
      e = ==== ==== 4 on
      4 = ==== ==== 6 your
      1 7 ==== ===4 2 ma-
      a 5 ==== ===3 v gi-
      2 4 ==== ===2 6 cal
      3 = ==== ==== 2 mys-
      e 2 ==== ===1 v te-
      4 0 ==== 3=C4 6 ry-
      o = ==== ==== 4 r-
      1 9 ==== ===2 6 ide
      u Z ==== ==== 2 ."""), 42.67, 46.57),
    phrase("dizzy", notes("""
      3 4 L4== 21W2 2 and
      e = ==== ==== 6 i'm
      1 5 ==== ===3 2 so
      3 4 ==== ===2 v di-
      e 0 ==== 3=C4 7 zzy
      4 Z ==== ==== 3 ,
      o = ==== ==== ^ don't
      1 4 ==== 2=W2 2 kn-
      b 5 ==== ===3 v ow
      2 = ==== ==== 6 what
      3 4 ==== ===2 4 hit
      e 0 ==== 3==4 6 me
      4 Z ==== ==== 3 ."""), 46.57, 51.03),
    phrase("alright", notes("""
      o 0 L4== 31C4 3 but
      1 2 ==== 2=W1 2 i'll
      3 4 ==== ===2 5 be
      e 2 ==== ===1 7 al-
      1 5 ==== ===3 2 right
      e Z ==== ==== 6 ."""), 51.03, 54.92)
  ]),
  Section("show", "B1", [
    phrase("underwater", notes("""
      o 0 L4== 33W3 6 my
      1 7 ==== 2=G3 2 h-
      b 9 ==== ===4 v ead's
      u 7 ==== ===3 6 u-
      3 5 ==== ===2 ^ n-
      e = ==== ==== 2 de-
      4 4 ==== ===1 v r
      o = ==== ==== 6 wa-
      u 2 ==== 3=W4 2 te-
      3 0 ==== ===3 v r
      e = ==== ===3 6 but
      4 Z ==== ==== 2 ."""), 54.92, 58.71),
    phrase("breathin", notes("""
      o Y L4== 33W2 2 i'm
      u 9 ==== =1=2 6 br-
      3 7 ==== ===1 ^ ea-
      e = ==== ==== 2 th-
      4 9 ==== ===2 v in
      o = ==== ==== 6 fine
      u Z ==== ==== 2 ."""), 58.71, 62.57),
    phrase("crazy", notes("""
      o 7 L4== 24P2 2 y-
      w 9 ==== ===3 v ou're
      u = ==== ==== 6 cr-
      3 7 ==== ===2 ^ a-
      e = ==== ==== 2 zy
      4 5 ==== ===1 6 and
      o 4 ==== 35G4 2 i'm
      u = ==== ==== 6 o-
      3 2 ==== ===3 ^ ut
      e = ==== ==== 2 of
      4 0 ==== ===2 4 my
      o 2 ==== ===3 2 mind
      3 Z ==== ==== 6 ."""), 62.57, 68.21)
  ]),
  Section("mirrors", "C1A", [
    phrase("all-me", notes("""
      o 4 L4== 21W2 4 cause
      1 = ==== ==== 2 a-
      b 7 ==== ===4 v a-
      3 = ==== ==== 6 ll
      4 4 ==== ===2 2 of
      o 7 ==== ===4 5 m-
      1 9 ==== 1==1 2 e
      2 Z ==== ==== 4 ."""), 68.21, 71.10),
    phrase("all-you", notes("""
      3 4 L4== 21W3 4 loves
      1 2 ==== ===2 2 all
      4 0 ==== 3=C4 6 of
      o 2 ==== 2=W3 4 y-
      1 4 ==== ==== 2 ou
      2 Z ==== ==== 6 ."""), 71.10, 74.68),
    phrase("curves", notes("""
      3 4 L4== 21W2 2 love
      e = ==== ==== 6 you-
      o 2 ==== ===1 ^ r
      1 = ==== ==== 3 curves
      2 = ==== ==== 5 and
      3 = ==== ==== 3 all
      4 0 ==== 3=C4 5 your
      o 2 ==== 2=W1 ^ ed-
      1 0 ==== 3=C4 3 ges
      2 Z ==== ==== 5 ."""), 74.86, 78.86),
    lyrics("imperfections", "all you-r per-fect im-per-fec-tions", "curves", 78.86, 82.63)
  ]),
  Section("sepulchre", "C1B", [
    phrase("give-your", notes("""
      3 4 L4== 21W2 3 give
      e = ==== ==== 5 your
      1 = ==== ==== 3 a-
      b 7 ==== ===4 v ll
      4 4 ==== ===2 7 to
      o 7 ==== ===4 ^ m-
      1 9 ==== 1==1 3 e
      2 Z ==== ==== 6 ."""), 82.63, 86.35),
    phrase("give-my", notes("""
      u 2 L4== 21W1 6 i'll
      3 9 ==== 1=== 3 give
      e 4 ==== 2==2 5 m-
      o 2 ==== ===1 ^ y
      1 = ==== ==== 3 all
      4 0 ==== 3=C4 7 to
      o 2 ==== 2=W1 ^ yo-
      1 4 ==== ===2 3 u
      2 Z ==== ==== 5 ."""), 86.35, 90.10),
    lyrics("end", "you're m-y end and my be-gin-ing", "curves", 90.10, 94.17),
    lyrics("lose", "e-ve-n when i lose i'm win-ning", "curves", 94.17, 97.70)
  ]),
  Section("altar", "C1O", [
    phrase("i-give", notes("""
      u 4 L4== 21W2 6 cause
      3 = ==== ==== 7 i
      e 5 ==== ===3 ^ give
      4 7 ==== ===4 ^ you
      o 0 ==== 1==3 2 a-
      u Y ==== ===2 6 u-
      p 0 ==== ===3 ^ i-
      3 Y ==== ===2 ^ a-
      o 9 ==== ===1 2 a-
      u 7 ==== 2==4 v ll
      3 Z ==== ==== 7 ,
      4 4 ==== ===2 7 of
      o = ==== ==== 4 me
      u Z ==== ==== 6 ."""), 97.70, 105.29),
    lyrics("you-give", "and you give me a-u-i-a-a-ll of you", "i-give", 105.29, 111.83),
    phrase("oo", notes("""
      4 4 L4== 21W2 6 oh-
      o 2 ==== ===1 2 o
      3 Z ==== ==== 6 ."""), 111.83, 115.05)
  ]),
  Section("bedroom", "V3", [
    phrase("times", notes("""
      3 2 L4== 21W1 2 how
      e 4 ==== ===2 v ma-
      4 2 ==== ===1 6 ni-
      m 4 ==== ===2 ^ y
      1 2 ==== ===1 2 t-
      a 4 ==== ===2 v imes
      2 = ==== ==== 6 do
      u 2 ==== ===1 ^ i
      3 4 ==== ===2 2 have
      e 2 ==== ===1 v to
      4 0 ==== 3=C4 6 tell
      1 = ==== ==== 2 you?
      2 Z ==== ==== 6 ."""), 115.05, 118.98),
    phrase("crying", notes("""
      3 4 L4== 21W2 2 e-
      e = ==== ==== 4 ven
      4 = ==== ==== 2 when
      o = ==== ==== 4 you're
      1 5 ==== ===3 2 c-
      b 7 ==== ===4 v ry-
      2 5 ==== ===3 6 ing
      u 4 ==== ===2 ^ you're
      3 = ==== ==== 2 beau-
      e 2 ==== ===1 v ti-
      4 0 ==== 1=C4 6 ful
      o = ==== ==== 4 t-
      1 9 ==== ===2 6 oo
      2 Z ==== ==== 4 ."""), 118.98, 122.55),
    phrase("beating", notes("""
      u 0 L4== 31C4 6 the
      3 2 ==== 2=W1 2 w-
      c 4 ==== ===2 v orld
      t = ==== ==== 6 is
      1 5 ==== ===3 2 beat-
      u 4 ==== ===2 6 i-
      p 5 ==== ===3 ^ i-
      3 4 ==== ===2 ^ ing
      e 0 ==== 3=C4 2 you
      o 4 ==== 2=W2 6 d-
      1 5 ==== ===3 ^ own
      u 4 ==== ===2 2 i-
      e 0 ==== 3=C4 v m
      4 = ==== ==== 6 a-
      o 2 ==== 2=W1 2 round
      2 Z ==== ==== 6 ."""), 122.55, 128.17),
    phrase("mood", notes("""
      u 2 L4== 21W1 6 through
      3 4 ==== ===2 2 e-
      e 2 ==== ===1 v ve-
      4 = ==== ==== 6 ry
      o 9 ==== 3=C2 2 mood
      2 Z ==== ==== 6 ."""), 128.17, 130.19)
  ]),
  Section("garage", "V4", [
    phrase("downfall", notes("""
      p 7 L4== 21W4 2 you're
      e 4 ==== ===2 4 my
      o = ==== ==== 2 down-
      a 0 ==== 3=C4 6 fall,
      3 7 ==== 2=W= 2 you're
      e 4 ==== ===2 4 my
      o = ==== ==== 2 muse
      a Z ==== ==== 6 ."""), 130.19, 133.97),
    phrase("distraction", notes("""
      u 0 L4== 31C4 6 my
      3 5 ==== 2=W3 2 w-
      e 7 ==== ===4 v orst
      4 4 ==== ===2 6 dis-
      o = ==== ==== 2 tra-
      1 2 ==== ===1 v ac-
      a = ==== ==== 6 tion,
      u = ==== ==== 2 my
      3 4 ==== ===2 4 rhy-
      e 2 ==== ===1 2 thm
      4 4 ==== ===2 4 n
      o 9 ==== 3=C2 2 blues
      2 Z ==== ==== 6 ."""), 133.97, 137.69),
    phrase("singing", notes("""
      u 4 L4== 21W2 6 i
      3 = ==== ==== 4 can't
      t = ==== ==== 6 stop
      1 5 ==== ===3 2 si-
      u 4 ==== ===2 6 ngi-
      3 0 ==== 3=C4 4 ing
      e = ==== ==== 6 it's
      4 Z ==== ==== 2 ,
      o 4 ==== 2=W2 2 ri-
      1 5 ==== ===3 v i-
      u 4 ==== ===2 6 ngi-
      3 0 ==== 3=C4 4 ing
      e = ==== ==== 6 in
      4 Z ==== ==== 2 ."""), 137.69, 142.49),
    phrase("head", notes("""
      o 2 L4== 21W1 2 my
      2 Z ==== ==== 6 ,
      u 4 ==== ===2 6 h-
      e 2 ==== ===1 ^ ead
      4 = ==== ==== 2 for
      o 4 ==== ===2 6 y-
      1 5 ==== ===3 ^ ou
      4 Z ==== ==== 2 ."""), 142.49, 150.28)
  ]),
  Section("show", "B2", [
    repeat("underwater", 146.37, 150.29),
    repeat("breathin", 150.29, 153.91),
    repeat("crazy", 153.91, 159.74)
  ]),
  Section("mirrors", "C2A", [
    repeat("all-me", 159.74, 162.63),
    repeat("all-you", 162.63, 166.38),
    repeat("curves", 166.38, 170.37),
    repeat("imperfections", 170.37, 175.05)
  ]),
  Section("sepulchre", "C2B", [
    repeat("give-your", 175.05, 177.75),
    phrase("give-my^", notes("""
      u 4 L4== 21W2 6 i'll
      3 0 ==== 1==3 3 give
      e Y ==== ===2 5 m-
      o 9 ==== ===1 ^ y
      1 = ==== ==== 3 all
      4 7 ==== 2==4 7 to
      o 4 ==== ===2 3 you
      2 Z ==== ==== 5 ."""), 177.75, 181.63),
    repeat("end", 181.63, 185.64),
    repeat("lose", 185.64, 189.20),
  ]),
  Section("altar", "C2O", [
    repeat("i-give", 189.20, 196.79),
    repeat("you-give", 196.79, 204.06)
  ]),
  Section("casino", "M", [
    phrase("give-me", notes("""
      a 5 L4== 21W3 3 give
      2 7 ==== ===4 5 me
      u Y ==== 1==2 3 a-
      3 0 ==== ===3 v ll
      e Y ==== ===2 5 of
      4 9 ==== ===1 3 you
      u 7 ==== 2==4 6 o-
      p 5 ==== ===3 ^ u-
      3 4 ==== ===2 ^ o-
      c 2 ==== ===1 ^ u-
      e 0 ==== 3=C4 ^ oh
      1 Z ==== ==== 1 ."""), 204.06, 207.59),
    phrase("cards", notes("""
      1 9 L4== 11W2 3 cards
      u 7 ==== 2==1 5 o-
      3 5 ==== ===4 ^ n
      e = ==== ==== 3 the
      o Y ==== 1==3 6 t-
      1 0 ==== ===4 ^ a-
      u Y ==== ===3 2 b-
      3 9 ==== ===2 v le
      e = ==== ==== 6 w-
      4 7 ==== 2==1 ^ e're
      o = ==== ==== 2 both
      u 5 ==== ===4 6 sh-
      3 4 ==== ===3 ^ o-
      e = ==== ==== 2 w-
      4 2 ==== ===2 v ing
      o = ==== ==== 6 hearts
      e Z ==== ==== 2 ."""), 207.59, 215.01),
    phrase("risk", notes("""
      1 9 L4== 11W1 2 ris-
      u 7 ==== 2==4 6 king
      3 5 ==== ===3 ^ it
      o 5 ==== 1==2 2 a-
      1 0 ==== ===3 v ll
      u Y ==== ===2 6 th-
      3 9 ==== ===1 ^ ough
      e = ==== ==== 2 it's
      o 7 ==== 2==4 6 hard
      3 Z ==== ==== 2 ."""), 215.01, 220.54)
  ]),
  Section("mirrors", "C3A", [
    repeat("all-me", 220.54, 223.52),
    repeat("all-you", 223.52, 227.34),
    repeat("curves", 227.34, 231.31),
    repeat("imperfections", 231.31, 235.15)
  ]),
  Section("sepulchre", "C3B", [
    repeat("give-your", 235.15, 238.65),
    repeat("give-my^", 238.65, 242.60),
    repeat("end", 242.60, 246.55),
    repeat("lose", 246.55, 250.20)
  ]),
  Section("altar", "C3O1", [
    repeat("i-give", 250.20, 257.77),
    repeat("you-give", 257.77, 265.26)
  ]),
  Section("altar", "C3O2", [
    phrase("i-give-auaua", notes("""
      3 4 L4== 21W2 7 i
      e 5 ==== ===3 ^ give
      4 7 ==== ===4 ^ you
      o 0 ==== 1==3 2 a-
      2 2 ==== ===4 v u-
      u Y ==== ===2 6 a-
      4 0 ==== ===3 ^ u-
      o 9 ==== ===1 2 a-
      u 7 ==== 2==4 v ll
      3 Z ==== ==== 7 ,
      4 4 ==== ===2 7 of
      o = ==== ==== 4 me
      3 Z ==== ==== 6 ."""), 265.26, 273.04),
    repeat("you-give", 273.04, 279.42),
    phrase("ouo", notes("""
      4 2 L4== 21W1 6 o-
      o 4 ==== ===2 ^ u-
      1 2 ==== ===1 ^ oh
      4 Z ==== ==== 1 ."""), 279.42, 282.03)
  ])
], "63.all-of-me.mp3"))

