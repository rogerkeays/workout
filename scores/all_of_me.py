# vim: foldmethod=marker foldmarker=\ Phrase(,) foldtext=getline(v\:foldstart)

import sys; sys.path.append("..")
from violin import *

# phrases
mouth = Phrase("mouth", parse_violin_notes("""
      3= 2 12W1 2v=LM what
      e= 4 ===2 4v=== would
      4= = ==== 6^=== i
      1= = ==== 2v=== do
      a= = ==== 4^=== with
      2= 2 ===1 2v=== o
      u= 4 ===2 4^=== -ut
      3= = ==== 2v=== your
      4= 0 =3C4 6^=== smart
      12 = ==== 2v6== mouth?"""), 23.51, 27.31)
drawin = Phrase("drawin'", parse_violin_notes("""
      3= 2 12W1 2v=LM draw
      e= 4 ===2 4v=== -in
      4= = ==== 6^=== me
      1= = ==== 2v=== in
      a= 2 ===1 4v=== a
      2= 4 ===2 6^=== you
      3= = ==== 2v=== kick
      e= 2 ===1 4^=== -in
      4= 0 =3C4 2v=== me
      o= = ==== 4^=== a
      12 9 ===2 2v6== -out"""), 27.31, 31.12)
spinnin = Phrase("spinnin'", parse_violin_notes("""
      u= 9 13C2 6^=LM you've
      3= 4 =2W= 4v=== got
      t= = ==== 7^=== my
      1= 5 ===3 2v=== head
      3= 4 ===2 5v=== spin
      e4 0 =3C4 7^=== -nin,
      1= 5 =2W3 2v=== no
      3= 4 ===2 5v=== kid
      e4 0 =3C4 7^3== -din"""), 31.12, 35.85)
pin = Phrase("pin", parse_violin_notes("""
      o= 0 13C4 3^=== i
      1u 2 =2W1 2v=== can't,
      3= 4 ===2 5v=== pin
      e= 2 ===1 7^=== yo
      o= 9 =3C2 4^=== -u
      1u = ==== 2v6== down"""),  35.85, 38.95)

mind = Phrase("mind", parse_violin_notes("""
      3= 2 12W1 2v=LM what's
      e= 4 ===2 4v=== go
      4= = ==== 6^=== -in
      1= = ==== 2v=== on
      a= 2 ===1 4v=== in
      2= 4 ===2 6^=== that
      3= = ==== 2v=== beau
      e= 2 ===1 4v=== ti
      4= 0 =3C4 6^=== ful
      w2 = ==== 2v6== mind?"""), 38.95, 42.67)
ride = Phrase("ride", parse_violin_notes("""
      3= 4 12W2 6^=LM i'm
      e= = ==== 4v=== on
      4= = ==== 6^=== your
      1= 7 ===4 2v=== ma
      a= 5 ===3 4v=== gi
      2= 4 ===2 6^=== cal
      3= = ==== 2v=== mys
      e= 2 ===1 5^=== te
      4= 0 =3C4 3v=== ry
      o= = ==== 5^=== r
      1u 9 ===2 3v7== -ide"""), 42.67, 46.57)
dizzy = Phrase("dizzy", parse_violin_notes("""
      3= 4 12W2 2v=== and
      e= = ==== 6^=== i'm
      1= 5 ===3 2v=== so
      3= 4 ===2 5v=== di
      e4 0 =3C4 7^=== zzy,
      o= = ==== 3^=== don't
      1= 4 =2W2 2v=== kn
      b= 5 ===3 3v=== -ow
      2= = ==== 6^=== what
      3= 4 ===2 4v=== hit
      e4 0 =3=4 6^3== me"""), 46.57, 51.03)
alright = Phrase("alright", parse_violin_notes("""
      o= 0 13C4 3^=== but
      1= 2 =2W1 2v=== i'll
      3= 4 ===2 5v=== be
      e= 2 ===1 7^=== al
      1e 5 ===3 2v6== -right"""), 51.03, 54.92)

underwater = Phrase("underwater", parse_violin_notes("""
      o= 0 33W3 6^=LM my
      1= 7 =2G3 2v=== h
      b= 9 ===4 4v=== -ead's
      u= 7 ===3 6^=== u
      3= 5 ===2 4^=== -n
      e= = ==== 2v=== de
      4= 4 ===1 4v=== -r
      o= = ==== 6^=== wa
      u= 2 =3W4 2v=== te
      3= 0 ===3 4v=== -r
      e4 = ===3 6^2== but"""), 54.92, 58.71)
