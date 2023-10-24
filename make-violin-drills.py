#!/usr/bin/env python3

import os
from violin import *

def locate(mp3):
 return os.environ['HOME'] + "/work/music/chunking/violin/" + mp3

goal("warmup")
make_drone("49")
finger_stretches()
jellyfish()
itsy_bitsy_spider()

goal("the-crawl", 90, locate("1001.the-crawl.mp3"))
for tempo in [45, 90]:
  piece(tempo, "the-crawl",
    phrase(tempo, "little baby crawls to danger (scared)", "443322112", start=10.16, stop=15.38),
    phrase(tempo, "scared he turns round in a circle", "22332233", start=15.38, stop=21.53)
  )

goal("baby-steps", 90, locate("1002.baby-steps.mp3"))
for tempo in [45, 90]:
  piece(tempo, "baby-steps",
    phrase(tempo, "left foot step (right)", "4432", "QQHQ", start=10.30, stop=13.05),
    phrase(tempo, "right foot step (looks)", "2232", "QQHQ", "UDUD", start=13.05, stop=15.67),
    phrase(tempo, "looks for mummy (fall)", "22112", start=15.67, stop=18.30),
    phrase(tempo, "falling down", "234", start=18.30, stop=21.75)
  )

goal("the-car-trip", 110, locate("1003.the-car-trip.mp3"))
for tempo in [55, 110]:
  piece(tempo, "the-car-trip",
    phrase(tempo, "little baby throwing up (mummy)", "11223323", "QQQQQQHQ", start=9.72, stop=12.04),
    phrase(tempo, "mummy wants to throw up too (pull)", "33443321", "QQQQQQHQ", "UDUDUDUD", start=12.04, stop=14.22),
    phrase(tempo, "pulling over (clean)", "12343", start=14.22, stop=16.52),
    phrase(tempo, "clean it up", "332", "QQH", start=16.52, stop=19.46)
  )

goal("aeroplane-games", 110, locate("1004.aeroplane-games.mp3"))
for tempo in [55, 110]:
  piece(tempo, "aeroplane-games",
    phrase(tempo, "flying upwards flying downwards (land)", "432112343", "EEEEEEEEE", start=9.59, stop=12.06),
    phrase(tempo, "landing at the terminal", "3322112", "EEEEEEE", start=14.24, stop=17.01)
  )

#goal("first-finger-etudes")
#fret_hitting(2, 2)

#goal("second-finger-etudes")
#fret_hitting(4, 2)

#goal("third-and-fourth-finger-etudes")
#fret_hitting(5, 3)
#fret_hitting(7, 4)

goal("lightly-row", 90, locate("1024.lightly-row.mp3"))
for tempo in [45, 90]:
  piece(tempo, "lightly-row",
    phrase(tempo, "lightly row, flamingo", "222222", "QQHQQH", frets="744522", fingers="422311", handshapes="WWWWWW", start=6.92, stop=10.52),
    phrase(tempo, "down the river we will go", "2222222", "QQQQQQH", frets="0245777", fingers="0123444", handshapes="WWWWWWW", start=10.52, stop=14.12),
    phrase(tempo, "always rowing, never slowing", "22222222", "QQQQQQQQ", frets="74445222", fingers="42223111", handshapes="WWWWWWWW", start=14.12, stop=17.60),
    phrase(tempo, "in my bright new red canoe", "2222222", "QQQQQQH", frets="0477444", fingers="0244222", handshapes="WWWWWWW", start=17.60, stop=21.23),
    phrase(tempo, "see the fishes swimming by", "2222222", "QQQQQQH", frets="2222245", fingers="1111123", handshapes="WWWWWWW", start=21.23, stop=24.85),
    phrase(tempo, "see the birds up in the sky", "2222222", "QQQQQQH", frets="4444457", fingers="2222234", handshapes="WWWWWWW", start=24.85, stop=28.58)
  )

