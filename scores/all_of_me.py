# vim: foldmethod=marker foldmarker=\ phrase(,) foldtext=getline(v\:foldstart)

import sys; sys.path.append("..")
from violin import *

process_piece(Piece("all-of-me", 4, 126, "48", [
  Section("art-desk", "V1", [
    phrase("mouth", notes("""
      3244 21W1 2^L= what
      e4== ===2 4^== would
      4=== ==== 6=== i
      1=== ==== 2=== do
      a=== ==== 4=== with-
      22== ===1 2=== o-
      u4== ===2 4=== ut
      3=== ==== 2==~ your
      40== 3=C4 6==~ smart
      1=== ==== 2==~ mouth?
      2Z== ==== 6.== ."""), 23.51, 27.31),
    phrase("drawin", notes("""
      3244 21W1 2vL= draw-
      e4== ===2 4v== in
      4=== ==== 6=== me
      1=== ==== 2=== in
      a2== ===1 4v== a
      24== ===2 6=== you
      3=== ==== 2=== kick-
      e2== ===1 4=== in
      40== 3=C4 2=== me
      o=== ==== 4=== a-
      19== ===2 2=== out
      2Z== ==== 6.== ."""), 27.31, 31.12),
    phrase("spinnin", notes("""
      u944 31C2 6^L= you've
      34== 2=W= 4=== got
      t=== ==== 7=== my
      15== ===3 2=== head
      34== ===2 5v== spin-
      e0== 3=C4 7=== nin
      4Z== ==== ==== ,
      15== 2=W3 2v== no
      34== ===2 5v== kid-
      e0== 3=C4 7=== din
      4Z== ==== 3.== ."""), 31.12, 35.85),
    phrase("pin", notes("""
      o044 31C4 3^L= i
      12== 2=W1 2=== can't
      uZ== ==== 5.== ,
      34== ===2 =v== pin
      e2== ===1 7=== yo-
      o9== 3=C2 4^== u
      1=== ==== 2=== down
      uZ== ==== 6.== ."""),  35.85, 38.95)
  ]),
  Section("disneyland", "V2", [
    phrase("mind", notes("""
      3244 21W1 2vL= what's
      e4== ===2 4v== go-
      4=== ==== 6=== in
      1=== ==== 2=== on
      a2== ===1 4v== in
      24== ===2 6=== that
      3=== ==== 2=== beau-
      e2== ===1 4v== ti-
      40== 3=C4 6=== ful
      w=== ==== 2=== mind
      2Z== ==== 6.== ?"""), 38.95, 42.67),
    phrase("ride", notes("""
      3444 21W2 6^L= i'm
      e=== ==== 4=== on
      4=== ==== 6=== your
      17== ===4 2=== ma-
      a5== ===3 4v== gi-
      24== ===2 6=== cal
      3=== ==== 2=== mys-
      e2== ===1 4v== te-
      40== 3=C4 6=== ry-
      o=== ==== 4=== r-
      19== ===2 6=== ide
      uZ== ==== 2.== ."""), 42.67, 46.57),
    phrase("dizzy", notes("""
      3444 21W2 2vL= and
      e=== ==== 6=== i'm
      15== ===3 2=== so
      34== ===2 5v== di-
      e0== 3=C4 7=== zzy
      4Z== ==== ==== ,
      o=== ==== 3^== don't
      14== 2=W2 2=== kn-
      b5== ===3 3v== ow
      2=== ==== 6=== what
      34== ===2 4=== hit
      e0== 3==4 6=== me
      4Z== ==== 3.== ."""), 46.57, 51.03),
    phrase("alright", notes("""
      o044 31C4 3=L= but
      12== 2=W1 2=== i'll
      34== ===2 5=== be
      e2== ===1 7=== al-
      15== ===3 2=== right
      eZ== ==== 6.== ."""), 51.03, 54.92)
  ]),
  Section("show", "B1", [
    phrase("underwater", notes("""
      o044 33W3 6=L= my
      17== 2=G3 2=== H-
      b9== ===4 4=== EAD'S
      u7== ===3 6=== u-
      35== ===2 4=== n-
      e=== ==== 2=== DE-
      44== ===1 4=== R
      o=== ==== 6=== wa-
      u2== 3=W4 2=== TE-
      30== ===3 4=== R
      e=== ===3 6=== but
      4Z== ==== 2.== ."""), 54.92, 58.71),
    phrase("breathin", notes("""
      oY44 33W2 2vL= i'm
      u9== =1=2 6=== br-
      37== ===1 4^== ea-
      e=== ==== 2=== th-
      49== ===2 4v== in
      o=== ==== 6=== fine
      uZ== ==== 2.== ."""), 58.71, 62.57),
    phrase("crazy", notes("""
      o744 24P2 2vL= y-
      w9== ===3 4v== ou're
      u=== ==== 6=== cr-
      37== ===2 4^== a-
      e=== ==== 2=== zy
      45== ===1 6=== and
      o4== 35G4 2=== i'm
      u=== ==== 6=== o-
      32== ===3 4^== ut
      e=== ==== 2=== of
      40== ===2 4=== my
      o2== ===3 2=== mind
      3Z== ==== 6.== ."""), 62.57, 68.21)
  ]),
  Section("mirrors", "C1A", [
    phrase("all-me", notes("""
      o444 21W2 4=L= cause
      1=== ==== 2=== A-
      b7== ===4 3=== A-
      3=== ==== 6=== ll
      44== ===2 2=== OF
      o7== ===4 5=== m-
      19== 1==1 2=== E
      2Z== ==== 4.== ."""), 68.21, 71.10),
    phrase("all-you", notes("""
      3444 21W3 4=L= loves
      12== ===2 2=== ALL
      40== 3=C4 6=== of
      o2== 2=W3 4=== y-
      14== ==== 2=== OU
      2Z== ==== 6.== ."""), 71.10, 74.68),
    phrase("CURVES", notes("""
      3444 21W2 2=L= LOVE
      e=== ==== 6=== you-
      o2== ===1 5=== r
      1=== ==== 3=== CURVES
      2=== ==== 5=== and
      3=== ==== 3=== ALL
      40== 3=C4 5=== your
      o2== 2=W1 4=== ed-
      10== 3=C4 3=== GES
      2Z== ==== 5.== ."""), 74.86, 78.86),
    lyrics("IMPERFECTIONS", "ALL you-r PER-fect IM-per-fec-TIONS", "CURVES", 78.86, 82.63)
  ]),
  Section("SEPULCHRE", "C1B", [
    phrase("GIVE-YOUR", notes("""
      3444 21W2 3=L= GIVE
      e=== ==== 5=== your
      1=== ==== 3=== A-
      b7== ===4 4=== LL
      44== ===2 7=== to
      o7== ===4 6=== m-
      19== 1==1 3=== E
      2Z== ==== 6.== ."""), 82.63, 86.35),
    phrase("give-my", notes("""
      u244 21W1 6=L= i'll
      39== 1=== 3=== GIVE
      e4== 2==2 5=== m-
      o2== ===1 4=== y
      1=== ==== 3=== ALL
      40== 3=C4 7=== to
      o2== 2=W1 6=== yo-
      14== ===2 3=== U
      2Z== ==== 5.== ."""), 86.35, 90.10),
    lyrics("END", "YOU'RE m-y END and MY be-gin-ING", "CURVES", 90.10, 94.17),
    lyrics("LOSE", "E-ve-n WHEN i LOSE i'm win-NING", "CURVES", 94.17, 97.70)
  ]),
  Section("ALTAR", "C1O", [
    phrase("I-GIVE", notes("""
      u444 21W2 6=L= CAUSE
      3=== ==== 7=== i
      e5== ===3 6=== give
      47== ===4 4=== you
      o0== 1==3 2=== A-
      uY== ===2 6=== u-
      p0== ===3 5=== i-
      3Y== ===2 4=== a-
      o9== ===1 2=== A-
      u7== 2==4 5=== LL
      3Z== ==== 7.== ,
      44== ===2 7=== of
      o=== ==== 4=== ME
      uZ== ==== 6.== ."""), 97.70, 105.29),
    lyrics("YOU-GIVE", "AND you give me A-u-i-a-A-LL of YOU", "I-GIVE", 105.29, 111.83),
    phrase("OO", notes("""
      4444 21W2 6=L= oh-
      o2== ===1 2=== O
      3Z== ==== 6.== ."""), 111.83, 115.05)
  ]),
  Section("BEDROOM", "V3", [
    phrase("TIMES", notes("""
      3244 21W1 2=L= HOW
      e4== ===2 4=== MA-
      42== ===1 6=== ni-
      m4== ===2 4=== y
      12== ===1 2=== T-
      a4== ===2 4=== IMES
      2=== ==== 6=== do
      u2== ===1 4=== i
      34== ===2 2=== HAVE
      e2== ===1 4=== TO
      40== 3=C4 6=== tell
      1=== ==== 2=== YOU?
      2Z== ==== 6.== ."""), 115.05, 118.98),
    phrase("CRYING", notes("""
      3444 21W2 2=L= E-
      e=== ==== 4=== ven
      4=== ==== 2=== WHEN
      o=== ==== 4=== you're
      15== ===3 2=== C-
      b7== ===4 4=== RY-
      25== ===3 6=== ing
      u4== ===2 4=== you're
      3=== ==== 2=== BEAU-
      e2== ===1 4=== TI-
      40== 1=C4 6=== ful
      o=== ==== 4=== T-
      19== ===2 6=== oo
      2Z== ==== 4.== ."""), 118.98, 122.55),
    phrase("beating", notes("""
      u044 31C4 6=L= the
      32== 2=W1 2=== W-
      c4== ===2 4=== ORLD
      t=== ==== 6=== is
      15== ===3 2=== BEAT-
      u4== ===2 6=== i-
      p5== ===3 4=== i-
      34== ===2 3=== ing
      e0== 3=C4 2=== YOU
      o4== 2=W2 6=== d-
      15== ===3 4=== own
      u4== ===2 2=== I-
      e0== 3=C4 4=== M
      4=== ==== 6=== a-
      o2== 2=W1 2=== ROUND
      2Z== ==== 6.== ."""), 122.55, 128.17),
    phrase("mood", notes("""
      u244 21W1 6=L= through
      34== ===2 2=== E-
      e2== ===1 4=== VE-
      4=== ==== 6=== ry
      o9== 3=C2 2=== MOOD
      2Z== ==== 6.== ."""), 128.17, 130.19)
  ]),
  Section("GARAGE", "V4", [
    phrase("DOWNFALL", notes("""
      p744 21W4 2=LM YOU'RE
      e4== ===2 4=== my
      o=== ==== 2=== DOWN-
      a0== 3=C4 6=== fall,
      37== 2=W= 2=== YOU'RE
      e4== ===2 4=== my
      o=== ==== 2=== MUSE
      aZ== ==== 6.== ."""), 130.19, 133.97),
    phrase("distraction", notes("""
      u044 31C4 6=L= my
      35== 2=W3 2=== W-
      e7== ===4 4=== ORST
      44== ===2 6=== dis-
      o=== ==== 2=== TRA-
      12== ===1 4=== AC-
      a=== ==== 6=== tion,
      u=== ==== 2=== MY
      34== ===2 4=== rhy-
      e2== ===1 2=== THM
      44== ===2 4=== n
      o9== 3=C2 2=== BLUES
      2Z== ==== 6.== ."""), 133.97, 137.69),
    phrase("singing", notes("""
      u444 21W2 6=L= i
      3=== ==== 4=== CAN'T
      t=== ==== 6=== stop
      15== ===3 2=== SI-
      u4== ===2 6=== ngi-
      30== 3=C4 4=== ING
      e=== ==== 6=== it's
      4Z== ==== 2.== ,
      o4== 2=W2 ==== RI-
      15== ===3 4=== I-
      u4== ===2 6=== ngi-
      30== 3=C4 4=== ING
      e=== ==== 6=== in
      4Z== ==== 2.== ."""), 137.69, 142.49),
    phrase("HEAD", notes("""
      o244 21W1 2=L= MY
      2Z== ==== 6.== ,
      u4== ===2 ==== h-
      e2== ===1 4=== ead
      4=== ==== 2=== FOR
      o4== ===2 6=== y-
      15== ===3 4=== ou
      4Z== ==== 2.== ."""), 142.49, 150.28)
  ]),
  Section("show", "B2", [
    repeat("underwater", 146.37, 150.29),
    repeat("BREATHIN", 150.29, 153.91),
    repeat("CRAZY", 153.91, 159.74)
  ]),
  Section("mirrors", "C2A", [
    repeat("all-me", 159.74, 162.63),
    repeat("all-you", 162.63, 166.38),
    repeat("CURVES", 166.38, 170.37),
    repeat("IMPERFECTIONS", 170.37, 175.05)
  ]),
  Section("SEPULCHRE", "C2B", [
    repeat("GIVE-YOUR", 175.05, 177.75),
    phrase("give-my^", notes("""
      u444 21W2 6=L= i'll
      30== 1==3 3=== GIVE
      eY== ===2 5=== m-
      o9== ===1 4=== y
      1=== ==== 3=== ALL
      47== 2==4 7=== to
      o4== ===2 3=== YOU
      2Z== ==== 5.== ."""), 177.75, 181.63),
    repeat("END", 181.63, 185.64),
    repeat("LOSE", 185.64, 189.20),
  ]),
  Section("ALTAR", "C2O", [
    repeat("I-GIVE", 189.20, 196.79),
    repeat("YOU-GIVE", 196.79, 204.06)
  ]),
  Section("CASINO", "M", [
    phrase("GIVE-ME", notes("""
      a544 21W3 3=LM GIVE
      27== ===4 5=== me
      uY== 1==2 3=== A-
      30== ===3 4=== LL
      eY== ===2 5=== of
      49== ===1 3=== YOU
      u7== 2==4 6=== o-
      p5== ===3 5=== u-
      34== ===2 3=== o-
      c2== ===1 3=== u-
      e0== 3=C4 2=== oh
      1Z== ==== 1.== ."""), 204.06, 207.59),
    phrase("CARDS", notes("""
      1944 11W2 3=L= CARDS
      u7== 2==1 5=== o-
      35== ===4 4=== n
      e=== ==== 3=== THE
      oY== 1==3 6=== t-
      10== ===4 4=== a-
      uY== ===3 2=== B-
      39== ===2 4=== LE
      e=== ==== 6=== w-
      47== 2==1 4=== e're
      o=== ==== 2=== BOTH
      u5== ===4 6=== sh-
      34== ===3 4=== o-
      e=== ==== 2=== W-
      42== ===2 4=== ING
      o=== ==== 6=== hearts
      eZ== ==== 2.== ."""), 207.59, 215.01),
    phrase("RISK", notes("""
      1944 11W1 2=LM RIS-
      u7== 2==4 6=== king
      35== ===3 5=== it
      o5== 1==2 2=== A-
      10== ===3 3=== LL
      uY== ===2 6=== th-
      39== ===1 5=== ough
      e=== ==== 2=== IT'S
      o7== 2==4 6=== hard
      3Z== ==== 2.== ."""), 215.01, 220.54)
  ]),
  Section("mirrors", "C3A", [
    repeat("all-me", 220.54, 223.52),
    repeat("all-you", 223.52, 227.34),
    repeat("CURVES", 227.34, 231.31),
    repeat("IMPERFECTIONS", 231.31, 235.15)
  ]),
  Section("SEPULCHRE", "C3B", [
    repeat("GIVE-YOUR", 235.15, 238.65),
    repeat("give-my^", 238.65, 242.60),
    repeat("END", 242.60, 246.55),
    repeat("LOSE", 246.55, 250.20)
  ]),
  Section("ALTAR", "C3O1", [
    repeat("I-GIVE", 250.20, 257.77),
    repeat("YOU-GIVE", 257.77, 265.26)
  ]),
  Section("altar", "C3O2", [
    phrase("i-give-auaua", notes("""
      3444 21W2 7=L= i
      e5== ===3 6=== give
      47== ===4 4=== you
      o0== 1==3 2=== A-
      22== ===4 4=== U-
      uY== ===2 6=== a-
      40== ===3 4=== u-
      o9== ===1 2=== A-
      u7== 2==4 5=== LL
      3Z== ==== 7.== ,
      44== ===2 ==== of
      o=== ==== 4=== ME
      3Z== ==== 6.== ."""), 265.26, 273.04),
    repeat("YOU-GIVE", 273.04, 279.42),
    phrase("ouo", notes("""
      4244 21W1 6=L= o-
      o4== ===2 5=== u-
      12== ===1 4=== oh
      4Z== ==== 1.== ."""), 279.42, 282.03)
  ])
], "63.all-of-me.mp3"))

