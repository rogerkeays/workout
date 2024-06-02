# vim: nowrap

import os
from violin import *

def locate(mp3):
 return os.environ['HOME'] + "/library/workout/violin/04.rehearse/" + mp3

def warmup():
  goal("warmup")
  finger_stretches()
  pinky_reaches()
  jellyfish()
  itsy_bitsy_spider()
  son_file()

def the_crawl(tempo=90):
  score("the-crawl", locate("01.the-crawl.mp3"), tempo,
    phrases = [("li-ttle ba-by crawls to dan-ger", 10.16),
               ("scared he turns round in a cir-cle", 15.38, 21.53)],

    index   = "|ltbb|ctdg|shtr|iacc",
    rhythm  = "|Q===|====|====|====",
    strings = "|4=3=|2=1=|2=3=|2=3=",
    shapes  = "|N===|====|====|===="
  )

def baby_steps(tempo=90):
  score("baby-steps", locate("02.baby-steps.mp3"), tempo,
    phrases = [("left foot step", 10.30),
               ("right foot step", 13.05),
               ("looks for mu-mmy", 15.67),
               ("fall-ing down", 18.30, 21.75)],

    index   = "|lfs|rfs|lfmm|fid",
    rhythm  = "|Q=H|Q=H|Q===|==H",
    strings = "|4=3|2=3|2=1=|234",
    shapes  = "|N==|===|====|==="
  )

def the_car_trip(tempo=110):
  score("the-car-trip", locate("03.the-car-trip.mp3"), tempo,
    phrases = [("li-ttle ba-by throw-ing up", 9.72),
               ("mu-mmy wants to throw up too", 12.04),
               ("pull-ing o-ver", 14.22),
               ("clean it up", 16.52, 19.46)],

    index   = "|ltbb|tiu|mmwt|tut|plov|ciu",
    rhythm  = "|Q===|==H|Q===|==H|Q===|==H",
    strings = "|1=2=|3=2|3=4=|3=2|1234|3=2",
    shapes  = "|N===|===|====|===|====|==="
  )

def aeroplane_games(tempo=110):
  score("aeroplane-games", locate("04.aeroplane-games.mp3"), tempo,
    phrases = [("fly-ing up-wards", 9.59),
               ("fly-ing down-wards", 10.82, 12.06),
               ("land-ing at the term-in-al", 14.24, 17.01)],

    index   = "|fidwfiup|ldattmn",
    rhythm  = "|E=======|======Q",
    strings = "|43211234|3=2=1=2",
    shapes  = "|N=======|======="
  )

def lightly_row(tempo=90):
  score("lightly-row", locate("27.lightly-row.mp3"), tempo,
    phrases = [("light-ly row, fla-min-go", 6.92),
               ("down the ri-ver we will go", 10.52),
               ("al-ways row-ing ne-ver slow-ing", 14.12),
               ("in my bright big red ca-noe", 17.60),
               ("see the fish-es swim-ming by", 21.23),
               ("see the birds up in the sky", 24.85, 28.58)],

    index   = "|llr|fmg|dtrv|wwg|awri|nvsi|imbb|rcn|stfs|smb|stbu|its",
    rhythm  = "|Q=H|Q=H|Q===|==H|Q===|====|====|==H|Q===|==H|Q===|==H",
    strings = "|12=|===|====|1==|=2==|====|==1=|===|2===|===|====|===",
    bowing  ="3|535|353|5353|535|3535|3535|3535|353|5353|535|3535|353",
    shapes  = "|NW=|===|====|N==|=W==|====|==N=|W==|====|===|====|===",
    fingers = "|02=|31=|0123|0==|=2==|31==|020=|2==|1===|=23|2===|=34",
    bases   = "|2==|===|====|===|====|====|====|===|====|===|====|==="
  )

def ponies(tempo=95):
  score("ponies", locate("34.ponies.mp3"), tempo,
    phrases = [("li-ttle girls like to draw", 12.68),
               ("all the pre-tty li-ttle po-nies", 20.28, 27.69),
               ("in her dreams she walks a-mong", 41.61, 50.63)],

    index   = "|lt|g|lt|d|at|ptlt|p|n|ih|d|swa|m",
    rhythm  = "|HQ|h|HQ|h|HQ|qE==|h|=|HQ|h|Q==|h",
    strings = "|3=|=|==|=|2=|=3==|=|=|4=|=|3==|=",
    bowing  ="3|53|5|35|3|53|5353|5|3|53|5|345|3",
    shapes  = "|G=|=|==|=|P=|=G==|=|=|==|=|===|=",
    bases   = "|2=|=|==|=|1=|=2==|=|=|==|=|===|=",
    fingers = "|04|=|32|3|24|0321|0|0|13|=|0=2|="
  )