breathin = Phrase("breathin'", parse_violin_notes("""
      o= Y 33W2 2v=LM i'm
      u= 9 1==2 6^=== br
      3= 7 ===1 4^=== -ea
      e= = ==== 2v=== th
      4= 9 ===2 4v=== -in
      ou = ==== 6^2== fine"""), 58.71, 62.57)
crazy = Phrase("crazy", parse_violin_notes("""
      o= 7 42P2 2v=== y
      w= 9 ===3 4v=== -ou're
      u= = ==== 6^=== cr
      3= 7 ===2 4^=== -a
      e= = ==== 2v=== zy
      4= 5 ===1 6^=== and
      o= 4 53G4 2v=== i'm
      u= = ==== 6^=== o
      3= 2 ===3 4^=== -ut
      e= = ==== 2v=== of
      4= 0 ===2 4^=== my
      o3 2 ===3 2v6== mind"""), 62.57, 68.21)

all_me = Phrase("all-me", parse_violin_notes("""
      o= 4 12W2 4^=LM cause
      1= = ==== 2v=== a-
      b= 7 ===4 3v=== a-
      3= = ==== 6^=== ll
      4= 4 ===2 2v=== of
      o= 7 ===4 5^=== m-
      12 9 =1=1 2v4== e"""), 68.21, 71.10)
all_you = Phrase("all-you", parse_violin_notes("""
      3= 4 12W3 4^=LM loves
      1= 2 ===2 2v=== all
      4= 0 =3C4 6^=== of
      o= 2 =2W3 4^=== y-
      12 4 ==== 2v6== ou"""), 71.10, 74.68)
curves = Phrase("curves", parse_violin_notes("""
      3= 4 12W2 2v=LM love
      e= = ==== 6^=== you-
      o= 2 ===1 5^=== r
      1= = ==== 3v=== curves
      2= = ==== 5^=== and
      3= = ==== 3v=== all
      4= 0 =3C4 5^=== your
      o= 2 =2W1 4^=== ed-
      12 9 =3C2 3v5== ges"""), 74.86, 78.86)
imperfections = clone(curves, "all you-r per-fect im-per-fec-tions", 78.86, 82.63)

give_your = Phrase("give-your", parse_violin_notes("""
      3= 4 12W2 3v=LM give
      e= = ==== 5^=== your
      1= = ==== 3v=== a-
      b= 7 ===4 4v=== ll
      4= 4 ===2 7^=== to
      o= 7 ===4 6^=== m-
      12 9 =1=1 3v6== e"""), 82.63, 86.35)
give_my = Phrase("give-my", parse_violin_notes("""
      u= 2 12W1 6^=LM i'll
      3= 9 =1== 3v=== give
      e= 4 =2=2 5^=== m-
      o= 2 ===1 4^=== y
      1= = ==== 3v=== all
      4= 0 =3C4 7^=== to
      o= 2 =2W1 6^=== yo-
      12 4 ===2 3v5== u"""), 86.35, 90.10)
end = clone(curves, "you're m-y end and my be-gin-ing", 90.10, 94.17)
lose = clone(curves, "e-ve-n when i lose i'm win-ning", 94.17, 97.70)

i_give = Phrase("i-give", parse_violin_notes("""
      u= 4 12W2 6v=LM cause
      3= = ==== 7^=== i
      e= 5 ===3 6^=== give
      4= 7 ===4 4^=== you
      o= 0 =1=3 2v=== a-
      u= Y ===2 6^=== u-
      p= 0 ===3 5^=== i-
      3= Y ===2 4^=== a-
      o= 9 ===1 2v=== a-
      u3 7 =2=4 5v=== ll
      4= 4 ===2 7^=== of
      ou = ==== 4v6== me"""), 97.70, 105.29)
you_give = clone(i_give, "and you give me a-u-i-a-a-ll of you", 105.29, 111.83)
oo = Phrase("oo", parse_violin_notes("""
      4= 4 12W2 6v=== oh-
      o3 2 ===1 2^6== -o"""), 111.83, 115.05)

