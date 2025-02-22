# vim: foldmethod=marker foldmarker=\ \ Phrase,\ ) foldtext=getline(v\:foldstart)

import sys; sys.path.append("..")
from violin import *

def parse_violin_notesx(text: str): return []

process_piece(Piece("all-of-me", 4, 126, "48", [
  Section("art-desk", "V1", [
    Phrase("mouth", parse_violin_notes("""
      3= 2 21W1 2v=LM what
      e= 4 ===2 4v=== would
      4= = ==== 6^=== i
      1= = ==== 2v=== do
      a= = ==== 4v=== with
      2= 2 ===1 6^=== o
      u= 4 ===2 4^=== -ut
      3= = ==== 2v=== your
      4= 0 3=C4 6^=== smart
      12 = ==== 2v6== mouth?"""), 23.51, 27.31
    ),
    Phrase("drawin'", parse_violin_notes("""
      3= 2 21W1 2v=LM draw
      e= 4 ===2 4v=== -in
      4= = ==== 6^=== me
      1= = ==== 2v=== in
      a= 2 ===1 4v=== a
      2= 4 ===2 6^=== you
      3= = ==== 2v=== kick
      e= 2 ===1 4v=== -in
      4= 0 3=C4 6^=== me
      o= = ==== 4^=== a
      12 9 ===2 2v6== -out"""), 27.31, 31.12
    ),
    Phrase("spinnin'", parse_violin_notes("""
      u= 9 31C2 6^=LM you've
      3= 4 2=W= 4v=== got
      t= = ==== 7^=== my
      1= 5 ===3 2v=== head
      3= 4 ===2 5v=== spin
      e4 0 3=C4 7^=== -nin,
      1= 5 2=W3 2v=== no
      3= 4 ===2 5v=== kid
      e4 0 3=C4 7^3== -din"""), 31.12, 35.85
    ),
    Phrase("pin", parse_violin_notes("""
      o= 0 31C4 3^=== i
      1u 2 2=W1 2v=== can't,
      3= 4 ===2 5v=== pin
      e= 2 ===1 7^=== yo
      o= 9 3=C2 4^=== -u
      1u = ==== 2v6== down"""),  35.85, 38.95
    )
  ]),
  Section("disneyland", "V2", [
    Phrase("mind", parse_violin_notes("""
      3= 2 21W1 2v=LM what's
      e= 4 ===2 4v=== go
      4= = ==== 6^=== -in
      1= = ==== 2v=== on
      a= 2 ===1 4v=== in
      2= 4 ===2 6^=== that
      3= = ==== 2v=== beau
      e= 2 ===1 4v=== ti
      4= 0 3=C4 6^=== ful
      w2 = ==== 2v6== mind?"""), 38.95, 42.67
    ),
    Phrase("ride", parse_violin_notes("""
      3= 4 21W2 2v=LM i'm
      e= = ==== 4v=== on
      4= = ==== 6^=== your
      1= 7 ===4 2v=== ma
      a= 5 ===3 4v=== gi
      2= 4 ===2 6^=== cal
      3= = ==== 2v=== mys
      e= 2 ===1 5^=== te
      4= 0 3=C4 3v=== ry
      o= = ==== 5^=== r
      1u 9 ===2 3v7== -ide"""), 42.67, 46.57
    ),
    Phrase("dizzy", parse_violin_notes("""
      3= 4 21W2 2v=== and
      e= = ==== 6^=== i'm
      1= 5 ===3 2v=== so
      3= 4 ===2 5v=== di
      e4 0 3=C4 7^=== zzy,
      o= = ==== 3^=== don't
      1= 4 2=W2 2v=== kn
      b= 5 ===3 3v=== -ow
      2= = ==== 6^=== what
      3= 4 ===2 4v=== hit
      e4 0 3==4 6^3== me"""), 46.57, 51.03
    ),
    Phrase("alright", parse_violin_notes("""
      o= 0 31C4 3^=== but
      1= 2 2=W1 2v=== i'll
      3= 4 ===2 5v=== be
      e= 2 ===1 7^=== al
      1e 5 ===3 2v6== -right"""), 51.03, 54.92
    )
  ]),
  Section("show", "B", [
    Phrase("underwater", parse_violin_notes("""
      o= 0 33G3 6^=LM my
      1= 7 2=W3 2v=== h
      b= 9 ===4 4v=== -ead's
      u= 7 ===3 6^=== u
      3= 5 ===2 4^=== -n
      e= = ==== 2v=== de
      4= 4 ===1 4v=== -r
      o= = ==== 6^=== wa
      u= 2 3=G4 2v=== te
      3= 0 ===3 4v=== -r
      e4 = ===3 6^2== but"""), 54.92, 58.71
    ),
    Phrase("breathin'", parse_violin_notes("""
      o= Y 33G2 2v=LM i'm
      u= 9 =1=2 6^=== br
      3= 7 ===1 4^=== -ea
      e= = ==== 2v=== th
      4= 9 ===2 4v=== -in
      ou = ==== 6^2== fine"""), 58.71, 62.57
    ),
    Phrase("crazy'", parse_violin_notes("""
      o= 7 25P2 2==== y
      w= 9 ===3 4==== -ou're
      u= = ==== 6==== cr
      3= 7 ===2 4==== -a
      e= = ==== 2==== zy
      4= 5 ===1 ===== and
      o= 4 3=G4 ===== i'm
      u= = ==== ===== o
      3= 2 ===3 ===== -ut
      e= = ==== ===== of
      4= 0 ===2 ===== my
      o3 2 ===3 ===== mind"""), 62.57, 68.21
    )
  ]),
  Section("church/mirrors", "CA", [
    #Phrase("all-me", clone(), 68.21)
    #Phrase("all-you", clone(), 71.10)
    #Phrase("curves", clone(), 74.86)
    #Phrase("imperfections", clone(), 78.86)
  ]),
  Section("church/sepulchre", "CB", [
    #Phrase("give-your", clone(), 82.63)
    #Phrase("give-my", clone(), 86.35)
    #Phrase("end", clone(), 90.10)
    #Phrase("lose", clone(), 94.17)
  ]),
  Section("altar", "O", [
    #Phrase("i-give", clone(), 97.70)
    #Phrase("you-give", clone(), 105.28)
    Phrase("oo", parse_violin_notes("""
      4= 4 21W2 ===== oh-
      o3 2 ===1 ===== -o"""), 111.83, 115.05
    )
  ]),
  Section("bedroom", "V3", [
    Phrase("times", parse_violin_notes("""
      3= 2 21W1 ===== how
      e= 4 ===2 ===== ma-
      4= 2 ===1 ===== -ni-
      m= 4 ===2 ===== -y
      1= 2 ===1 ===== t-
      a= 4 ===2 ===== imes
      2= = ==== ===== do
      u= 2 ===1 ===== i
      3= 4 ===2 ===== have
      e= 2 ===1 ===== to
      4= 0 3=C4 ===== tell
      12 = ==== ===== you?"""), 115.05, 118.98
    ),
    Phrase("crying", parse_violin_notes("""
      3= 4 21W2 ===== e-
      e= = ==== ===== ven
      4= = ==== ===== when
      o= = ==== ===== you're
      1= 5 ===3 ===== c-
      b= 7 ===4 ===== -ry-
      2= 5 ===3 ===== -ing
      u= 4 ===2 ===== you're
      3= = ==== ===== beau-
      e= 2 ===1 ===== ti-
      4= 0 1=C4 ===== -ful
      o= = ==== ===== t-
      12 9 ===2 ===== -oo"""), 118.98, 122.55
    ),
    Phrase("beating", parse_violin_notes("""
      u= 0 31C4 ===== the
      3= 2 2=W1 ===== w-
      c= 4 ===2 ===== -orld
      t= = ==== ===== is
      1= 5 ===3 ===== bea-
      u= 4 ===2 ===== -t-
      p= 5 ===3 ===== -i-
      3= 4 ===2 ===== -ng
      e= 0 3=C4 ===== you
      o= 4 2=W2 ===== d-
      1= 5 ===3 ===== -own
      u= 4 ===2 ===== i-
      e= 0 3=C4 ===== -m
      4= = ==== ===== a-
      o2 2 2=W1 ===== -round"""), 122.55, 128.17
    ),
    Phrase("mood", parse_violin_notes("""
      u= 2 21W1 ===== through
      3= 4 ===2 ===== e-
      e= 2 ===1 ===== -ve-
      4= = ==== ===== -ry
      o2 9 3=C2 ===== mood"""), 128.17, 130.19
    )
  ]),
  Section("garage", "V4", [
    Phrase("downfall", parse_violin_notes("""
      p= 7 21W4 ===== you're
      e= 4 ===2 ===== my
      o= = ==== ===== down-
      a= 0 3=C4 ===== fall,
      3= 7 2=W= ===== you're
      e= 4 ===2 ===== my
      oa = ==== ===== muse"""), 130.19, 133.97
    ),
    Phrase("distraction", parse_violin_notes("""
      u= 0 31C4 ===== my
      3= 5 2=W3 ===== w-
      e= 7 ===4 ===== orst
      4= 4 ===2 ===== dis-
      o= = ==== ===== tra-
      1= 2 ===1 ===== ac-
      a= = ==== ===== tion,
      u= = ==== ===== my
      3= 4 ===2 ===== rhy-
      e= 2 ===1 ===== thm
      4= 4 ===2 ===== n
      o2 9 31C4 ===== blues"""), 133.97, 137.69
    ),
    Phrase("singing", parse_violin_notes("""
      u= 4 21W2 ===== i
      3= = ==== ===== can't
      t= = ==== ===== stop
      1= 5 ===3 ===== si-
      u= 4 ===2 ===== ngi-
      3= 0 3=C4 ===== ing
      e4 = ==== ===== it's,
      o= 4 2=W2 ===== ri-
      1= 5 ===3 ===== -i-
      u= 4 ===2 ===== ngi-
      3= 0 3=C4 ===== ing
      e4 = ==== ===== in"""), 137.69, 142.49
    ),
    Phrase("head", parse_violin_notes("""
      o2 2 21W1 ===== my,
      u= 4 ===2 ===== h-
      e= 2 ===1 ===== -ead
      4= = ==== ===== for
      o= 4 ===2 ===== y-
      14 5 ===3 ===== -ou"""), 142.49, 150.28
    )
  ]),
  Section("show", "B", [
    #Phrase("underwater", clone(), 146.37)
    #Phrase("breathing", clone(), 150.29)
    #Phrase("crazy", clone(), 153.91)
  ]),
  Section("church/mirrors", "CA", [
    #Phrase("all-me", clone(), 159.74)
    #Phrase("all-you", clone(), 162.63)
    #Phrase("curves", clone(), 166.38)
    #Phrase("imperfections", clone(), 170.37)
  ]),
  Section("church/sepulchre", "CB", [
    #Phrase("give-your", clone(), 174.05)
    Phrase("give-my", parse_violin_notes("""
      u= 2 21W1 6^=LM i'll
      3= 9 1=== 3v=== give
      e= 4 2==2 5^=== m-
      o= 2 ===1 4^=== y
      1= = ==== 3v=== all
      4= 0 3=C4 7^=== to
      o= 2 2=W1 6^=== yo-
      12 4 ===2 3v5== u"""), 177.75, 181.63
    ),
    #Phrase("end", clone(), 181.63)
    #Phrase("lose", clone(), 185.64)
  ]),
  Section("altar", "O", [
    #Phrase("i-give", clone(), 189.20)
    #Phrase("you-give", clone(), 196.79)
  ]),
  Section("casino", "M", [
    Phrase("give-me", parse_violin_notes("""
      a= 5 21W3 3v=LM give
      2= 7 ===4 5^=== me
      u= Y 1==2 3v=== a-
      3= 0 ===3 4v=== ll
      e= Y ===2 5^=== of
      4= 9 ===1 3v=== you
      u= 7 2==4 6^=== o-
      p= 5 ===3 5^=== u-
      3= 4 ===2 3^=== o-
      c= 2 ===1 3^=== u-
      e1 0 3=C4 2^1== oh"""), 204.06, 207.59
    ),
    Phrase("cards", parse_violin_notes("""
      1= 9 11W2 3v=LM cards
      u= 7 2==1 5^=== o-
      3= 5 ===4 4^=== n
      e= = ==== 3v=== the
      o= Y 1==3 6^=== t-
      1= 0 ===4 4^=== a-
      u= Y ===3 2v=== b-
      3= 9 ===2 4v=== le
      e= = ==== 6^=== w-
      4= 7 2==1 4^=== e're
      o= = ==== 2v=== both
      u= 5 ===4 6^=== sh-
      3= 4 ===3 4^=== o-
      e= = ==== 2v=== w-
      4= 2 ===2 4v=== ing
      oe = ==== 6^2== hearts"""), 207.59, 215.01
    ),
    Phrase("risk", parse_violin_notes("""
      1= 9 11W1 2v=LM ris-
      u= 7 2==4 6^=== king
      3= 5 ===3 5^=== it
      o= Y 1==2 2v=== a-
      1= 0 ===3 3v=== ll
      u= Y ===2 6^=== th-
      3= 9 ===1 5^=== ough
      e= = ==== 2v=== it's
      o3 7 2==4 6^2== hard"""), 215.01, 220.54
    )
  ]),
  Section("church/mirrors", "CA", [
    Phrase("all-me", parse_violin_notes("""
      o= 4 21W2 4^=LM cause
      1= = ==== 2v=== a-
      b= 7 ===4 3v=== a-
      3= = ==== 6^=== ll
      4= 4 ===2 2v=== of
      o= 7 ===4 5^=== m-
      12 9 1==1 2v4== e"""), 220.54, 223.52
    ),
    Phrase("all-you", parse_violin_notes("""
      3= 4 21W3 4^=LM loves
      1= 2 ===2 2v=== all
      4= 0 3=C4 6^=== of
      o= 2 2=W3 4v=== y-
      12 4 ==== 5v6== ou"""), 223.52, 227.34
    )
    #Phrase("curves", clone("end", "love you-r curves and all your ed-ges .", 227.34)
    #Phrase("imperfections", clone("end", "all you-r per-fect im-per-fec-tions .", 231.31)
  ]),
  Section("church/sepulchre", "CB", [
    Phrase("give-your", parse_violin_notes("""
      3= 4 21W2 3v=LM give
      e= = ==== 5^=== your
      1= = ==== 3v=== a-
      b= 7 ===4 4v=== ll
      4= 4 ===2 7^=== to
      o= 7 ===4 6^=== m-
      12 9 1==1 3v6== e"""), 235.15, 238.65
    ),
    Phrase("give-my^", parse_violin_notes("""
      u= 4 21W2 6^=LM i'll
      3= 0 1==3 3v=== give
      e= Y ===2 5^=== m-
      o= 9 ===1 4^=== y
      1= = ==== 3v=== all
      4= 7 2==4 7^=== to
      o2 4 ===2 3v5== you"""), 238.65, 242.60
    ),
    Phrase("end", parse_violin_notes("""
      3= 4 21W2 5v=LM you're
      e= = ==== 6^=== m-
      o= 2 ===1 5^=== y
      1= = ==== 3v=== end
      2= = ==== 5^=== and
      3= = ==== 3v=== my
      4= 0 3=C4 5^=== be-
      o= 2 2=W1 4^=== gin-
      12 9 3=C2 3v5== ning"""), 242.60, 246.55
    )
    #Phrase("lose", clone("end", "e-ve-n when i lose i'm win-ning ."), 246.55)
  ]),
  Section("altar", "O", [
    #Phrase("i-give", clone("you-give", "cause i give you a-u-i-a-a-ll , of me ."), 250.20)
    #Phrase("you-give", clone(), 257.77)
  ]),
  Section("altar", "O", [
    Phrase("auaua", parse_violin_notes("""
      3= 4 21W2 7^=LM i
      e= 5 ===3 6^=== give
      4= 7 ===4 4^=== you
      o= 0 1==3 2v=== a-
      2= 2 ===4 4v=== u-
      u= Y ===2 6^=== a-
      4= 0 ===3 4^=== u-
      o= 9 ===1 2v=== a-
      u3 7 2==4 5v=== ll
      4= 4 ===2 7^=== of
      o3 = ==== 4v6== me"""), 265.26, 273.04
    ),
    Phrase("you-give", parse_violin_notes("""
      u= 4 21W2 6v=LM and
      3= = ==== 7^=== you
      e= 5 ===3 6^=== give
      4= 7 ===4 4^=== me
      o= 0 1==3 2v=== a-
      u= Y ===2 6^=== u-
      p= 0 ===3 5^=== i-
      3= Y ===2 4^=== a-
      o= 9 ===1 2v=== a-
      u3 7 2==4 5v=== ll
      4= 4 ===2 7^=== of
      ou = ==== 4v6== you"""), 273.04, 279.42
    ),
    Phrase("ouo", parse_violin_notes("""
      4= 2 21W1 6^=LM o-
      o= 4 ===2 5^=== u-
      14 2 ===1 4^1== oh"""), 279.42, 282.03
    )
  ])
], "63.all-of-me.mp3"))

