# vim: foldmethod=marker foldmarker=\ phrase(,) foldtext=getline(v\:foldstart)

import sys; sys.path.append("..")
from violin import *

process_piece(Piece("all-of-me", 4, 126, "48", [
  Section("art-desk", "V1", [
    phrase("mouth", parse_violin_notes("""
      3= 2 21W1 v2=LM what
      e= 4 ===2 v4=== would
      4= = ==== ^6=== i
      1= = ==== v2=== do
      a= = ==== ^4=== with
      2= 2 ===1 v2=== o
      u= 4 ===2 ^4=== -ut
      3= = ==== v2=== your
      4= 0 3=C4 ^6=== smart
      12 = ==== v26== mouth?"""), 23.51, 27.31),
    phrase("drawin", parse_violin_notes("""
      3= 2 21W1 v2=LM draw
      e= 4 ===2 v4=== -in
      4= = ==== ^6=== me
      1= = ==== v2=== in
      a= 2 ===1 v4=== a
      2= 4 ===2 ^6=== you
      3= = ==== v2=== kick
      e= 2 ===1 ^4=== -in
      4= 0 3=C4 v2=== me
      o= = ==== ^4=== a
      12 9 ===2 v26== -out"""), 27.31, 31.12),
    phrase("spinnin", parse_violin_notes("""
      u= 9 31C2 ^6=LM you've
      3= 4 2=W= v4=== got
      t= = ==== ^7=== my
      1= 5 ===3 v2=== head
      3= 4 ===2 v5=== spin
      e4 0 3=C4 ^7=== -nin,
      1= 5 2=W3 v2=== no
      3= 4 ===2 v5=== kid
      e4 0 3=C4 ^73== -din"""), 31.12, 35.85),
    phrase("pin", parse_violin_notes("""
      o= 0 31C4 ^3=LM i
      1u 2 2=W1 v2=== can't,
      3= 4 ===2 v5=== pin
      e= 2 ===1 ^7=== yo
      o= 9 3=C2 ^4=== -u
      1u = ==== v26== down"""),  35.85, 38.95)
  ]),
  Section("disneyland", "V2", [
    phrase("mind", parse_violin_notes("""
      3= 2 21W1 v2=LM what's
      e= 4 ===2 v4=== go
      4= = ==== ^6=== -in
      1= = ==== v2=== on
      a= 2 ===1 v4=== in
      2= 4 ===2 ^6=== that
      3= = ==== v2=== beau
      e= 2 ===1 v4=== ti
      4= 0 3=C4 ^6=== ful
      w2 = ==== v26== mind?"""), 38.95, 42.67),
    phrase("ride", parse_violin_notes("""
      3= 4 21W2 ^6=LM i'm
      e= = ==== v4=== on
      4= = ==== ^6=== your
      1= 7 ===4 v2=== ma
      a= 5 ===3 v4=== gi
      2= 4 ===2 ^6=== cal
      3= = ==== v2=== mys
      e= 2 ===1 v4=== te
      4= 0 3=C4 ^6=== ry
      o= = ==== v4=== r
      1u 9 ===2 ^62== -ide"""), 42.67, 46.57),
    phrase("dizzy", parse_violin_notes("""
      3= 4 21W2 v2=LM and
      e= = ==== ^6=== i'm
      1= 5 ===3 v2=== so
      3= 4 ===2 v5=== di
      e4 0 3=C4 ^7=== zzy,
      o= = ==== ^3=== don't
      1= 4 2=W2 v2=== kn
      b= 5 ===3 v3=== -ow
      2= = ==== ^6=== what
      3= 4 ===2 v4=== hit
      e4 0 3==4 ^63== me"""), 46.57, 51.03),
    phrase("alright", parse_violin_notes("""
      o= 0 31C4 ^3=LM but
      1= 2 2=W1 v2=== i'll
      3= 4 ===2 v5=== be
      e= 2 ===1 ^7=== al
      1e 5 ===3 v26== -right"""), 51.03, 54.92)
  ]),
  Section("show", "B1", [
    phrase("underwater", parse_violin_notes("""
      o= 0 33W3 ^6=LM my
      1= 7 2=G3 v2=== h
      b= 9 ===4 v4=== -ead's
      u= 7 ===3 ^6=== u
      3= 5 ===2 ^4=== -n
      e= = ==== v2=== de
      4= 4 ===1 v4=== -r
      o= = ==== ^6=== wa
      u= 2 3=W4 v2=== te
      3= 0 ===3 v4=== -r
      e4 = ===3 ^62== but"""), 54.92, 58.71),
    phrase("breathin", parse_violin_notes("""
      o= Y 33W2 v2=LM i'm
      u= 9 =1=2 ^6=== br
      3= 7 ===1 ^4=== -ea
      e= = ==== v2=== th
      4= 9 ===2 v4=== -in
      ou = ==== ^62== fine"""), 58.71, 62.57),
    phrase("crazy", parse_violin_notes("""
      o= 7 24P2 v2=LM y
      w= 9 ===3 v4=== -ou're
      u= = ==== ^6=== cr
      3= 7 ===2 ^4=== -a
      e= = ==== v2=== zy
      4= 5 ===1 ^6=== and
      o= 4 35G4 v2=== i'm
      u= = ==== ^6=== o
      3= 2 ===3 ^4=== -ut
      e= = ==== v2=== of
      4= 0 ===2 ^4=== my
      o3 2 ===3 v26== mind"""), 62.57, 68.21)
  ]),
  Section("church.mirrors", "CA1", [
    phrase("all-me", parse_violin_notes("""
      o= 4 21W2 ^4=LM cause
      1= = ==== v2=== a-
      b= 7 ===4 v3=== a-
      3= = ==== ^6=== ll
      4= 4 ===2 v2=== of
      o= 7 ===4 ^5=== m-
      12 9 1==1 v24== e"""), 68.21, 71.10),
    phrase("all-you", parse_violin_notes("""
      3= 4 21W3 ^4=LM loves
      1= 2 ===2 v2=== all
      4= 0 3=C4 ^6=== of
      o= 2 2=W3 ^4=== y-
      12 4 ==== v26== ou"""), 71.10, 74.68),
    phrase("curves", parse_violin_notes("""
      3= 4 21W2 v2=LM love
      e= = ==== ^6=== you-
      o= 2 ===1 ^5=== r
      1= = ==== v3=== curves
      2= = ==== ^5=== and
      3= = ==== v3=== all
      4= 0 3=C4 ^5=== your
      o= 2 2=W1 ^4=== ed-
      12 0 3=C4 v35== ges"""), 74.86, 78.86),
    lyrics("imperfections", "all you-r per-fect im-per-fec-tions", "curves", 78.86, 82.63)
  ]),
  Section("church.sepulchre", "CB1", [
    phrase("give-your", parse_violin_notes("""
      3= 4 21W2 v3=LM give
      e= = ==== ^5=== your
      1= = ==== v3=== a-
      b= 7 ===4 v4=== ll
      4= 4 ===2 ^7=== to
      o= 7 ===4 ^6=== m-
      12 9 1==1 v36== e"""), 82.63, 86.35),
    phrase("give-my", parse_violin_notes("""
      u= 2 21W1 ^6=LM i'll
      3= 9 1=== v3=== give
      e= 4 2==2 ^5=== m-
      o= 2 ===1 ^4=== y
      1= = ==== v3=== all
      4= 0 3=C4 ^7=== to
      o= 2 2=W1 ^6=== yo-
      12 4 ===2 v35== u"""), 86.35, 90.10),
    lyrics("end", "you're m-y end and my be-gin-ing", "curves", 90.10, 94.17),
    lyrics("lose", "e-ve-n when i lose i'm win-ning", "curves", 94.17, 97.70)
  ]),
  Section("altar", "O1", [
    phrase("i-give", parse_violin_notes("""
      u= 4 21W2 v6=LM cause
      3= = ==== ^7=== i
      e= 5 ===3 ^6=== give
      4= 7 ===4 ^4=== you
      o= 0 1==3 v2=== a-
      u= Y ===2 ^6=== u-
      p= 0 ===3 ^5=== i-
      3= Y ===2 ^4=== a-
      o= 9 ===1 v2=== a-
      u3 7 2==4 v5=== ll
      4= 4 ===2 ^7=== of
      ou = ==== v46== me"""), 97.70, 105.29),
    lyrics("you-give", "and you give me a-u-i-a-a-ll of you", "i-give", 105.29, 111.83),
    phrase("oo", parse_violin_notes("""
      4= 4 21W2 v6=LM oh-
      o3 2 ===1 ^26== -o"""), 111.83, 115.05)
  ]),
  Section("bedroom", "V3", [
    phrase("times", parse_violin_notes("""
      3= 2 21W1 v2=LM how
      e= 4 ===2 v4=== ma-
      4= 2 ===1 ^6=== -ni-
      m= 4 ===2 ^4=== -y
      1= 2 ===1 v2=== t-
      a= 4 ===2 v4=== imes
      2= = ==== ^6=== do
      u= 2 ===1 ^4=== i
      3= 4 ===2 v2=== have
      e= 2 ===1 v4=== to
      4= 0 3=C4 ^6=== tell
      12 = ==== v26== you?"""), 115.05, 118.98),
    phrase("crying", parse_violin_notes("""
      3= 4 21W2 v2=LM e-
      e= = ==== ^4=== ven
      4= = ==== v2=== when
      o= = ==== ^4=== you're
      1= 5 ===3 v2=== c-
      b= 7 ===4 v4=== -ry-
      2= 5 ===3 ^6=== -ing
      u= 4 ===2 ^4=== you're
      3= = ==== v2=== beau-
      e= 2 ===1 v4=== ti-
      4= 0 1=C4 ^6=== -ful
      o= = ==== v4=== t-
      12 9 ===2 ^64== -oo"""), 118.98, 122.55),
    phrase("beating", parse_violin_notes("""
      u= 0 31C4 ^6=LM the
      3= 2 2=W1 v2=== w-
      c= 4 ===2 v4=== -orld
      t= = ==== ^6=== is
      1= 5 ===3 v2=== beat-
      u= 4 ===2 ^6=== -i-
      p= 5 ===3 ^4=== -i-
      3= 4 ===2 ^3=== -ing
      e= 0 3=C4 v2=== you
      o= 4 2=W2 ^6=== d-
      1= 5 ===3 ^4=== -own
      u= 4 ===2 v2=== i-
      e= 0 3=C4 v4=== -m
      4= = ==== ^6=== a-
      o2 2 2=W1 v26== -round"""), 122.55, 128.17),
    phrase("mood", parse_violin_notes("""
      u= 2 21W1 ^6=LM through
      3= 4 ===2 v2=== e-
      e= 2 ===1 v4=== -ve-
      4= = ==== ^6=== -ry
      o2 9 3=C2 v26== mood"""), 128.17, 130.19)
  ]),
  Section("garage", "V4", [
    phrase("downfall", parse_violin_notes("""
      p= 7 21W4 v2=LM you're
      e= 4 ===2 ^4=== my
      o= = ==== v2=== down-
      a= 0 3=C4 ^6=== fall,
      3= 7 2=W= v2=== you're
      e= 4 ===2 ^4=== my
      oa = ==== v26== muse"""), 130.19, 133.97),
    phrase("distraction", parse_violin_notes("""
      u= 0 31C4 ^6=LM my
      3= 5 2=W3 v2=== w-
      e= 7 ===4 v4=== orst
      4= 4 ===2 ^6=== dis-
      o= = ==== v2=== tra-
      1= 2 ===1 v4=== ac-
      a= = ==== ^6=== tion,
      u= = ==== v2=== my
      3= 4 ===2 ^4=== rhy-
      e= 2 ===1 v2=== thm
      4= 4 ===2 ^4=== n
      o2 9 3=C2 v26== blues"""), 133.97, 137.69),
    phrase("singing", parse_violin_notes("""
      u= 4 21W2 ^6=LM i
      3= = ==== v4=== can't
      t= = ==== ^6=== stop
      1= 5 ===3 v2=== si-
      u= 4 ===2 ^6=== ngi-
      3= 0 3=C4 v4=== ing
      e4 = ==== ^6=== it's,
      o= 4 2=W2 v2=== ri-
      1= 5 ===3 v4=== -i-
      u= 4 ===2 ^6=== ngi-
      3= 0 3=C4 v4=== ing
      e4 = ==== ^62== in"""), 137.69, 142.49),
    phrase("head", parse_violin_notes("""
      o2 2 21W1 v2=LM my,
      u= 4 ===2 ^6=== h-
      e= 2 ===1 ^4=== -ead
      4= = ==== v2=== for
      o= 4 ===2 ^6=== y-
      14 5 ===3 ^42== -ou"""), 142.49, 150.28)
  ]),
  Section("show", "B2", [
    repeat("underwater", 146.37, 150.29),
    repeat("breathin", 150.29, 153.91),
    repeat("crazy", 153.91, 159.74)
  ]),
  Section("church.mirrors", "CA2", [
    repeat("all-me", 159.74, 162.63),
    repeat("all-you", 162.63, 166.38),
    repeat("curves", 166.38, 170.37),
    repeat("imperfections", 170.37, 175.05)
  ]),
  Section("church.sepulchre", "CB2", [
    repeat("give-your", 175.05, 177.75),
    repeat("give-my", 177.75, 181.63),
    repeat("end", 181.63, 185.64),
    repeat("lose", 185.64, 189.20),
  ]),
  Section("altar", "O2", [
    repeat("i-give", 189.20, 196.79),
    repeat("you-give", 196.79, 204.06)
  ]),
  Section("casino", "M", [
    phrase("give-me", parse_violin_notes("""
      a= 5 21W3 v3=LM give
      2= 7 ===4 ^5=== me
      u= Y 1==2 v3=== a-
      3= 0 ===3 v4=== ll
      e= Y ===2 ^5=== of
      4= 9 ===1 v3=== you
      u= 7 2==4 ^6=== o-
      p= 5 ===3 ^5=== u-
      3= 4 ===2 ^3=== o-
      c= 2 ===1 ^3=== u-
      e1 0 3=C4 ^21== oh"""), 204.06, 207.59),
    phrase("cards", parse_violin_notes("""
      1= 9 11W2 v3=LM cards
      u= 7 2==1 ^5=== o-
      3= 5 ===4 ^4=== n
      e= = ==== v3=== the
      o= Y 1==3 ^6=== t-
      1= 0 ===4 ^4=== a-
      u= Y ===3 v2=== b-
      3= 9 ===2 v4=== le
      e= = ==== ^6=== w-
      4= 7 2==1 ^4=== e're
      o= = ==== v2=== both
      u= 5 ===4 ^6=== sh-
      3= 4 ===3 ^4=== o-
      e= = ==== v2=== w-
      4= 2 ===2 v4=== ing
      oe = ==== ^62== hearts"""), 207.59, 215.01),
    phrase("risk", parse_violin_notes("""
      1= 9 11W1 v2=LM ris-
      u= 7 2==4 ^6=== king
      3= 5 ===3 ^5=== it
      o= 5 1==2 v2=== a-
      1= 0 ===3 v3=== ll
      u= Y ===2 ^6=== th-
      3= 9 ===1 ^5=== ough
      e= = ==== v2=== it's
      o3 7 2==4 ^62== hard"""), 215.01, 220.54)
  ]),
  Section("church.mirrors", "CA3", [
    repeat("all-me", 220.54, 223.52),
    repeat("all-you", 223.52, 227.34),
    repeat("curves", 227.34, 231.31),
    repeat("imperfections", 231.31, 235.15)
  ]),
  Section("church.sepulchre", "CB3", [
    repeat("give-your", 235.15, 238.65),
    phrase("give-my^", parse_violin_notes("""
      u= 4 21W2 ^6=LM i'll
      3= 0 1==3 v3=== give
      e= Y ===2 ^5=== m-
      o= 9 ===1 ^4=== y
      1= = ==== v3=== all
      4= 7 2==4 ^7=== to
      o2 4 ===2 v35== you"""), 238.65, 242.60),
    repeat("end", 242.60, 246.55),
    repeat("lose", 246.55, 250.20)
  ]),
  Section("altar", "O3", [
    repeat("i-give", 250.20, 257.77),
    repeat("you-give", 257.77, 265.26)
  ]),
  Section("altar", "O4", [
    phrase("i-give-auaua", parse_violin_notes("""
      3= 4 21W2 ^7=LM i
      e= 5 ===3 ^6=== give
      4= 7 ===4 ^4=== you
      o= 0 1==3 v2=== a-
      2= 2 ===4 v4=== u-
      u= Y ===2 ^6=== a-
      4= 0 ===3 ^4=== u-
      o= 9 ===1 v2=== a-
      u3 7 2==4 v5=== ll
      4= 4 ===2 ^7=== of
      o3 = ==== v46== me"""), 265.26, 273.04),
    repeat("you-give", 273.04, 279.42),
    phrase("ouo", parse_violin_notes("""
      4= 2 21W1 ^6=LM o-
      o= 4 ===2 ^5=== u-
      14 2 ===1 ^41== oh"""), 279.42, 282.03)
  ])
], "63.all-of-me.mp3"))

