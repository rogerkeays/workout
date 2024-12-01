# vim: nowrap

import os
from violin import *

def the_crawl(meter=4, tempo=90, tonic=37):
  piece(1, "the-crawl", locate("01.the-crawl.mp3"), tempo,
    phrases = [("li-ttle ba-by crawls to dan-ger", 10.16),
               ("scared he turns round in a cir-cle", 15.38, 21.53)],

    index   = "|ltbb|ctdg |shtr|iacc",
    rhythm  = "|1234|1234 |1234|1234",
    strings = "|4=3=|2=1= |2=3=|2=3=",
    shapes  = "|N===|==== |====|===="
  )

def baby_steps(meter=4, tempo=90, tonic=37):
  piece(2, "baby-steps", locate("02.baby-steps.mp3"), tempo,
    phrases = [("left foot step", 10.30),
               ("right foot step", 13.05),
               ("looks for mu-mmy", 15.67),
               ("fall-ing down", 18.30, 21.75)],

    index   = "|lfs |rfs |lfmm |fid",
    rhythm  = "|123 |123 |1234 |123",
    strings = "|4=3 |2=3 |2=1= |234",
    shapes  = "|N== |=== |==== |==="
  )

def the_car_trip(meter=4, tempo=110, tonic=37):
  piece(3, "the-car-trip", locate("03.the-car-trip.mp3"), tempo,
    phrases = [("li-ttle ba-by throw-ing up", 9.72),
               ("mu-mmy wants to throw up too", 12.04),
               ("pull-ing o-ver", 14.22),
               ("clean it up", 16.52, 19.46)],

    index   = "|ltbb|tiu |mmwt|tut |plov|ciu",
    rhythm  = "|1234|123 |1234|123 |1234|123",
    strings = "|1=2=|3=2 |3=4=|3=2 |1234|3=2",
    shapes  = "|N===|=== |====|=== |====|==="
  )

def aeroplane_games(meter=4, tempo=110, tonic=37):
  piece(4, "aeroplane-games", locate("04.aeroplane-games.mp3"), tempo,
    phrases = [("fly-ing up-wards", 9.59),
               ("fly-ing down-wards", 10.82, 12.06),
               ("land-ing at the term-in-al", 14.24, 17.01)],

    index   = "|fidw fiup |ldattmn",
    rhythm  = "|1a2u 3e4o |1a2u3e4",
    strings = "|4321 1234 |3=2=1=2",
    shapes  = "|N=== ==== |======="
  )

def lightly_row(meter=4, tempo=90, tonic=49):
  piece(27, "lightly-row", locate("27.lightly-row.mp3"), tempo,
    phrases = [("light-ly row, fla-min-go", 6.92),
               ("down the ri-ver we will go", 10.52),
               ("al-ways row-ing ne-ver slow-ing", 14.12),
               ("in my bright big red ca-noe", 17.60),
               ("see the fish-es swim-ming by", 21.23),
               ("see the birds up in the sky", 24.85, 28.58)],

    index   = "|llr|fmg |dtrv|wwg |awri|nvsi |imbb|rcn |stfs|smb |stbu|its",
    rhythm  = "|123|123 |1234|123 |1234|1234 |1234|123 |1234|123 |1234|123",
    strings = "|12=|=== |====|1== |=2==|==== |==1=|=== |2===|=== |====|===",
    bowing  ="5|353|535 |3535|353 |5353|5353 |5353|535 |3535|353 |5353|535",
    shapes  = "|NW=|=== |====|N== |=W==|==== |==N=|W== |====|=== |====|===",
    fingers = "|02=|31= |0123|0== |=2==|31== |020=|2== |1===|=23 |2===|=34",
    bases   = "|2==|=== |====|=== |====|==== |====|=== |====|=== |====|==="
  )

def ponies(meter=3, tempo=95, tonic=42):
  piece(34, "ponies", locate("34.ponies.mp3"), tempo,
    phrases = [("li-ttle girls like to draw", 12.68),
               ("all the pre-tty li-ttle po-nies", 20.28, 27.69),
               ("in her dreams she walks a-mong", 41.61, 50.63)],

    index   = "|lt|g|lt|d |at|ptlt|p|n |ih|d|swa|m",
    rhythm  = "|13|1|13|1 |13|1u3e|1|1 |13|1|123|1",
    strings = "|3=|=|==|= |2=|=3==|=|= |4=|=|3==|=",
    bowing  ="5|35|3|53|5 |35|3535|3|5 |35|3|543|5",
    shapes  = "|G=|=|==|= |P=|=G==|=|= |==|=|===|=",
    bases   = "|2=|=|==|= |1=|=2==|=|= |==|=|===|=",
    fingers = "|04|=|32|3 |24|0321|0|0 |13|=|0=2|="
  )

def musette(meter=4, tempo=120, tonic=42):
  piece(35, "musette", locate("35.musette.mp3"), tempo,
    phrases = [("i'm go-ing fish-ing, i'm go-ing fish-ing", 9.77),
               ("go-nna sit down and choose some ta-ckle", 14.07, 17.87),
               ("go-nna sit down and choose some bait .", 21.93),
               ("here it comes, here it comes more free food", 25.84),
               ("care-ful-ly, care-ful-ly ste-al it", 29.69, 33.59),
               ("big strike, think it got a-way", 37.43, 41.55)],

    index   = "|igifi|igifi |gnsda|cstk |gnsda|csb. |hichic|mff |cflcfl|sli |bstiga|w",
    rhythm  = "|13e4o|13e4o |1a234|1234 |1a234|123w |1a23e4|123 |1a23e4|123 |123e4o|1",
    strings = "|3====|===== |=====|==== |=====|==== |2=====|1== |2=====|=== |1==2==|3",
    bowing  ="5|35353|53535 |35345|3535 |35345|3535 |353535|353 |535353|535 |453535|3",
    shapes  = "|W====|===== |=====|==== |=====|==== |======|=== |======|=== |======|=",
    bases   = "|2====|===== |=====|==== |=====|==== |======|=== |======|=== |======|=",
    fingers = "|43210|43210 |23432|1420 |23432|1400 |234234|050 |234234|040 |040210|2",
    attack  = "|D====|===== |==SSS|D=== |==SSS|D==R |D=SD=S|==D |==SD=S|==D |S=D===|="
  )