times = Phrase("times", parse_violin_notes("""
      3= 2 12W1 2v=== how
      e= 4 ===2 4v=== ma-
      4= 2 ===1 6^=== -ni-
      m= 4 ===2 4^=== -y
      1= 2 ===1 2v=== t-
      a= 4 ===2 4v=== imes
      2= = ==== 6^=== do
      u= 2 ===1 4^=== i
      3= 4 ===2 2v=== have
      e= 2 ===1 4v=== to
      4= 0 =3C4 6^=== tell
      12 = ==== 2v6== you?"""), 115.05, 118.98)
crying = Phrase("crying", parse_violin_notes("""
      3= 4 12W2 2v=== e-
      e= = ==== 4^=== ven
      4= = ==== 2v=== when
      o= = ==== 4^=== you're
      1= 5 ===3 2v=== c-
      b= 7 ===4 4v=== -ry-
      2= 5 ===3 6^=== -ing
      u= 4 ===2 4^=== you're
      3= = ==== 2v=== beau-
      e= 2 ===1 4^=== ti-
      4= 0 =1C4 6v=== -ful
      o= = ==== 2^=== t-
      12 9 ===2 2v6== -oo"""), 118.98, 122.55)
beating = Phrase("beating", parse_violin_notes("""
      u= 0 13C4 6^=== the
      3= 2 =2W1 2v=== w-
      c= 4 ===2 4v=== -orld
      t= = ==== 6^=== is
      1= 5 ===3 2v=== beat-
      u= 4 ===2 6^=== -i-
      p= 5 ===3 4^=== -i-
      3= 4 ===2 3^=== -ing
      e= 0 =3C4 2v=== you
      o= 4 =2W2 6^=== d-
      1= 5 ===3 4^=== -own
      u= 4 ===2 2v=== i-
      e= 0 =3C4 4v=== -m
      4= = ==== 6^=== a-
      o2 2 =2W1 2v6== -round"""), 122.55, 128.17)
mood = Phrase("mood", parse_violin_notes("""
      u= 2 12W1 6^=== through
      3= 4 ===2 2v=== e-
      e= 2 ===1 4v=== -ve-
      4= = ==== 6^=== -ry
      o2 9 =3C2 2v6== mood"""), 128.17, 130.19)

downfall = Phrase("downfall", parse_violin_notes("""
      p= 7 12W4 2v=== you're
      e= 4 ===2 4^=== my
      o= = ==== 2v=== down-
      a= 0 =3C4 6^=== fall,
      3= 7 =2W= 2v=== you're
      e= 4 ===2 4^=== my
      oa = ==== 2v6== muse"""), 130.19, 133.97)
distraction = Phrase("distraction", parse_violin_notes("""
      u= 0 13C4 6^=== my
      3= 5 =2W3 2v=== w-
      e= 7 ===4 4v=== orst
      4= 4 ===2 6^=== dis-
      o= = ==== 2v=== tra-
      1= 2 ===1 4v=== ac-
      a= = ==== 6^=== tion,
      u= = ==== 2v=== my
      3= 4 ===2 4^=== rhy-
      e= 2 ===1 2v=== thm
      4= 4 ===2 4^=== n
      o2 9 =3C2 2v6== blues"""), 133.97, 137.69)
singing = Phrase("singing", parse_violin_notes("""
      u= 4 12W2 6^=== i
      3= = ==== 4v=== can't
      t= = ==== 6^=== stop
      1= 5 ===3 2v=== si-
      u= 4 ===2 6^=== ngi-
      3= 0 =3C4 4v=== ing
      e4 = ==== 6^=== it's,
      o= 4 =2W2 2v=== ri-
      1= 5 ===3 4v=== -i-
      u= 4 ===2 6^=== ngi-
      3= 0 =3C4 4v=== ing
      e4 = ==== 6^2== in"""), 137.69, 142.49)
head = Phrase("head", parse_violin_notes("""
      o2 2 12W1 2v=== my,
      u= 4 ===2 6^=== h-
      e= 2 ===1 4^=== -ead
      4= = ==== 2v=== for
      o= 4 ===2 6^=== y-
      14 5 ===3 4^2== -ou"""), 142.49, 150.28)

give_me = Phrase("give-me", parse_violin_notes("""
      a= 5 12W3 3v=LM give
      2= 7 ===4 5^=== me
      u= Y =1=2 3v=== a-
      3= 0 ===3 4v=== ll
      e= Y ===2 5^=== of
      4= 9 ===1 3v=== you
      u= 7 =2=4 6^=== o-
      p= 5 ===3 5^=== u-
      3= 4 ===2 3^=== o-
      c= 2 ===1 3^=== u-
      e1 0 =3C4 2^1== oh"""), 204.06, 207.59)
