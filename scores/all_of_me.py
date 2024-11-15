# vim: foldmethod=marker foldmarker=##,#. foldtext=getline(v\:foldstart)

import sys; sys.path.append("..")
from violin import *

meter=4; tempo=126; tonic=48

phrases   = [("what would i do with-o-ut your smart mouth? .", 23.51)] ##1
index     = "wwi|dwouys|m."
rhythm    = "3e4|1a2u34|12"
degrees   = "24=|==24=0|=."
fingers   = "23=|==23=1|=="
strings   = "3==|======|=="
bases     = "6==|======|=="
shapes    = "C==|======|=="
bowing    = "246|242462|62"
attack    = "L==|======|=."
dynamics  = "M==|======|=="

phrases  += [("draw-in me in a you kick-in me a-out .", 27.31)] ##1
index    += "dim|iaykima|o."
rhythm   += "3e4|1a23e4o|12"
degrees  += "24=|=24=20=|9."
fingers  += "23=|=23=21=|3="
strings  += "3==|=======|4="
bases    += "6==|=======|=="
shapes   += "C==|=======|P="
bowing   += "246|2462535|37"
attack   += "L==|=======|=."
dynamics += "M==|=======|=="

phrases  += [("you've got my head spin-nin , no kid-din .", 31.12)] ##1
index    += "ygm|hsn,|nkd."
rhythm   += "u3t|13e4|13e4"
degrees  += "94=|540.|540."
fingers  += "3==|431=|431="
strings  += "43=|====|===="
bases    += "6==|====|===="
shapes   += "PC=|====|===="
bowing   += "767|2747|=153"
attack   += "L==|===.|L==."
dynamics += "M==|====|===="

phrases  += [("i can't , pin yo-u down .", 35.85)] ##1
index    += "i|c,pyu|d."
rhythm   += "o|1u3eo|1u"
degrees  += "0|2.429|=."
fingers  += "1|2=323|=="
strings  += "3|====4|=="
bases    += "6|=====|=="
shapes   += "C|====P|=="
bowing   += "3|26=46|72"
attack   += "L|=.L==|=."
dynamics += "M|=====|==" #.

phrases  += [("what's go-in on in that beau-ti-ful mind? .", 38.95)] ##1
index    += "wgi|oitbtfm|."
rhythm   += "3e4|1a23e4w|2"
degrees  += "24=|=24=20=|."
fingers  += "23=|=23=21=|="
strings  += "3==|=======|="
bases    += "6==|=======|="
shapes   += "C==|=======|="
bowing   += "246|2462535|2"
attack   += "L==|=======|."
dynamics += "M==|=======|="

phrases  += [("i'm on your ma-gi-cal mys-te-ry r-ide .", 42.67)] ##1
index    += "ioy|mgcmtrr|i."
rhythm   += "3e4|1a23e4o|1u"
degrees  += "4==|754=20=|9."
fingers  += "3==|143=21=|3="
strings  += "3==|23=====|4="
bases    += "6==|=======|=="
shapes   += "C==|=======|P="
bowing   += "242|5353535|37"
attack   += "L==|=======|=."
dynamics += "M==|=======|=="

phrases  += [("and i'm so di-zzy , don't kn-ow what hit me .", 46.57)] ##1
index    += "ai|sdz,d|kowhm."
rhythm   += "3e|13e4o|1b23e4"
degrees  += "4=|540.=|45=40."
fingers  += "3=|431==|4==31="
strings  += "3=|=====|======"
bases    += "6=|=====|======"
shapes   += "C=|=====|KC===="
bowing   += "==|=====|======"
attack   += "L=|===.L|=====."
dynamics += "M=|=====|======"

phrases  += [("but i'll be a-l-right .", 51.03, 54.92)]  ##1
index    += "b|ibal|r."
rhythm   += "o|13eo|1e"
degrees  += "0|242=|5."
fingers  += "1|232=|4="
strings  += "3|====|=="
bases    += "6|====|=="
shapes   += "C|====|==" #.

phrases  += [("my h-ead's u-n-de-r-wa-te-r but .", 54.92)] ##1
index    += "m|heundrw|trb."
rhythm   += "o|1bu3e4o|u3e4"
degrees  += "0|7975=4=|20=."
fingers  += "1|1214=3=|21=="
strings  += "3|4==3===|===="
bases    += "6|=======|===="
shapes   += "C|=======|===="

phrases  += [("i'm br-ea-th-in fine .", 58.71)] ##1
index    += "i|betif|."
rhythm   += "o|u3e4o|u"
degrees  += "Y|97=9=|."
fingers  += "4|32=3=|="
strings  += "4|=====|="
bases    += "6|=====|="
shapes   += "P|=====|="

