# vim: foldmethod=marker foldmarker=\ phrase(,) foldtext=getline(v\:foldstart)

import sys; sys.path.append("..")
from violin import *

process_piece(Piece("all-of-me", 4, 126, "48", [
  Section("art-desk", "V1", [
    phrase("mouth", notes("""
      324= 21W1 2L= what
      e4== ===2 ^== would
      4=== ==== 6== i
      1=== ==== 2== do
      a=== ==== 4== with-
      22== ===1 2== o-
      u4== ===2 4== ut
      3=== ==== 2=~ your
      40== 3=C4 6=~ smart
      1=== ==== 2=~ mouth?
      2Z== ==== 6== ."""), 23.51, 27.31),
    phrase("drawin", notes("""
      324= 21W1 2L= draw-
      e4== ===2 v== in
      4=== ==== 6== me
      1=== ==== 2== in
      a2== ===1 v== a
      24== ===2 6== you
      3=== ==== 2== kick-
      e2== ===1 4== in
      40== 3=C4 2== me
      o=== ==== 4== a-
      19== ===2 2== out
      2Z== ==== 6== ."""), 27.31, 31.12),
    phrase("spinnin", notes("""
      u94= 31C2 6L= you've
      34== 2=W= 4== got
      t=== ==== 7== my
      15== ===3 2== head
      34== ===2 v== spin-
      e0== 3=C4 7== nin
      4Z== ==== 2== ,
      15== 2=W3 2== no
      34== ===2 v== kid-
      e0== 3=C4 7== din
      4Z== ==== 3== ."""), 31.12, 35.85),
    phrase("pin", notes("""
      o04= 31C4 3L= i
      12== 2=W1 2== can't
      uZ== ==== 5== ,
      34== ===2 v== pin
      e2== ===1 7== yo-
      o9== 3=C2 ^== u
      1=== ==== 2== down
      uZ== ==== 6== ."""),  35.85, 38.95)
  ]),
  Section("disneyland", "V2", [
    phrase("mind", notes("""
      324= 21W1 2L= what's
      e4== ===2 v== go-
      4=== ==== 6== in
      1=== ==== 2== on
      a2== ===1 v== in
      24== ===2 6== that
      3=== ==== 2== beau-
      e2== ===1 v== ti-
      40== 3=C4 6== ful
      w=== ==== 2== mind
      2Z== ==== 6== ?"""), 38.95, 42.67),
    phrase("ride", notes("""
      344= 21W2 6L= i'm
      e=== ==== 4== on
      4=== ==== 6== your
      17== ===4 2== ma-
      a5== ===3 v== gi-
      24== ===2 6== cal
      3=== ==== 2== mys-
      e2== ===1 v== te-
      40== 3=C4 6== ry-
      o=== ==== 4== r-
      19== ===2 6== ide
      uZ== ==== 2== ."""), 42.67, 46.57),
    phrase("dizzy", notes("""
      344= 21W2 2L= and
      e=== ==== 6== i'm
      15== ===3 2== so
      34== ===2 v== di-
      e0== 3=C4 7== zzy
      4Z== ==== 3== ,
      o=== ==== ^== don't
      14== 2=W2 2== kn-
      b5== ===3 v== ow
      2=== ==== 6== what
      34== ===2 4== hit
      e0== 3==4 6== me
      4Z== ==== 3== ."""), 46.57, 51.03),
    phrase("alright", notes("""
      o04= 31C4 3L= but
      12== 2=W1 2== i'll
      34== ===2 5== be
      e2== ===1 7== al-
      15== ===3 2== right
      eZ== ==== 6== ."""), 51.03, 54.92)
  ]),
  Section("show", "B1", [
    phrase("underwater", notes("""
      o04= 33W3 6L= my
      17== 2=G3 2== h-
      b9== ===4 v== ead's
      u7== ===3 6== u-
      35== ===2 ^== n-
      e=== ==== 2== de-
      44== ===1 v== r
      o=== ==== 6== wa-
      u2== 3=W4 2== te-
      30== ===3 v== r
      e=== ===3 6== but
      4Z== ==== 2== ."""), 54.92, 58.71),
    phrase("breathin", notes("""
      oY4= 33W2 2L= i'm
      u9== =1=2 6== br-
      37== ===1 ^== ea-
      e=== ==== 2== th-
      49== ===2 v== in
      o=== ==== 6== fine
      uZ== ==== 2== ."""), 58.71, 62.57),
    phrase("crazy", notes("""
      o74= 24P2 2L= y-
      w9== ===3 v== ou're
      u=== ==== 6== cr-
      37== ===2 ^== a-
      e=== ==== 2== zy
      45== ===1 6== and
      o4== 35G4 2== i'm
      u=== ==== 6== o-
      32== ===3 ^== ut
      e=== ==== 2== of
      40== ===2 4== my
      o2== ===3 2== mind
      3Z== ==== 6== ."""), 62.57, 68.21)
  ]),
  Section("mirrors", "C1A", [
    phrase("all-me", notes("""
      o44= 21W2 4L= cause
      1=== ==== 2== a-
      b7== ===4 v== a-
      3=== ==== 6== ll
      44== ===2 2== of
      o7== ===4 5== m-
      19== 1==1 2== e
      2Z== ==== 4== ."""), 68.21, 71.10),
    phrase("all-you", notes("""
      344= 21W3 4L= loves
      12== ===2 2== all
      40== 3=C4 6== of
      o2== 2=W3 4== y-
      14== ==== 2== ou
      2Z== ==== 6== ."""), 71.10, 74.68),
    phrase("curves", notes("""
      344= 21W2 2L= love
      e=== ==== 6== you-
      o2== ===1 ^== r
      1=== ==== 3== curves
      2=== ==== 5== and
      3=== ==== 3== all
      40== 3=C4 5== your
      o2== 2=W1 ^== ed-
      10== 3=C4 3== ges
      2Z== ==== 5== ."""), 74.86, 78.86),
    lyrics("imperfections", "all you-r per-fect im-per-fec-tions", "curves", 78.86, 82.63)
  ]),
  Section("sepulchre", "C1B", [
    phrase("give-your", notes("""
      344= 21W2 3L= give
      e=== ==== 5== your
      1=== ==== 3== a-
      b7== ===4 v== ll
      44== ===2 7== to
      o7== ===4 ^== m-
      19== 1==1 3== e
      2Z== ==== 6== ."""), 82.63, 86.35),
    phrase("give-my", notes("""
      u24= 21W1 6L= i'll
      39== 1=== 3== give
      e4== 2==2 5== m-
      o2== ===1 ^== y
      1=== ==== 3== all
      40== 3=C4 7== to
      o2== 2=W1 ^== yo-
      14== ===2 3== u
      2Z== ==== 5== ."""), 86.35, 90.10),
    lyrics("end", "you're m-y end and my be-gin-ing", "curves", 90.10, 94.17),
    lyrics("lose", "e-ve-n when i lose i'm win-ning", "curves", 94.17, 97.70)
  ]),
  Section("altar", "C1O", [
    phrase("i-give", notes("""
      u44= 21W2 6L= cause
      3=== ==== 7== i
      e5== ===3 ^== give
      47== ===4 ^== you
      o0== 1==3 2== a-
      uY== ===2 6== u-
      p0== ===3 ^== i-
      3Y== ===2 ^== a-
      o9== ===1 2== a-
      u7== 2==4 v== ll
      3Z== ==== 7== ,
      44== ===2 7== of
      o=== ==== 4== me
      uZ== ==== 6== ."""), 97.70, 105.29),
    lyrics("you-give", "and you give me a-u-i-a-a-ll of you", "i-give", 105.29, 111.83),
    phrase("oo", notes("""
      444= 21W2 6L= oh-
      o2== ===1 2== o
      3Z== ==== 6== ."""), 111.83, 115.05)
  ]),
  Section("bedroom", "V3", [
    phrase("times", notes("""
      324= 21W1 2L= how
      e4== ===2 v== ma-
      42== ===1 6== ni-
      m4== ===2 ^== y
      12== ===1 2== t-
      a4== ===2 v== imes
      2=== ==== 6== do
      u2== ===1 ^== i
      34== ===2 2== have
      e2== ===1 v== to
      40== 3=C4 6== tell
      1=== ==== 2== you?
      2Z== ==== 6== ."""), 115.05, 118.98),
    phrase("crying", notes("""
      344= 21W2 2L= e-
      e=== ==== 4== ven
      4=== ==== 2== when
      o=== ==== 4== you're
      15== ===3 2== c-
      b7== ===4 v== ry-
      25== ===3 6== ing
      u4== ===2 ^== you're
      3=== ==== 2== beau-
      e2== ===1 v== ti-
      40== 1=C4 6== ful
      o=== ==== 4== t-
      19== ===2 6== oo
      2Z== ==== 4== ."""), 118.98, 122.55),
    phrase("beating", notes("""
      u04= 31C4 6L= the
      32== 2=W1 2== w-
      c4== ===2 v== orld
      t=== ==== 6== is
      15== ===3 2== beat-
      u4== ===2 6== i-
      p5== ===3 ^== i-
      34== ===2 ^== ing
      e0== 3=C4 2== you
      o4== 2=W2 6== d-
      15== ===3 ^== own
      u4== ===2 2== i-
      e0== 3=C4 v== m
      4=== ==== 6== a-
      o2== 2=W1 2== round
      2Z== ==== 6== ."""), 122.55, 128.17),
    phrase("mood", notes("""
      u24= 21W1 6L= through
      34== ===2 2== e-
      e2== ===1 v== ve-
      4=== ==== 6== ry
      o9== 3=C2 2== mood
      2Z== ==== 6== ."""), 128.17, 130.19)
  ]),
  Section("garage", "V4", [
    phrase("downfall", notes("""
      p74= 21W4 2L= you're
      e4== ===2 4== my
      o=== ==== 2== down-
      a0== 3=C4 6== fall,
      37== 2=W= 2== you're
      e4== ===2 4== my
      o=== ==== 2== muse
      aZ== ==== 6== ."""), 130.19, 133.97),
    phrase("distraction", notes("""
      u04= 31C4 6L= my
      35== 2=W3 2== w-
      e7== ===4 v== orst
      44== ===2 6== dis-
      o=== ==== 2== tra-
      12== ===1 v== ac-
      a=== ==== 6== tion,
      u=== ==== 2== my
      34== ===2 4== rhy-
      e2== ===1 2== thm
      44== ===2 4== n
      o9== 3=C2 2== blues
      2Z== ==== 6== ."""), 133.97, 137.69),
    phrase("singing", notes("""
      u44= 21W2 6l= i
      3=== ==== 4== can't
      t=== ==== 6== stop
      15== ===3 2== si-
      u4== ===2 6== ngi-
      30== 3=C4 4== ing
      e=== ==== 6== it's
      4Z== ==== 2== ,
      o4== 2=W2 2== ri-
      15== ===3 v== i-
      u4== ===2 6== ngi-
      30== 3=C4 4== ing
      e=== ==== 6== in
      4Z== ==== 2== ."""), 137.69, 142.49),
    phrase("head", notes("""
      o24= 21W1 2l= my
      2Z== ==== 6== ,
      u4== ===2 6== h-
      e2== ===1 ^== ead
      4=== ==== 2== for
      o4== ===2 6== y-
      15== ===3 ^== ou
      4Z== ==== 2== ."""), 142.49, 150.28)
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
      u44= 21W2 6L= i'll
      30== 1==3 3== give
      eY== ===2 5== m-
      o9== ===1 ^== y
      1=== ==== 3== all
      47== 2==4 7== to
      o4== ===2 3== you
      2Z== ==== 5== ."""), 177.75, 181.63),
    repeat("end", 181.63, 185.64),
    repeat("lose", 185.64, 189.20),
  ]),
  Section("altar", "C2O", [
    repeat("i-give", 189.20, 196.79),
    repeat("you-give", 196.79, 204.06)
  ]),
  Section("casino", "M", [
    phrase("give-me", notes("""
      a54= 21W3 3L= give
      27== ===4 5== me
      uY== 1==2 3== a-
      30== ===3 v== ll
      eY== ===2 5== of
      49== ===1 3== you
      u7== 2==4 6== o-
      p5== ===3 ^== u-
      34== ===2 ^== o-
      c2== ===1 ^== u-
      e0== 3=C4 ^== oh
      1Z== ==== 1== ."""), 204.06, 207.59),
    phrase("cards", notes("""
      194= 11W2 3L= cards
      u7== 2==1 5== o-
      35== ===4 ^== n
      e=== ==== 3== the
      oY== 1==3 6== t-
      10== ===4 ^== a-
      uY== ===3 2== b-
      39== ===2 v== le
      e=== ==== 6== w-
      47== 2==1 ^== e're
      o=== ==== 2== both
      u5== ===4 6== sh-
      34== ===3 ^== o-
      e=== ==== 2== w-
      42== ===2 v== ing
      o=== ==== 6== hearts
      eZ== ==== 2== ."""), 207.59, 215.01),
    phrase("risk", notes("""
      194= 11W1 2L= RIS-
      u7== 2==4 6== king
      35== ===3 ^== it
      o5== 1==2 2== A-
      10== ===3 v== LL
      uY== ===2 6== th-
      39== ===1 ^== ough
      e=== ==== 2== IT'S
      o7== 2==4 6== hard
      3Z== ==== 2== ."""), 215.01, 220.54)
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
      344= 21W2 7L= i
      e5== ===3 ^== give
      47== ===4 ^== you
      o0== 1==3 2== a-
      22== ===4 v== u-
      uY== ===2 6== a-
      40== ===3 ^== u-
      o9== ===1 2== a-
      u7== 2==4 v== ll
      3Z== ==== 7== ,
      44== ===2 7== of
      o=== ==== 4== me
      3Z== ==== 6== ."""), 265.26, 273.04),
    repeat("you-give", 273.04, 279.42),
    phrase("ouo", notes("""
      424= 21W1 6L= o-
      o4== ===2 ^== u-
      12== ===1 ^== oh
      4Z== ==== 1== ."""), 279.42, 282.03)
  ])
], "63.all-of-me.mp3"))