cards = Phrase("cards", parse_violin_notes("""
      1= 9 11W2 3v=LM cards
      u= 7 =2=1 5^=== o-
      3= 5 ===4 4^=== n
      e= = ==== 3v=== the
      o= Y =1=3 6^=== t-
      1= 0 ===4 4^=== a-
      u= Y ===3 2v=== b-
      3= 9 ===2 4v=== le
      e= = ==== 6^=== w-
      4= 7 =2=1 4^=== e're
      o= = ==== 2v=== both
      u= 5 ===4 6^=== sh-
      3= 4 ===3 4^=== o-
      e= = ==== 2v=== w-
      4= 2 ===2 4v=== ing
      oe = ==== 6^2== hearts"""), 207.59, 215.01)
risk = Phrase("risk", parse_violin_notes("""
      1= 9 11W1 2v=LM ris-
      u= 7 =2=4 6^=== king
      3= 5 ===3 5^=== it
      o= 5 =1=2 2v=== a-
      1= 0 ===3 3v=== ll
      u= Y ===2 6^=== th-
      3= 9 ===1 5^=== ough
      e= = ==== 2v=== it's
      o3 7 =2=4 6^2== hard"""), 215.01, 220.54)

give_myx = Phrase("give-my^", parse_violin_notes("""
      u= 4 12W2 6^=LM i'll
      3= 0 =1=3 3v=== give
      e= Y ===2 5^=== m-
      o= 9 ===1 4^=== y
      1= = ==== 3v=== all
      4= 7 =2=4 7^=== to
      o2 4 ===2 3v5== you"""), 238.65, 242.60)
i_givex = Phrase("auaua", parse_violin_notes("""
      3= 4 12W2 7^=LM i
      e= 5 ===3 6^=== give
      4= 7 ===4 4^=== you
      o= 0 =1=3 2v=== a-
      2= 2 ===4 4v=== u-
      u= Y ===2 6^=== a-
      4= 0 ===3 4^=== u-
      o= 9 ===1 2v=== a-
      u3 7 =2=4 5v=== ll
      4= 4 ===2 7^=== of
      o3 = ==== 4v6== me"""), 265.26, 273.04)
ouo = Phrase("ouo", parse_violin_notes("""
      4= 2 12W1 6^=LM o-
      o= 4 ===2 5^=== u-
      14 2 ===1 4^1== oh"""), 279.42, 282.03)

# arrangement
process_piece(Piece("all-of-me", 4, 126, "48", [
  Section("art-desk", "V1", [ mouth, drawin, spinnin, pin ]),
  Section("disneyland", "V2", [ mind, ride, dizzy, alright ]),
  Section("show", "B", [ underwater, breathin, crazy ]),
  Section("church/mirrors", "CA", [ all_me, all_you, curves, imperfections ]),
  Section("church/sepulchre", "CB", [ give_your, give_my, end, lose ]),
  Section("altar", "O", [ i_give, you_give, oo ]),
  Section("bedroom", "V3", [ times, crying, beating, mood ]),
  Section("garage", "V4", [ downfall, distraction, singing, head ]),
  Section("show", "B", [ underwater, breathin, crazy ]), # 146.37, 150.29, 153.91
  Section("church/mirrors", "CA", [ all_me, all_you, curves, imperfections ]), # 159.74, 162.63, 166.38, 170.37
  Section("church/sepulchre", "CB", [ give_your, give_my, end, lose ]), # 175.05, 177.75, 181.63, 185.64
  Section("altar", "O", [ i_give, you_give ]), # 189.20, 196.79
  Section("casino", "M", [ give_me, cards, risk ]),
  Section("church/mirrors", "CA", [ all_me, all_you, curves, imperfections ]), # 220.54, 223.52, 227.34, 231.31
  Section("church/sepulchre", "CB", [ give_your, give_myx, end, lose ]), # 235.15, 238.65, 242.60, 246.55
  Section("altar", "O", [ i_give, you_give ]), # 250.20, 257.77
  Section("altar", "O", [ i_givex, you_give, ouo ]) # 265.26, 273.04, >279.42
], "63.all-of-me.mp3"))