phrases  += [("y-ou're cr-a-zy and i'm o-ut of my mind .", 62.57)] ##1
index    += "yo|cazai|otomm|."
rhythm   += "ow|u3e4o|u3e4o|3"
degrees  += "79|=7=54|=2=02|."
fingers  += "12|=1=43|=2=12|="
strings  += "2=|===3=|=====|="
bases    += "6=|=====|=====|="
shapes   += "C=|=====|=====|=" #.

phrases  += [("cause a-a-ll of m-e .", 68.21)] ##1
index    += "c|aalom|e."
rhythm   += "o|1b34o|12"
degrees  += "4|=7=47|9."
fingers  += "3|=1=31|2="
strings  += "3|=2=32|=="
bases    += "6|=====|=="
shapes   += "C|=====|=="

phrases  += [("loves all of y-ou .", 71.10)] ##1
index    += "l|aoy|u."
rhythm   += "3|14o|12"
degrees  += "4|202|4."
fingers  += "3|213|3="
strings  += "3|===|=="
bases    += "6|==8|6="
shapes   += "C|==N|C="

phrases  += [("love you-r curves and all your ed-ges .", 74.86)] ##1
index    += "lyr|caaye|g."
rhythm   += "3eo|1234o|12"
degrees  += "4=2|===02|9."
fingers  += "3=2|===12|3="
strings  += "3==|=====|4="
bases    += "6==|=====|=="
shapes   += "C==|=====|P="

phrases  += [("all you-r per-fect im-per-fec-tions .", 78.86)] ##1
index    += "ayr|pfipf|t."
rhythm   += "3eo|1234o|12"
degrees  += "4=2|===02|9."
fingers  += "3=2|===12|3="
strings  += "3==|=====|4="
bases    += "6==|=====|=="
shapes   += "C==|=====|P=" #.

phrases  += [("give your a-ll to m-e .", 82.63)] ##1
index    += "gy|altm|e."
rhythm   += "3e|1b4o|12"
degrees  += "4=|=747|9."
fingers  += "3=|=131|2="
strings  += "3=|=232|=="
bases    += "6=|====|=="
shapes   += "C=|====|=="

phrases  += [("i'll give m-y all to yo-u .", 86.35)] ##1
index    += "igmy|aty|u."
rhythm   += "u3eo|14o|12"
degrees  += "2942|=02|4."
fingers  += "2232|=12|3="
strings  += "323=|===|=="
bases    += "6===|===|=="
shapes   += "C===|===|=="

phrases  += [("you're m-y end and my be-gin-ning .", 90.10)] ##1
index    += "ymy|eambg|n."
rhythm   += "3eo|1234o|1a"
degrees  += "4=2|===02|9."
fingers  += "3=2|===12|3="
strings  += "3==|=====|4="
bases    += "6==|=====|=="
shapes   += "C==|=====|P="

phrases  += [("e-ve-n when i lose i'm win-ning .", 94.17)] ##1
index    += "evn|wiliw|n."
rhythm   += "3eo|1234o|1a"
degrees  += "4=2|===02|9."
fingers  += "3=2|===12|3="
strings  += "3==|=====|4="
bases    += "6==|=====|=="
shapes   += "C==|=====|P=" #.

phrases  += [("cause i give you a-u-i-a-a-ll , of me .", 97.70)] ##1
index    += "cigya|uiaa|l,om|.|"
rhythm   += "u3e4o|up3o|u34o|u|"
degrees  += "4=570|Y0Y9|7.4=|.|"
fingers  += "3=414|3432|1=3=|=|"
strings  += "3==2=|====|==3=|=|"
bases    += "6====|====|====|=|"
shapes   += "C====|====|====|=|"

phrases  += [("and you give me a-u-i-a-a-ll , of you .", 105.28)] ##1
index    += "aygma|uiaa|l,oy|."
rhythm   += "u3e4o|up3o|u34o|u"
degrees  += "4=570|Y0Y9|7.4=|."
fingers  += "3=414|3432|1=3=|="
strings  += "3==2=|====|==3=|="
bases    += "6====|====|====|="
shapes   += "C====|====|====|="

phrases  += [("oh-o .", 111.83)] ##1
index    += "oo|."
rhythm   += "4o|3"
degrees  += "42|."
fingers  += "32|="
strings  += "3=|="
bases    += "6=|="
shapes   += "C=|=" #.

phrases  += [("how ma-n-y t-imes do i have to tell you .", 115.05)] ##1
index    += "hmny|tidihtt|y."
rhythm   += "3e4m|1a2u3e4|12"
degrees  += "2424|24=2420|=."
fingers  += "2323|23=2321|=="
strings  += "3===|=======|=="
bases    += "6===|=======|=="
shapes   += "C===|=======|=="

phrases  += [("e-ven when you're c-ry-ing you're beau-ti-ful t-oo .", 118.98)] ##1
index    += "evwy|criybtft|o."
rhythm   += "3e4o|1b2u3e4o|12"
degrees  += "4===|5754=20=|9."
fingers  += "3===|4143=21=|3="
strings  += "3===|=23=====|4="
bases    += "6===|========|=="
shapes   += "C===|========|P="

