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
    phrase(tempo, "left foot step (right)", "4432", "sshs", start=10.30, stop=13.05),
    phrase(tempo, "right foot step (looks)", "2232", "sshs", "udud", start=13.05, stop=15.67),
    phrase(tempo, "looks for mummy (fall)", "22112", start=15.67, stop=18.30),
    phrase(tempo, "falling down", "234", start=18.30, stop=21.75)
  )

goal("the-car-trip", 110, locate("1003.the-car-trip.mp3"))
for tempo in [55, 110]:
  piece(tempo, "the-car-trip",
    phrase(tempo, "little baby throwing up (mummy)", "11223323", "sssssshs", start=9.72, stop=12.04),
    phrase(tempo, "mummy wants to throw up too (pull)", "33443321", "sssssshs", "udududud", start=12.04, stop=14.22),
    phrase(tempo, "pulling over (clean)", "12343", start=14.22, stop=16.52),
    phrase(tempo, "clean it up", "332", "ssh", start=16.52, stop=19.46)
  )

goal("aeroplane-games", 110, locate("1004.aeroplane-games.mp3"))
for tempo in [55, 110]:
  piece(tempo, "aeroplane-games",
    phrase(tempo, "flying upwards flying downwards (land)", "432112343", "iiiiiiiii", start=9.59, stop=12.06),
    phrase(tempo, "landing at the terminal", "3322112", "iiiiiii", start=14.24, stop=17.01)
  )

#goal("first-finger-etudes")
#fret_hitting(2, 2)

#goal("second-finger-etudes")
#fret_hitting(4, 2)

#goal("third-and-fourth-finger-etudes")
#fret_hitting(5, 3)
#fret_hitting(7, 4)

#goal("lightly-row", 90, locate("1024.lightly-row.mp3"))
#for tempo in [45, 90]:
#  scale_49_major_one_octave(tempo, "m", "detache", "ss")
#  phrase(tempo, "lightly row, flamingo", "sssx sssx", "/744 522", "", 6.92, 10.52)
#  phrase(tempo, "down the river we will go", "ssss sssx", "0245 777", "", 10.52, 14.12)
#  phrase(tempo, "always rowing, never slowing", "ssss ssss", "7444 5222", "", 14.12, 17.60)
#  phrase(tempo, "in my bright new red canoe", "ssss sssx", "0477 444", "", 17.60, 21.23)
#  phrase(tempo, "see the fishes swimming by", "ssss sssx", "2222 245", "", 21.23, 24.85)
#  phrase(tempo, "see the birds up in the sky", "ssss sssx", "4444 457", "", 24.85, 28.58)
#  piece(tempo, "lightly-row")

