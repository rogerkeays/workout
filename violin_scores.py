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