phrases  += [("the w-orld is bea-t-i-ng you d-own i-m a-round .", 122.55)] ##1
index    += "twoi|btinyd|oimar|."
rhythm   += "u3ct|1up3eo|1ue4o|2"
degrees  += "024=|545404|540=2|."
fingers  += "123=|434313|431=2|="
strings  += "3===|======|=====|="
bases    += "6===|======|=====|="
shapes   += "C===|======|=====|="

phrases  += [("through e-ve-ry mood .", 128.17)] ##1
index    += "tevrm|."
rhythm   += "u3e4o|2"
degrees  += "242=9|."
fingers  += "232=3|="
strings  += "3===4|="
bases    += "6====|="
shapes   += "C===P|=" #.

phrases  += [("you're my down-fall, you're my muse .", 130.19)] ##1
index    += "ymd|fymm|."
rhythm   += "peo|a3eo|a"
degrees  += "74=|0744|."
fingers  += "13=|1=3=|="
strings  += "23=|=23=|="
bases    += "6==|====|="
shapes   += "C==|====|="

phrases  += [("my w-orst dis-tr-ac-tion, my rhy-thm n blues .", 133.97)] ##1
index    += "mwodt|atmrtnb|."
rhythm   += "u3e4o|1au3e4o|2"
degrees  += "0574=|2==4249|."
fingers  += "1413=|2==323=|="
strings  += "3=23=|======4|="
bases    += "6====|=======|="
shapes   += "C====|======P|="

phrases  += [("i can't stop si-ng-ing it's , r-i-ng-ing in .", 137.69)] ##1
index    += "ics|snii,r|inii."
rhythm   += "u3t|1u3e4o|1u3e4"
degrees  += "4==|540=.4|540=."
fingers  += "3==|431==3|431=="
strings  += "3==|======|====="
bases    += "6==|======|====="
shapes   += "C==|======|====="

phrases  += [("my , h-ead for y-ou .", 142.49, 150.28)] ##1
index    += "m|,hefy|o."
rhythm   += "o|2ue4o|14"
degrees  += "2|.42=4|5."
fingers  += "2|=32=4|=="
strings  += "3|=====|=="
bases    += "6|=====|=="
shapes   += "C|====K|C=" #.

phrases  += [("i'll give m-y all to you .", 178.75, 181.63)] ##1
index    += "igmy|aty|."
rhythm   += "u3eo|14o|2"
degrees  += "40Y9|=74|."
fingers  += "3432|=13|="
strings  += "32==|==3|="
bases    += "6===|===|="
shapes   += "C===|===|=" #.

phrases  += [("give me a-ll of you o-u-o-u-oh .", 204.06)] ##1
index    += "gmaloy|ououo|.|"
rhythm   += "a2u3e4|up3ce|1|"
degrees  += "57Y0Y9|75420|.|"
fingers  += "413432|14321|=|"
strings  += "32====|=3===|=|"
bases    += "6=====|=====|=|"
shapes   += "C=====|=====|=|"

phrases  += [("cards o-n the t-a-b-le, w-e're both sh-o-w-ing hearts .", 207.59)] ##1
index    += "contt|ablweb|sowih|."
rhythm   += "1u3eo|1u3e4o|u3e4o|e"
degrees  += "975=Y|0Y9=7=|54=2=|."
fingers  += "214=3|432=1=|43=2=|="
strings  += "2=3=2|======|3====|="
bases    += "6====|======|=====|="
shapes   += "C====|======|=====|="

phrases  += [("ris-king it a-ll, th-ough it's hard .", 215.01, 220.54)] ##1
index    += "|rkia|ltoih|."
rhythm   += "|1u3o|1u3eo|3"
degrees  += "|975Y|0Y9=7|."
fingers  += "|2143|432=1|="
strings  += "|2=32|=====|="
bases    += "|6===|=====|="
shapes   += "|C===|=====|=" #.

phrases  += [("i give you a-u-a-u-a-ll , of me .", 265.26)] ##1
index    += "igya|uaua|l,om|."
rhythm   += "3e4o|2u4o|u34o|3"
degrees  += "4570|2Y09|7.4=|."
fingers  += "3414|1342|1=3=|="
strings  += "3=2=|12==|==3=|="
bases    += "6===|====|====|="
shapes   += "C===|NC==|====|="

phrases  += [("o-u-oh .", 279.42, 282.03)] ##1
index    += "ou|o."
rhythm   += "4o|14"
degrees  += "24|2."
fingers  += "23|2="
strings  += "3=|=="
bases    += "6=|=="
shapes   += "C=|==" #.

piece(63, "all-of-me", locate("63.all-of-me.mp3"), tempo, phrases, index, rhythm,
    strings, bowing, shapes, bases, fingers, attack, dynamics)