def musette(tempo=120):
  score("musette", locate("35.musette.mp3"), tempo,
    phrases = [("i'm go-ing fish-ing, i'm go-ing fish-ing", 9.77),
               ("go-nna sit down and choose some ta-ckle", 14.07, 17.87),
               ("go-nna sit down and choose some bait .", 21.93),
               ("here it comes, here it comes more free food", 25.84),
               ("care-ful-ly, care-ful-ly ste-al it", 29.69, 33.59),
               ("big strike, think it got a-way", 37.43, 41.55)],

    index   = "|igifi|igifi|gnsda|cstk|gnsda|csb.|hichic|mff|cflcfl|sli|bstiga|w",
    rhythm  = "|HE===|HE===|==Q==|====|E=Q==|==H0|E=QE=Q|==H|E=QE=Q|==H|Q=E===|W",
    strings = "|3====|=====|=====|====|=====|====|2=====|1==|2=====|===|1==2==|3",
    bowing  ="3|53535|35353|53543|5353|53543|5353|535353|535|353535|353|435353|5",
    shapes  = "|W====|=====|=====|====|=====|====|======|===|======|===|======|=",
    bases   = "|2====|=====|=====|====|=====|====|======|===|======|===|======|=",
    fingers = "|43210|43210|23432|1420|23432|1400|234234|050|234234|040|040210|2",
    attack  = "|D====|=====|==SSS|D===|==SSS|D==R|D=SD=S|==D|==SD=S|==D|S=D===|="
  )

