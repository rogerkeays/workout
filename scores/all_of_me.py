# vim: foldmethod=marker foldmarker=\ \ Phrase,\ ) foldtext=getline(v\:foldstart)

import sys; sys.path.append("..")
from violin import *

def parse_violin_notesx(text: str): return []

process_piece(Piece("all-of-me", 4, 126, "48", [
  Section("art-desk", "V1", [
    Phrase("mouth", parse_violin_notesx("""
      phrases  += [("what would i do with-o-ut your smart mouth? .", 23.51)]
      index    += "wwi dwouys m."
      rhythm   += "3e4 1a2u34 12"
      degrees  += "24= ==24=0 =."
      fingers  += "23= ==23=1 =="
      strings  += "3== ====== =="
      bases    += "6== ====== =="
      shapes   += "C== ====== =="
      bowing   += "246 246426 26"
      attack   += "L== ====== =."
      dynamics += "M== ====== ==" """), 23.51, 27.31
    ),
    Phrase("drawin'", parse_violin_notesx("""
      phrases  += [("draw-in me in a you kick-in me a-out .", 27.31)] ##1
      index    += "dim iaykima o."
      rhythm   += "3e4 1a23e4o 12"
      bowing   += "246 2462464 26"
      degrees  += "24= =24=20= 9."
      fingers  += "23= =23=21= 3="
      strings  += "3== ======= 4="
      bases    += "6== ======= =="
      shapes   += "C== ======= P="
      attack   += "L== ======= =."
      dynamics += "M== ======= ==" """), 27.31, 31.12
    ),
    Phrase("spinnin'", parse_violin_notesx("""
      phrases  += [("you've got my head spin-nin , no kid-din .", 31.12)] ##1
      index    += "ygm hsn, nkd."
      rhythm   += "u3t 13e4 13e4"
      degrees  += "94= 540. 540."
      fingers  += "3== 431= 431="
      strings  += "43= ==== ===="
      bases    += "6== ==== ===="
      shapes   += "PC= ==== ===="
      bowing   += "767 2747 =153"
      attack   += "L== ===. L==."
      dynamics += "M== ==== ====" """), 31.12, 35.85
    ),
    Phrase("pin", parse_violin_notesx("""
      phrases  += [("i can't , pin yo-u down .", 35.85)] ##1
      index    += "i c,pyu d."
      rhythm   += "o 1u3eo 1u"
      degrees  += "0 2.429 =."
      fingers  += "1 2=323 =="
      strings  += "3 ====4 =="
      bases    += "6 ===== =="
      shapes   += "C ====P =="
      bowing   += "3 26=46 72"
      attack   += "L =.L== =."
      dynamics += "M ===== ==" """), 35.85, 38.95
    )
  ]),
  Section("disneyland", "V2", [
    Phrase("mind", parse_violin_notesx("""
      phrases  += [("what's go-in on in that beau-ti-ful mind? .", 38.95)] ##1
      index    += "wgi oitbtfm ."
      rhythm   += "3e4 1a23e4w 2"
      degrees  += "24= =24=20= ."
      fingers  += "23= =23=21= ="
      strings  += "3== ======= ="
      bases    += "6== ======= ="
      shapes   += "C== ======= ="
      bowing   += "246 2462535 2"
      attack   += "L== ======= ."
      dynamics += "M== ======= =" """), 38.95, 42.67
    ),
    Phrase("ride", parse_violin_notesx("""
      phrases  += [("i'm on your ma-gi-cal mys-te-ry r-ide .", 42.67)] ##1
      index    += "ioy mgcmtrr i."
      rhythm   += "3e4 1a23e4o 1u"
      degrees  += "4== 754=20= 9."
      fingers  += "3== 143=21= 3="
      strings  += "3== 23===== 4="
      bases    += "6== ======= =="
      shapes   += "C== ======= P="
      bowing   += "242 5353535 37"
      attack   += "L== ======= =."
      dynamics += "M== ======= ==" """), 42.67, 46.57
    ),
    Phrase("dizzy", parse_violin_notesx("""
      phrases  += [("and i'm so di-zzy , don't kn-ow what hit me .", 46.57)] ##1
      index    += "ai sdz,d kowhm."
      rhythm   += "3e 13e4o 1b23e4"
      degrees  += "4= 540.= 45=40."
      fingers  += "3= 431== 4==31="
      strings  += "3= ===== ======"
      bases    += "6= ===== ======"
      shapes   += "C= ===== KC===="
      bowing   += "== ===== ======"
      attack   += "L= ===.L =====."
      dynamics += "M= ===== ======" """), 46.57, 51.03
    ),
    Phrase("alright", parse_violin_notesx("""
      phrases  += [("but i'll be a-l-right .", 51.03, 54.92)]  ##1
      index    += "b ibal r."
      rhythm   += "o 13eo 1e"
      degrees  += "0 242= 5."
      fingers  += "1 232= 4="
      strings  += "3 ==== =="
      bases    += "6 ==== =="
      shapes   += "C ==== ==" #."""), 51.03, 54.92
    )
  ]),
  Section("show", "B", [
    Phrase("underwater", parse_violin_notesx("""
      phrases  += [("my h-ead's u-n-de-r-wa-te-r but .", 54.92)] ##1
      index    += "m heundrw trb."
      rhythm   += "o 1bu3e4o u3e4"
      degrees  += "0 7975=4= 20=."
      fingers  += "1 1214=3= 21=="
      strings  += "3 4==3=== ===="
      bases    += "6 ======= ===="
      shapes   += "C ======= ====" """), 54.92, 58.71
    ),
    Phrase("breathin'", parse_violin_notesx("""
      phrases  += [("i'm br-ea-th-in fine .", 58.71)] ##1
      index    += "i betif ."
      rhythm   += "o u3e4o u"
      degrees  += "Y 97=9= ."
      fingers  += "4 32=3= ="
      strings  += "4 ===== ="
      bases    += "6 ===== ="
      shapes   += "P ===== =" """), 58.71, 62.57
    ),
    Phrase("crazy'", parse_violin_notesx("""
      phrases  += [("y-ou're cr-a-zy and i'm o-ut of my mind .", 62.57)] ##1
      index    += "yo cazai otomm ."
      rhythm   += "ow u3e4o u3e4o 3"
      degrees  += "79 =7=54 =2=02 ."
      fingers  += "12 =1=43 =2=12 ="
      strings  += "2= ===3= ===== ="
      bases    += "6= ===== ===== ="
      shapes   += "C= ===== ===== =" #. """), 62.57, 68.21
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
    Phrase("oo", parse_violin_notesx("""
      phrases  += [("oh-o .", 111.83)] ##1 :oo
      index    += "oo ."
      rhythm   += "4o 3"
      degrees  += "42 ."
      fingers  += "32 ="
      strings  += "3= ="
      bases    += "6= ="
      shapes   += "C= =" #. """), 111.83, 115.05
    )
  ]),
  Section("bedroom", "V3", [
    Phrase("times", parse_violin_notesx("""
      phrases  += [("how ma-n-y t-imes do i have to tell you .", 115.05)] ##1
      index    += "hmny tidihtt y."
      rhythm   += "3e4m 1a2u3e4 12"
      degrees  += "2424 24=2420 =."
      fingers  += "2323 23=2321 =="
      strings  += "3=== ======= =="
      bases    += "6=== ======= =="
      shapes   += "C=== ======= ==" """), 115.05, 118.98
    ),
    Phrase("crying", parse_violin_notesx("""
      phrases  += [("e-ven when you're c-ry-ing you're beau-ti-ful t-oo .", 118.98)] ##1
      index    += "evwy criybtft o."
      rhythm   += "3e4o 1b2u3e4o 12"
      degrees  += "4=== 5754=20= 9."
      fingers  += "3=== 4143=21= 3="
      strings  += "3=== =23===== 4="
      bases    += "6=== ======== =="
      shapes   += "C=== ======== P=" """), 118.98, 122.55
    ),
    Phrase("beating", parse_violin_notesx("""
      phrases  += [("the w-orld is bea-t-i-ng you d-own i-m a-round .", 122.55)] ##1
      index    += "twoi btinyd oimar ."
      rhythm   += "u3ct 1up3eo 1ue4o 2"
      degrees  += "024= 545404 540=2 ."
      fingers  += "123= 434313 431=2 ="
      strings  += "3=== ====== ===== ="
      bases    += "6=== ====== ===== ="
      shapes   += "C=== ====== ===== =" """), 122.55, 128.17
    ),
    Phrase("mood", parse_violin_notesx("""
      phrases  += [("through e-ve-ry mood .", 128.17)] ##1
      index    += "tevrm ."
      rhythm   += "u3e4o 2"
      degrees  += "242=9 ."
      fingers  += "232=3 ="
      strings  += "3===4 ="
      bases    += "6==== ="
      shapes   += "C===P =" #. """), 128.17, 130.19
    )
  ]),
  Section("garage", "V4", [
    Phrase("downfall", parse_violin_notesx("""
      phrases  += [("you're my down-fall, you're my muse .", 130.19)] ##1
      index    += "ymd fymm ."
      rhythm   += "peo a3eo a"
      degrees  += "74= 0744 ."
      fingers  += "13= 1=3= ="
      strings  += "23= =23= ="
      bases    += "6== ==== ="
      shapes   += "C== ==== =" """), 130.19, 133.97
    ),
    Phrase("distraction", parse_violin_notesx("""
      phrases  += [("my w-orst dis-tr-ac-tion, my rhy-thm n blues .", 133.97)] ##1
      index    += "mwodt atmrtnb ."
      rhythm   += "u3e4o 1au3e4o 2"
      degrees  += "0574= 2==4249 ."
      fingers  += "1413= 2==323= ="
      strings  += "3=23= ======4 ="
      bases    += "6==== ======= ="
      shapes   += "C==== ======P =" """), 133.97, 137.69
    ),
    Phrase("singing", parse_violin_notesx("""
      phrases  += [("i can't stop si-ng-ing it's , r-i-ng-ing in .", 137.69)] ##1
      index    += "ics snii,r inii."
      rhythm   += "u3t 1u3e4o 1u3e4"
      degrees  += "4== 540=.4 540=."
      fingers  += "3== 431==3 431=="
      strings  += "3== ====== ====="
      bases    += "6== ====== ====="
      shapes   += "C== ====== =====" """), 137.69, 142.49
    ),
    Phrase("head", parse_violin_notesx("""
      phrases  += [("my , h-ead for y-ou .", 142.49, 150.28)] ##1
      index    += "m ,hefy o."
      rhythm   += "o 2ue4o 14"
      degrees  += "2 .42=4 5."
      fingers  += "2 =32=4 =="
      strings  += "3 ===== =="
      bases    += "6 ===== =="
      shapes   += "C ====K C=" #. """), 142.49, 150.28
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
    Phrase("give-my", parse_violin_notesx("""
      phrases  += [("i'll give m-y all to yo-u .", 162.63)] ##1 :_give-my
      index    += "igmy aty u."
      rhythm   += "u3eo 14o 12"
      degrees  += "2942 =02 4."
      fingers  += "1121 =41 2="
      strings  += "212= =32 =="
      bases    += "1=== === =="
      shapes   += "W=== =CW =="
      bowing   += "6354 376 35"
      attack   += "L=== === =."
      dynamics += "V=== === ==" """),  177.75, 181.63
    )
    #Phrase("end", clone(), 181.63)
    #Phrase("lose", clone(), 185.64)
  ]),
  Section("altar", "O", [
    #Phrase("i-give", clone(), 189.20)
    #Phrase("you-give", clone(), 196.79)
  ]),
  ###
  Section("casino", "M", [
    Phrase("give-me", parse_violin_notes("""
      a= 5 21W3 3=LM give
      2= 7 ===4 5=== me
      u= Y 1==2 3=== a-
      3= 0 ===3 4=== ll
      e= Y ===2 5=== of
      4= 9 ===1 3=== you
      u= 7 2==4 6=== o-
      p= 5 ===3 5=== u-
      3= 4 ===2 3=== o-
      c= 2 ===1 3=== u-
      e1 0 1==4 21== oh"""), 204.06, 207.59
    ),
    Phrase("cards", parse_violin_notes("""
      1= 9 11W2 3=LM cards
      u= 7 2==1 5=== o-
      3= 5 ===4 4=== n
      e= = ==== 3=== the
      o= Y 1==3 6=== t-
      1= 0 ===4 4=== a-
      u= Y ===3 2=== b-
      3= 9 ===2 4=== le
      e= = ==== 6=== w-
      4= 7 2==1 4=== e're
      o= = ==== 2=== both
      u= 5 ===4 6=== sh-
      3= 4 ===3 4=== o-
      e= = ==== 2=== w-
      4= 2 ===2 4=== ing
      oe = ==== 62== hearts"""), 207.59, 215.01
    ),
    Phrase("risk", parse_violin_notes("""
      1= 9 11W1 2=LM ris-
      u= 7 2==4 6=== king
      3= 5 ===3 5=== it
      o= Y 1==2 2=== a-
      1= 0 ===3 3=== ll
      u= Y ===2 6=== th-
      3= 9 ===1 5=== ough
      e= = ==== 2=== it's
      o3 7 2==4 62== hard"""), 215.01, 220.54
    )
  ]),
  Section("church/mirrors", "CA", [
    Phrase("all-me", parse_violin_notes("""
      o= 4 21W2 4=LM cause
      1= = ==== 2=== a-
      b= 7 ===4 3=== a-
      3= = ==== 6=== ll
      4= 4 ===2 2=== of
      o= 7 ===4 5=== m-
      12 9 1==1 24== e"""), 220.54, 223.52
    ),
    Phrase("all-you", parse_violin_notes("""
      3= 4 21W3 4=LM loves
      1= 2 ===2 2=== all
      4= 0 1=C1 6=== of
      o= 2 2=W3 4=== y-
      12 4 ==== 56== ou"""), 223.52, 227.34
    )
    #Phrase("curves", clone("end", "love you-r curves and all your ed-ges .", 227.34)
    #Phrase("imperfections", clone("end", "all you-r per-fect im-per-fec-tions .", 231.31)
  ]),
  Section("church/sepulchre", "CB", [
    Phrase("give-your", parse_violin_notes("""
      3= 4 21W2 3=LM give
      e= = ==== 5=== your
      1= = ==== 3=== a-
      b= 7 ===4 4=== ll
      4= 4 ===2 7=== to
      o= 7 ===4 6=== m-
      12 9 1==1 36== e"""), 235.15, 238.65
    ),
    Phrase("give-my^", parse_violin_notes("""
      u= 4 21W2 6=LM i'll
      3= 0 1==3 3=== give
      e= Y ===2 5=== m-
      o= 9 ===1 4=== y
      1= = ==== 3=== all
      4= 7 2==4 7=== to
      o2 4 ===2 35== you"""), 238.65, 242.60
    ),
    Phrase("end", parse_violin_notes("""
      3= 4 21W2 5=LM you're
      e= = ==== 6=== m-
      o= 2 ===1 5=== y
      1= = ==== 3=== end
      2= = ==== 5=== and
      3= = ==== 3=== my
      4= 0 3=C4 5=== be-
      o= 2 2=W1 4=== gin-
      12 9 3=C2 35== ning"""), 242.60, 246.55
    )
    #Phrase("lose", clone("end", "e-ve-n when i lose i'm win-ning ."), 246.55)
  ]),
  Section("altar", "O", [
    #Phrase("i-give", clone("you-give", "cause i give you a-u-i-a-a-ll , of me ."), 250.20)
    #Phrase("you-give", clone(), 257.77)
  ]),
  Section("altar", "O", [
    Phrase("auaua", parse_violin_notes("""
      3= 4 21W2 7=LM i
      e= 5 ===3 6=== give
      4= 7 ===4 4=== you
      o= 0 1==3 2=== a-
      2= 2 ===4 4=== u-
      u= Y ===2 6=== a-
      4= 0 ===3 4=== u-
      o= 9 ===1 2=== a-
      u3 7 2==4 5=== ll
      4= 4 ===2 7=== of
      o3 = ==== 46== me"""), 265.26, 273.04
    ),
    Phrase("you-give", parse_violin_notes("""
      u= 4 21W2 6=LM and
      3= = ==== 7=== you
      e= 5 ===3 6=== give
      4= 7 ===4 4=== me
      o= 0 1==3 2=== a-
      u= Y ===2 6=== u-
      p= 0 ===3 5=== i-
      3= Y ===2 4=== a-
      o= 9 ===1 2=== a-
      u3 7 2==4 5=== ll
      4= 4 ===2 7=== of
      ou = ==== 46== you"""), 273.04, 279.42
    ),
    Phrase("ouo", parse_violin_notes("""
      4= 2 21W1 6=LM o-
      o= 4 ===2 5=== u-
      14 2 ===1 41== oh"""), 279.42, 282.03
    )
  ])
], "63.all-of-me.mp3"))

