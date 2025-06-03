# vim: foldmethod=marker foldmarker=\ phrase(,) foldtext=getline(v\:foldstart)

import sys; sys.path.append("..")
from violin import *

process_piece(Piece("all-of-me", 4, 126, "48", [
  Section("Art-desk", "V1", [
    phrase("Mouth", notes("""
      3= 2 21W1 v2=LM What
      e= 4 ===2 v4=== Would
      4= = ==== ^6=== i
      1= = ==== v2=== Do
      a= = ==== ^4=== with-
      2= 2 ===1 v2=== O-
      u= 4 ===2 ^4=== ut
      3= = ==== v2=== Your
      4= 0 3=C4 ^6=== smart
      12 = ==== v26== Mouth?"""), 23.51, 27.31),
    phrase("Drawin", notes("""
      3= 2 21W1 v2=LM Draw-
      e= 4 ===2 v4=== In
      4= = ==== ^6=== me
      1= = ==== v2=== In
      a= 2 ===1 v4=== A
      2= 4 ===2 ^6=== you
      3= = ==== v2=== Kick-
      e= 2 ===1 ^4=== in
      4= 0 3=C4 v2=== Me
      o= = ==== ^4=== a-
      12 9 ===2 v26== Out"""), 27.31, 31.12),
    phrase("spinnin", notes("""
      u= 9 31C2 ^6=LM you've
      3= 4 2=W= v4=== Got
      t= = ==== ^7=== my
      1= 5 ===3 v2=== Head
      3= 4 ===2 v5=== Spin-
      e4 0 3=C4 ^7=== nin,
      1= 5 2=W3 v2=== No
      3= 4 ===2 v5=== Kid-
      e4 0 3=C4 ^73== din"""), 31.12, 35.85),
    phrase("pin", notes("""
      o= 0 31C4 ^3=LM i
      1u 2 2=W1 v2=== Can't,
      3= 4 ===2 v5=== Pin
      e= 2 ===1 ^7=== yo-
      o= 9 3=C2 ^4=== u
      1u = ==== v26== Down"""),  35.85, 38.95)
  ]),
  Section("Disneyland", "V2", [
    phrase("Mind", notes("""
      3= 2 21W1 v2=LM What's
      e= 4 ===2 v4=== Go-
      4= = ==== ^6=== in
      1= = ==== v2=== On
      a= 2 ===1 v4=== In
      2= 4 ===2 ^6=== that
      3= = ==== v2=== Beau-
      e= 2 ===1 v4=== Ti-
      4= 0 3=C4 ^6=== ful
      w2 = ==== v26== Mind?"""), 38.95, 42.67),
    phrase("ride", notes("""
      3= 4 21W2 ^6=LM i'm
      e= = ==== v4=== On
      4= = ==== ^6=== your
      1= 7 ===4 v2=== Ma-
      a= 5 ===3 v4=== Gi-
      2= 4 ===2 ^6=== cal
      3= = ==== v2=== Mys-
      e= 2 ===1 v4=== Te-
      4= 0 3=C4 ^6=== ry-
      o= = ==== v4=== R-
      1u 9 ===2 ^62== ide"""), 42.67, 46.57),
    phrase("Dizzy", notes("""
      3= 4 21W2 v2=LM And
      e= = ==== ^6=== i'm
      1= 5 ===3 v2=== So
      3= 4 ===2 v5=== Di-
      e4 0 3=C4 ^7=== zzy,
      o= = ==== ^3=== don't
      1= 4 2=W2 v2=== Kn-
      b= 5 ===3 v3=== Ow
      2= = ==== ^6=== what
      3= 4 ===2 v4=== Hit
      e4 0 3==4 ^63== me"""), 46.57, 51.03),
    phrase("alright", notes("""
      o= 0 31C4 ^3=LM but
      1= 2 2=W1 v2=== I'll
      3= 4 ===2 v5=== Be
      e= 2 ===1 ^7=== al-
      1e 5 ===3 v26== Right"""), 51.03, 54.92)
  ]),
  Section("show", "B1", [
    phrase("underwater", notes("""
      o= 0 33W3 ^6=LM my
      1= 7 2=G3 v2=== H-
      b= 9 ===4 v4=== Ead's
      u= 7 ===3 ^6=== u-
      3= 5 ===2 ^4=== n-
      e= = ==== v2=== De-
      4= 4 ===1 v4=== R
      o= = ==== ^6=== wa-
      u= 2 3=W4 v2=== Te-
      3= 0 ===3 v4=== R
      e4 = ===3 ^62== but"""), 54.92, 58.71),
    phrase("Breathin", notes("""
      o= Y 33W2 v2=LM I'm
      u= 9 =1=2 ^6=== br-
      3= 7 ===1 ^4=== ea-
      e= = ==== v2=== Th-
      4= 9 ===2 v4=== In
      ou = ==== ^62== fine"""), 58.71, 62.57),
    phrase("Crazy", notes("""
      o= 7 24P2 v2=LM Y-
      w= 9 ===3 v4=== Ou're
      u= = ==== ^6=== cr-
      3= 7 ===2 ^4=== a-
      e= = ==== v2=== Zy
      4= 5 ===1 ^6=== and
      o= 4 35G4 v2=== I'm
      u= = ==== ^6=== o-
      3= 2 ===3 ^4=== ut
      e= = ==== v2=== Of
      4= 0 ===2 ^4=== my
      o3 2 ===3 v26== Mind"""), 62.57, 68.21)
  ]),
  Section("mirrors", "C1A", [
    phrase("all-me", notes("""
      o= 4 21W2 ^4=LM cause
      1= = ==== v2=== A-
      b= 7 ===4 v3=== A-
      3= = ==== ^6=== ll
      4= 4 ===2 v2=== Of
      o= 7 ===4 ^5=== m-
      12 9 1==1 v24== E"""), 68.21, 71.10),
    phrase("all-you", notes("""
      3= 4 21W3 ^4=LM loves
      1= 2 ===2 v2=== All
      4= 0 3=C4 ^6=== of
      o= 2 2=W3 ^4=== y-
      12 4 ==== v26== Ou"""), 71.10, 74.68),
    phrase("Curves", notes("""
      3= 4 21W2 v2=LM Love
      e= = ==== ^6=== you-
      o= 2 ===1 ^5=== r
      1= = ==== v3=== Curves
      2= = ==== ^5=== and
      3= = ==== v3=== All
      4= 0 3=C4 ^5=== your
      o= 2 2=W1 ^4=== ed-
      12 0 3=C4 v35== Ges"""), 74.86, 78.86),
    lyrics("Imperfections", "All you-r Per-fect Im-per-fec-Tions", "Curves", 78.86, 82.63)
  ]),
  Section("Sepulchre", "C1B", [
    phrase("Give-your", notes("""
      3= 4 21W2 v3=LM Give
      e= = ==== ^5=== your
      1= = ==== v3=== A-
      b= 7 ===4 v4=== Ll
      4= 4 ===2 ^7=== to
      o= 7 ===4 ^6=== m-
      12 9 1==1 v36== E"""), 82.63, 86.35),
    phrase("give-my", notes("""
      u= 2 21W1 ^6=LM i'll
      3= 9 1=== v3=== Give
      e= 4 2==2 ^5=== m-
      o= 2 ===1 ^4=== y
      1= = ==== v3=== All
      4= 0 3=C4 ^7=== to
      o= 2 2=W1 ^6=== yo-
      12 4 ===2 v35== U"""), 86.35, 90.10),
    lyrics("End", "You're m-y End and My be-gin-Ing", "Curves", 90.10, 94.17),
    lyrics("Lose", "E-ve-n When i Lose i'm win-Ning", "Curves", 94.17, 97.70)
  ]),
  Section("Altar", "C1O", [
    phrase("I-give", notes("""
      u= 4 21W2 v6=LM Cause
      3= = ==== ^7=== i
      e= 5 ===3 ^6=== give
      4= 7 ===4 ^4=== you
      o= 0 1==3 v2=== A-
      u= Y ===2 ^6=== u-
      p= 0 ===3 ^5=== i-
      3= Y ===2 ^4=== a-
      o= 9 ===1 v2=== A-
      u3 7 2==4 v5=== Ll
      4= 4 ===2 ^7=== of
      ou = ==== v46== Me"""), 97.70, 105.29),
    lyrics("You-give", "And you give me A-u-i-a-A-Ll of You", "I-give", 105.29, 111.83),
    phrase("Oo", notes("""
      4= 4 21W2 ^6=LM oh-
      o3 2 ===1 v26== O"""), 111.83, 115.05)
  ]),
  Section("Bedroom", "V3", [
    phrase("Times", notes("""
      3= 2 21W1 v2=LM How
      e= 4 ===2 v4=== Ma-
      4= 2 ===1 ^6=== ni-
      m= 4 ===2 ^4=== y
      1= 2 ===1 v2=== T-
      a= 4 ===2 v4=== Imes
      2= = ==== ^6=== do
      u= 2 ===1 ^4=== i
      3= 4 ===2 v2=== Have
      e= 2 ===1 v4=== To
      4= 0 3=C4 ^6=== tell
      12 = ==== v26== You?"""), 115.05, 118.98),
    phrase("Crying", notes("""
      3= 4 21W2 v2=LM E-
      e= = ==== ^4=== ven
      4= = ==== v2=== When
      o= = ==== ^4=== you're
      1= 5 ===3 v2=== C-
      b= 7 ===4 v4=== Ry-
      2= 5 ===3 ^6=== ing
      u= 4 ===2 ^4=== you're
      3= = ==== v2=== Beau-
      e= 2 ===1 v4=== Ti-
      4= 0 1=C4 ^6=== ful
      o= = ==== v4=== T-
      12 9 ===2 ^64== oo"""), 118.98, 122.55),
    phrase("beating", notes("""
      u= 0 31C4 ^6=LM the
      3= 2 2=W1 v2=== W-
      c= 4 ===2 v4=== Orld
      t= = ==== ^6=== is
      1= 5 ===3 v2=== Beat-
      u= 4 ===2 ^6=== i-
      p= 5 ===3 ^4=== i-
      3= 4 ===2 ^3=== ing
      e= 0 3=C4 v2=== You
      o= 4 2=W2 ^6=== d-
      1= 5 ===3 ^4=== own
      u= 4 ===2 v2=== I-
      e= 0 3=C4 v4=== M
      4= = ==== ^6=== a-
      o2 2 2=W1 v26== Round"""), 122.55, 128.17),
    phrase("mood", notes("""
      u= 2 21W1 ^6=LM through
      3= 4 ===2 v2=== E-
      e= 2 ===1 v4=== Ve-
      4= = ==== ^6=== ry
      o2 9 3=C2 v26== Mood"""), 128.17, 130.19)
  ]),
  Section("Garage", "V4", [
    phrase("Downfall", notes("""
      p= 7 21W4 v2=LM You're
      e= 4 ===2 ^4=== my
      o= = ==== v2=== Down-
      a= 0 3=C4 ^6=== fall,
      3= 7 2=W= v2=== You're
      e= 4 ===2 ^4=== my
      oa = ==== v26== Muse"""), 130.19, 133.97),
    phrase("distraction", notes("""
      u= 0 31C4 ^6=LM my
      3= 5 2=W3 v2=== W-
      e= 7 ===4 v4=== Orst
      4= 4 ===2 ^6=== dis-
      o= = ==== v2=== Tra-
      1= 2 ===1 v4=== Ac-
      a= = ==== ^6=== tion,
      u= = ==== v2=== My
      3= 4 ===2 ^4=== rhy-
      e= 2 ===1 v2=== Thm
      4= 4 ===2 ^4=== n
      o2 9 3=C2 v26== Blues"""), 133.97, 137.69),
    phrase("singing", notes("""
      u= 4 21W2 ^6=LM i
      3= = ==== v4=== Can't
      t= = ==== ^6=== stop
      1= 5 ===3 v2=== Si-
      u= 4 ===2 ^6=== ngi-
      3= 0 3=C4 v4=== Ing
      e4 = ==== ^6=== it's,
      o= 4 2=W2 v2=== Ri-
      1= 5 ===3 v4=== I-
      u= 4 ===2 ^6=== ngi-
      3= 0 3=C4 v4=== Ing
      e4 = ==== ^62== in"""), 137.69, 142.49),
    phrase("Head", notes("""
      o2 2 21W1 v2=LM My,
      u= 4 ===2 ^6=== h-
      e= 2 ===1 ^4=== ead
      4= = ==== v2=== For
      o= 4 ===2 ^6=== y-
      14 5 ===3 ^42== ou"""), 142.49, 150.28)
  ]),
  Section("show", "B2", [
    repeat("underwater", 146.37, 150.29),
    repeat("Breathin", 150.29, 153.91),
    repeat("Crazy", 153.91, 159.74)
  ]),
  Section("mirrors", "C2A", [
    repeat("all-me", 159.74, 162.63),
    repeat("all-you", 162.63, 166.38),
    repeat("Curves", 166.38, 170.37),
    repeat("Imperfections", 170.37, 175.05)
  ]),
  Section("Sepulchre", "C2B", [
    repeat("Give-your", 175.05, 177.75),
    phrase("give-my^", notes("""
      u= 4 21W2 ^6=LM i'll
      3= 0 1==3 v3=== Give
      e= Y ===2 ^5=== m-
      o= 9 ===1 ^4=== y
      1= = ==== v3=== All
      4= 7 2==4 ^7=== to
      o2 4 ===2 v35== You"""), 177.75, 181.63),
    repeat("End", 181.63, 185.64),
    repeat("Lose", 185.64, 189.20),
  ]),
  Section("Altar", "C2O", [
    repeat("I-give", 189.20, 196.79),
    repeat("You-give", 196.79, 204.06)
  ]),
  Section("Casino", "M", [
    phrase("Give-me", notes("""
      a= 5 21W3 v3=LM Give
      2= 7 ===4 ^5=== me
      u= Y 1==2 v3=== A-
      3= 0 ===3 v4=== Ll
      e= Y ===2 ^5=== of
      4= 9 ===1 v3=== You
      u= 7 2==4 ^6=== o-
      p= 5 ===3 ^5=== u-
      3= 4 ===2 ^3=== o-
      c= 2 ===1 ^3=== u-
      e1 0 3=C4 ^21== oh"""), 204.06, 207.59),
    phrase("Cards", notes("""
      1= 9 11W2 v3=LM Cards
      u= 7 2==1 ^5=== o-
      3= 5 ===4 ^4=== n
      e= = ==== v3=== The
      o= Y 1==3 ^6=== t-
      1= 0 ===4 ^4=== a-
      u= Y ===3 v2=== B-
      3= 9 ===2 v4=== Le
      e= = ==== ^6=== w-
      4= 7 2==1 ^4=== e're
      o= = ==== v2=== Both
      u= 5 ===4 ^6=== sh-
      3= 4 ===3 ^4=== o-
      e= = ==== v2=== W-
      4= 2 ===2 v4=== Ing
      oe = ==== ^62== hearts"""), 207.59, 215.01),
    phrase("Risk", notes("""
      1= 9 11W1 v2=LM Ris-
      u= 7 2==4 ^6=== king
      3= 5 ===3 ^5=== it
      o= 5 1==2 v2=== A-
      1= 0 ===3 v3=== Ll
      u= Y ===2 ^6=== th-
      3= 9 ===1 ^5=== ough
      e= = ==== v2=== It's
      o3 7 2==4 ^62== hard"""), 215.01, 220.54)
  ]),
  Section("mirrors", "C3A", [
    repeat("all-me", 220.54, 223.52),
    repeat("all-you", 223.52, 227.34),
    repeat("Curves", 227.34, 231.31),
    repeat("Imperfections", 231.31, 235.15)
  ]),
  Section("Sepulchre", "C3B", [
    repeat("Give-your", 235.15, 238.65),
    repeat("give-my^", 238.65, 242.60),
    repeat("End", 242.60, 246.55),
    repeat("Lose", 246.55, 250.20)
  ]),
  Section("Altar", "C3O1", [
    repeat("I-give", 250.20, 257.77),
    repeat("You-give", 257.77, 265.26)
  ]),
  Section("altar", "C3O2", [
    phrase("i-give-auaua", notes("""
      3= 4 21W2 ^7=LM i
      e= 5 ===3 ^6=== give
      4= 7 ===4 ^4=== you
      o= 0 1==3 v2=== A-
      2= 2 ===4 v4=== U-
      u= Y ===2 ^6=== a-
      4= 0 ===3 ^4=== u-
      o= 9 ===1 v2=== A-
      u3 7 2==4 v5=== Ll
      4= 4 ===2 ^7=== of
      o3 = ==== v46== Me"""), 265.26, 273.04),
    repeat("You-give", 273.04, 279.42),
    phrase("ouo", notes("""
      4= 2 21W1 ^6=LM o-
      o= 4 ===2 ^5=== u-
      14 2 ===1 ^41== oh"""), 279.42, 282.03)
  ])
], "63.all-of-me.mp3"))