def all_of_me(tempo=126, tonic=48, meter=4):
  phrases  = [("what would i do with-o-ut your smart mouth?", 23.51),
              ("draw-in me in a you kick-in me a-out", 27.31),
              ("you've got my head spin-nin , no kid-din", 31.12),
              ("i can't , pin yo-u down", 35.85)]

  index    = "wwi|dwouys|m. dim|iaykima|o. ygm|hsn,|nkd. i|c,pyu|d. "
  rhythm   = "3e4|1a2u34|12 3e4|1a23e4o|12 u3t|13e4|13e4 o|1u3eo|1u "
  degrees  = "24=|===?=0|0. 24=|=24=20=|9. 94=|540,|540. 0|2,429|=. "
  strings  = "3==|======|=. ===|=======|=. ===|===,|===. =|=,===|=. "
  bases    = "6==|======|=. ===|=======|=. ===|===,|===. =|=,===|=. "
  bowing   ="3535|435435|3. 535|4354353|5. 353|535,|354. 3|5,353|53 "

  phrases += [("what's go-in on in that beau-ti-ful mind?", 38.95),
              ("i'm on your ma-gi-cal my-ste-ry r-ide", 42.67),
              ("and i-m so di-zzy , don't kn-ow what hit me", 46.57),
              ("but i'll be a-l-right", 51.03)]

  index   += "wgi|oitbtfm|. ioy|mgcmsrr|i. aim|sdz,d|kowhm. b|ibal|r. "
  rhythm  += "3e4|1a23e4w|2 3e4|1a23e4o|1u 3em|13e4o|1b23e4 o|13eo|1e "
  degrees += "24=|=24=20=|. 4==|754=20=|9. 4==|540,=|45=40. 0|242?|5. "
  strings += "3==|=======|. ===|=======|=. ===|===,=|=====. =|====|=. "
  bases   += "6==|=======|. ===|=======|=. ===|===,=|=====. =|====|=. "
  bowing  += "535|4354353|. 535|3534535|3. 534|535,3|54354. 3|5432|5. "

  phrases += [("my h-ead's u-n-de-r-wa-te-r but", 54.92),
              ("i'm br-ea-th-in fine", 58.71),
              ("y-ou're c-ra-zy and i'm o-ut of my mind", 62.57)]

  index   += "m|heundrw|trb. i|betif|. yo|crzai|otomm|. "
  rhythm  += "o|1bu3e4o|u3e4 o|u3e4o|u ow|u3e4o|u3e4o|3 "
  degrees += "0|7975=4=|20=. Y|97=9=|. ?9|=7=54|=2=02|. "
  bowing  += "3"

  phrases += [("cause a-a-ll of m-e", 68.21),
              ("loves all of y-ou", 71.10),
              ("love you-r curves and all your ed-ges", 74.86),
              ("all you-r per-fect im-per-fec-tions", 78.86)]

  index   += "c|aalom|e. l|aoy|u. lyr|caaye|g. ayr|pfipf|t. "
  rhythm  += "o|1b34o|12 3|14o|12 3eo|1234o|12 3eo|1234o|12 "
  degrees += "4|7??47|9. 4|202|4. 4=2|===02|9. 4=2|===02|9. "

  phrases += [("give your a-ll to m-e", 82.63),
              ("i'll give m-y all to yo-u", 86.35),
              ("you're m-y end and my be-gin-ning", 90.10),
              ("e-ven when i lose i'm win-ning", 94.17)]

  index   += "gy|altm|e. igmy|aty|u. ymy|eambg|n. ev|wiliw|n. "
  rhythm  += "3e|1b4o|12 u3eo|14o|12 3eo|1234o|1a 3e|1234o|1a "
  degrees += "4=|=749|L. 294?|202|4. 4=2|===02|0. 4=|2==02|9. "

  phrases += [("cause i give you a-u-i-a-a-ll , of me", 97.70),
              ("and you give me a-u-i-a-a-ll , of you", 105.28),
              ("oh-o", 111.83)]

  index   += "cigya|uiaa|l,om|. |aygma|uiaa|l,oy|. oo|. "
  rhythm  += "u3e4o|up3o|u34o|u |u3e4o|up3o|u34o|u 4o|3 "
  degrees += "4=570|L??9|7,4=|. |4=570|L??9|7,4=|. =2|. "

  phrases += [("how ma-n-y t-imes do i have to tell you", 115.05),
              ("e-ven when you're c-ry-ing you're beau-ti-ful t-oo", 118.98),
              ("the w-orld is bea-t-ing you down i-m a-round", 122.55),
              ("through e-ve-ry mood", 128.17)]

  index   += "hmny|tidihtt|y. evwy|criybtft|o. twoi|btiyd|imar|. tevrm|. "
  rhythm  += "3e4m|1a2u3e4|12 3e4o|1b2u3e4o|12 u3ct|1u3eo|ue4o|2 u3e4o|2 "
  degrees += "24=?|=?=2420|=. 4===|754=20=9|?. 0?4=|540=5|40=2|. 242=0|. "

  phrases += [("you're my down-fall, you're my muse", 130.19),
              ("my w-orst dis-tr-ac-tion, my rhy-thm n blues", 133.97),
              ("i can't stop si-ng-ing it's , r-i-ng-ing in", 137.69),
              ("my , h-ead for y-ou", 142.49, 150.28)]

  index   += "ymd|fymm|. mwodt|atmrtnb|. ics|snii,r|inii. m|,hefy|o. "
  rhythm  += "peo|a3eo|a u3e4o|1au3e4o|2 u3t|1u3e4o|1u3e4 o|2ue4o|14 "
  degrees += "74=|0744|. 0574=|2==4249|. 44=|540=,4|540=. 2|,42=4|5. "

  phrases += [("i'll give m-y all to you", 178.75, 181.63)]

  index   += "igmy|aty|. "
  rhythm  += "u3eo|14o|2 "
  degrees += "40Y9|=74|. "

  phrases += [("give me a-ll of you o-u-o-u-oh", 204.06),
              ("cards o-n the t-a-b-le, w-e're both sh-o-w-ing hearts", 207.59),
              ("ris-king it a-ll, th-ough it's hard", 215.01, 220.54)]

  index   += "gmaloy|ououo. |contt|ablweb|sowih|. |rkia|ltoih|. "
  rhythm  += "a2u3e4|up3ce1 |1u3eo|1u3e4o|u3e4o|e |1u3o|1u3eo|3 "
  degrees += "570Y=9|75420. |975=Y|0Y9=7=|54=2=|. |975Y|0Y9=7|. "

  phrases += [("i give you a-u-a-u-a-ll , of me", 265.26),
              ("o-u-oh", 279.42, 282.03)]

  index   += "igya|uaua|l,om|. ou|o. "
  rhythm  += "3e4o|2u4o|u34o|3 4o|14 "
  degrees += "4570|2L09|7,4=|. 24|2. "

