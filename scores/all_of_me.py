# vim: foldmethod=marker foldmarker=\ phrase(,) foldtext=getline(v\:foldstart)

import sys; sys.path.append("..")
from violin import *

process_piece(Piece("all-of-me", 4, 126, "48", [
  Section("ART-DESK", "V1", [
    phrase("MOUTH", notes("""
      3= 2 21W1 v2=LM WHAT
      e= 4 ===2 v4=== WOULD
      4= = ==== ^6=== i
      1= = ==== v2=== DO
      a= = ==== ^4=== with-
      2= 2 ===1 v2=== O-
      u= 4 ===2 ^4=== ut
      3= = ==== v2=== YOUR
      4= 0 3=C4 ^6=== smart
      12 = ==== v26== MOUTH?"""), 23.51, 27.31),
    phrase("DRAWIN", notes("""
      3= 2 21W1 v2=LM DRAW-
      e= 4 ===2 v4=== IN
      4= = ==== ^6=== me
      1= = ==== v2=== In
      a= 2 ===1 v4=== A
      2= 4 ===2 ^6=== you
      3= = ==== v2=== KICK-
      e= 2 ===1 ^4=== in
      4= 0 3=C4 v2=== ME
      o= = ==== ^4=== a-
      12 9 ===2 v26== OUT"""), 27.31, 31.12),
    phrase("spinnin", notes("""
      u= 9 31C2 ^6=LM you've
      3= 4 2=W= v4=== GOT
      t= = ==== ^7=== my
      1= 5 ===3 v2=== HEAD
      3= 4 ===2 v5=== SPIN-
      e4 0 3=C4 ^7=== nin,
      1= 5 2=W3 v2=== NO
      3= 4 ===2 v5=== KID-
      e4 0 3=C4 ^73== din"""), 31.12, 35.85),
    phrase("pin", notes("""
      o= 0 31C4 ^3=LM i
      1u 2 2=W1 v2=== CAN'T,
      3= 4 ===2 v5=== PIN
      e= 2 ===1 ^7=== yo-
      o= 9 3=C2 ^4=== u
      1u = ==== v26== DOWN"""),  35.85, 38.95)
  ]),
  Section("DISNEYLAND", "V2", [
    phrase("MIND", notes("""
      3= 2 21W1 v2=LM WHAT'S
      e= 4 ===2 v4=== GO-
      4= = ==== ^6=== in
      1= = ==== v2=== ON
      a= 2 ===1 v4=== IN
      2= 4 ===2 ^6=== that
      3= = ==== v2=== BEAU-
      e= 2 ===1 v4=== TI-
      4= 0 3=C4 ^6=== ful
      w2 = ==== v26== MIND?"""), 38.95, 42.67),
    phrase("ride", notes("""
      3= 4 21W2 ^6=LM i'm
      e= = ==== v4=== ON
      4= = ==== ^6=== your
      1= 7 ===4 v2=== MA-
      a= 5 ===3 v4=== GI-
      2= 4 ===2 ^6=== cal
      3= = ==== v2=== MYS-
      e= 2 ===1 v4=== TE-
      4= 0 3=C4 ^6=== ry-
      o= = ==== v4=== R-
      1u 9 ===2 ^62== ide"""), 42.67, 46.57),
    phrase("DIZZY", notes("""
      3= 4 21W2 v2=LM AND
      e= = ==== ^6=== i'm
      1= 5 ===3 v2=== SO
      3= 4 ===2 v5=== DI-
      e4 0 3=C4 ^7=== zzy,
      o= = ==== ^3=== don't
      1= 4 2=W2 v2=== KN-
      b= 5 ===3 v3=== OW
      2= = ==== ^6=== what
      3= 4 ===2 v4=== HIT
      e4 0 3==4 ^63== me"""), 46.57, 51.03),
    phrase("alright", notes("""
      o= 0 31C4 ^3=LM but
      1= 2 2=W1 v2=== I'LL
      3= 4 ===2 v5=== BE
      e= 2 ===1 ^7=== al-
      1e 5 ===3 v26== RIGHT"""), 51.03, 54.92)
  ]),
  Section("show", "B1", [
    phrase("underwater", notes("""
      o= 0 33W3 ^6=LM my
      1= 7 2=G3 v2=== H-
      b= 9 ===4 v4=== EAD'S
      u= 7 ===3 ^6=== u-
      3= 5 ===2 ^4=== n-
      e= = ==== v2=== DE-
      4= 4 ===1 v4=== R
      o= = ==== ^6=== wa-
      u= 2 3=W4 v2=== TE-
      3= 0 ===3 v4=== R
      e4 = ===3 ^62== but"""), 54.92, 58.71),
    phrase("BREATHIN", notes("""
      o= Y 33W2 v2=LM I'M
      u= 9 =1=2 ^6=== br-
      3= 7 ===1 ^4=== ea-
      e= = ==== v2=== TH-
      4= 9 ===2 v4=== IN
      ou = ==== ^62== fine"""), 58.71, 62.57),
    phrase("CRAZY", notes("""
      o= 7 24P2 v2=LM Y-
      w= 9 ===3 v4=== OU'RE
      u= = ==== ^6=== cr-
      3= 7 ===2 ^4=== a-
      e= = ==== v2=== ZY
      4= 5 ===1 ^6=== and
      o= 4 35G4 v2=== I'M
      u= = ==== ^6=== o-
      3= 2 ===3 ^4=== ut
      e= = ==== v2=== OF
      4= 0 ===2 ^4=== my
      o3 2 ===3 v26== MIND"""), 62.57, 68.21)
  ]),
  Section("mirrors", "C1A", [
    phrase("all-me", notes("""
      o= 4 21W2 ^4=LM cause
      1= = ==== v2=== A-
      b= 7 ===4 v3=== A-
      3= = ==== ^6=== ll
      4= 4 ===2 v2=== OF
      o= 7 ===4 ^5=== m-
      12 9 1==1 v24== E"""), 68.21, 71.10),
    phrase("all-you", notes("""
      3= 4 21W3 ^4=LM loves
      1= 2 ===2 v2=== ALL
      4= 0 3=C4 ^6=== of
      o= 2 2=W3 ^4=== y-
      12 4 ==== v26== OU"""), 71.10, 74.68),
    phrase("CURVES", notes("""
      3= 4 21W2 v2=LM LOVE
      e= = ==== ^6=== you-
      o= 2 ===1 ^5=== r
      1= = ==== v3=== CURVES
      2= = ==== ^5=== and
      3= = ==== v3=== ALL
      4= 0 3=C4 ^5=== your
      o= 2 2=W1 ^4=== ed-
      12 0 3=C4 v35== GES"""), 74.86, 78.86),
    lyrics("IMPERFECTIONS", "ALL you-r PER-fect IM-per-fec-TIONS", "CURVES", 78.86, 82.63)
  ]),
  Section("SEPULCHRE", "C1B", [
    phrase("GIVE-YOUR", notes("""
      3= 4 21W2 v3=LM GIVE
      e= = ==== ^5=== your
      1= = ==== v3=== A-
      b= 7 ===4 v4=== LL
      4= 4 ===2 ^7=== to
      o= 7 ===4 ^6=== m-
      12 9 1==1 v36== E"""), 82.63, 86.35),
    phrase("give-my", notes("""
      u= 2 21W1 ^6=LM i'll
      3= 9 1=== v3=== GIVE
      e= 4 2==2 ^5=== m-
      o= 2 ===1 ^4=== y
      1= = ==== v3=== ALL
      4= 0 3=C4 ^7=== to
      o= 2 2=W1 ^6=== yo-
      12 4 ===2 v35== U"""), 86.35, 90.10),
    lyrics("END", "YOU'RE m-y END and MY be-gin-ING", "CURVES", 90.10, 94.17),
    lyrics("LOSE", "E-ve-n WHEN i LOSE i'm win-NING", "CURVES", 94.17, 97.70)
  ]),
  Section("ALTAR", "C1O", [
    phrase("I-GIVE", notes("""
      u= 4 21W2 v6=LM CAUSE
      3= = ==== ^7=== i
      e= 5 ===3 ^6=== give
      4= 7 ===4 ^4=== you
      o= 0 1==3 v2=== A-
      u= Y ===2 ^6=== u-
      p= 0 ===3 ^5=== i-
      3= Y ===2 ^4=== a-
      o= 9 ===1 v2=== A-
      u3 7 2==4 v5=== LL
      4= 4 ===2 ^7=== of
      ou = ==== v46== ME"""), 97.70, 105.29),
    lyrics("YOU-GIVE", "AND you give me A-u-i-a-A-LL of YOU", "I-GIVE", 105.29, 111.83),
    phrase("OO", notes("""
      4= 4 21W2 ^6=LM oh-
      o3 2 ===1 v26== O"""), 111.83, 115.05)
  ]),
  Section("BEDROOM", "V3", [
    phrase("TIMES", notes("""
      3= 2 21W1 v2=LM HOW
      e= 4 ===2 v4=== MA-
      4= 2 ===1 ^6=== ni-
      m= 4 ===2 ^4=== y
      1= 2 ===1 v2=== T-
      a= 4 ===2 v4=== IMES
      2= = ==== ^6=== do
      u= 2 ===1 ^4=== i
      3= 4 ===2 v2=== HAVE
      e= 2 ===1 v4=== TO
      4= 0 3=C4 ^6=== tell
      12 = ==== v26== YOU?"""), 115.05, 118.98),
    phrase("CRYING", notes("""
      3= 4 21W2 v2=LM E-
      e= = ==== ^4=== ven
      4= = ==== v2=== WHEN
      o= = ==== ^4=== you're
      1= 5 ===3 v2=== C-
      b= 7 ===4 v4=== RY-
      2= 5 ===3 ^6=== ing
      u= 4 ===2 ^4=== you're
      3= = ==== v2=== BEAU-
      e= 2 ===1 v4=== TI-
      4= 0 1=C4 ^6=== ful
      o= = ==== v4=== T-
      12 9 ===2 ^64== oo"""), 118.98, 122.55),
    phrase("beating", notes("""
      u= 0 31C4 ^6=LM the
      3= 2 2=W1 v2=== W-
      c= 4 ===2 v4=== ORLD
      t= = ==== ^6=== is
      1= 5 ===3 v2=== BEAT-
      u= 4 ===2 ^6=== i-
      p= 5 ===3 ^4=== i-
      3= 4 ===2 ^3=== ing
      e= 0 3=C4 v2=== YOU
      o= 4 2=W2 ^6=== d-
      1= 5 ===3 ^4=== own
      u= 4 ===2 v2=== I-
      e= 0 3=C4 v4=== M
      4= = ==== ^6=== a-
      o2 2 2=W1 v26== ROUND"""), 122.55, 128.17),
    phrase("mood", notes("""
      u= 2 21W1 ^6=LM through
      3= 4 ===2 v2=== E-
      e= 2 ===1 v4=== VE-
      4= = ==== ^6=== ry
      o2 9 3=C2 v26== MOOD"""), 128.17, 130.19)
  ]),
  Section("GARAGE", "V4", [
    phrase("DOWNFALL", notes("""
      p= 7 21W4 v2=LM YOU'RE
      e= 4 ===2 ^4=== my
      o= = ==== v2=== DOWN-
      a= 0 3=C4 ^6=== fall,
      3= 7 2=W= v2=== YOU'RE
      e= 4 ===2 ^4=== my
      oa = ==== v26== MUSE"""), 130.19, 133.97),
    phrase("distraction", notes("""
      u= 0 31C4 ^6=LM my
      3= 5 2=W3 v2=== W-
      e= 7 ===4 v4=== ORST
      4= 4 ===2 ^6=== dis-
      o= = ==== v2=== TRA-
      1= 2 ===1 v4=== AC-
      a= = ==== ^6=== tion,
      u= = ==== v2=== MY
      3= 4 ===2 ^4=== rhy-
      e= 2 ===1 v2=== THM
      4= 4 ===2 ^4=== n
      o2 9 3=C2 v26== BLUES"""), 133.97, 137.69),
    phrase("singing", notes("""
      u= 4 21W2 ^6=LM i
      3= = ==== v4=== CAN'T
      t= = ==== ^6=== stop
      1= 5 ===3 v2=== SI-
      u= 4 ===2 ^6=== ngi-
      3= 0 3=C4 v4=== ING
      e4 = ==== ^6=== it's,
      o= 4 2=W2 v2=== RI-
      1= 5 ===3 v4=== I-
      u= 4 ===2 ^6=== ngi-
      3= 0 3=C4 v4=== ING
      e4 = ==== ^62== in"""), 137.69, 142.49),
    phrase("HEAD", notes("""
      o2 2 21W1 v2=LM MY,
      u= 4 ===2 ^6=== h-
      e= 2 ===1 ^4=== ead
      4= = ==== v2=== FOR
      o= 4 ===2 ^6=== y-
      14 5 ===3 ^42== ou"""), 142.49, 150.28)
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
      u= 4 21W2 ^6=LM i'll
      3= 0 1==3 v3=== GIVE
      e= Y ===2 ^5=== m-
      o= 9 ===1 ^4=== y
      1= = ==== v3=== ALL
      4= 7 2==4 ^7=== to
      o2 4 ===2 v35== YOU"""), 177.75, 181.63),
    repeat("END", 181.63, 185.64),
    repeat("LOSE", 185.64, 189.20),
  ]),
  Section("ALTAR", "C2O", [
    repeat("I-GIVE", 189.20, 196.79),
    repeat("YOU-GIVE", 196.79, 204.06)
  ]),
  Section("CASINO", "M", [
    phrase("GIVE-ME", notes("""
      a= 5 21W3 v3=LM GIVE
      2= 7 ===4 ^5=== me
      u= Y 1==2 v3=== A-
      3= 0 ===3 v4=== LL
      e= Y ===2 ^5=== of
      4= 9 ===1 v3=== YOU
      u= 7 2==4 ^6=== o-
      p= 5 ===3 ^5=== u-
      3= 4 ===2 ^3=== o-
      c= 2 ===1 ^3=== u-
      e1 0 3=C4 ^21== oh"""), 204.06, 207.59),
    phrase("CARDS", notes("""
      1= 9 11W2 v3=LM CARDS
      u= 7 2==1 ^5=== o-
      3= 5 ===4 ^4=== n
      e= = ==== v3=== THE
      o= Y 1==3 ^6=== t-
      1= 0 ===4 ^4=== a-
      u= Y ===3 v2=== B-
      3= 9 ===2 v4=== LE
      e= = ==== ^6=== w-
      4= 7 2==1 ^4=== e're
      o= = ==== v2=== BOTH
      u= 5 ===4 ^6=== sh-
      3= 4 ===3 ^4=== o-
      e= = ==== v2=== W-
      4= 2 ===2 v4=== ING
      oe = ==== ^62== hearts"""), 207.59, 215.01),
    phrase("RISK", notes("""
      1= 9 11W1 v2=LM RIS-
      u= 7 2==4 ^6=== king
      3= 5 ===3 ^5=== it
      o= 5 1==2 v2=== A-
      1= 0 ===3 v3=== LL
      u= Y ===2 ^6=== th-
      3= 9 ===1 ^5=== ough
      e= = ==== v2=== IT'S
      o3 7 2==4 ^62== hard"""), 215.01, 220.54)
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
      3= 4 21W2 ^7=LM i
      e= 5 ===3 ^6=== give
      4= 7 ===4 ^4=== you
      o= 0 1==3 v2=== A-
      2= 2 ===4 v4=== U-
      u= Y ===2 ^6=== a-
      4= 0 ===3 ^4=== u-
      o= 9 ===1 v2=== A-
      u3 7 2==4 v5=== LL
      4= 4 ===2 ^7=== of
      o3 = ==== v46== ME"""), 265.26, 273.04),
    repeat("YOU-GIVE", 273.04, 279.42),
    phrase("ouo", notes("""
      4= 2 21W1 ^6=LM o-
      o= 4 ===2 ^5=== u-
      14 2 ===1 ^41== oh"""), 279.42, 282.03)
  ])
], "63.all-of-me.mp3"))

