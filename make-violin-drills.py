#!/usr/bin/env python3
# vim: nowrap

import os
from violin import *

def locate(mp3):
 return os.environ['HOME'] + "/library/repertoire/violin/" + mp3

goal("warmup")
make_drone("49")
finger_stretches()
pinky_reaches()
jellyfish()
itsy_bitsy_spider()
son_file()

goal("lightly-row", 90, locate("00.27.lightly-row.mp3"))
for tempo in [45, 90]:
  piece(tempo, "lightly-row",
    phrase(tempo, "lightly row, flamingo", "QQHQQH", "122222", "NWWWWW", "2", "022311", start=6.92, stop=10.52),
    phrase(tempo, "down the river we will go", "QQQQQQH", "2222111", "WWWWNNN", "2", "0123000", start=10.52, stop=14.12),
    phrase(tempo, "always rowing, never slowing", "QQQQQQQQ", "12222222", "NWWWWWWW", "2", "02223111", "UD", start=14.12, stop=17.60),
    phrase(tempo, "in my bright new red canoe", "QQQQQQH", "2211222", "WWNNWWW", "2", "0200222", "UD", start=17.60, stop=21.23),
    phrase(tempo, "see the fishes swimming by", "QQQQQQH", "2", "W", "2", "1111123", start=21.23, stop=24.85),
  )

goal("ponies", 95, locate("00.34.ponies.mp3"))
for tempo in [95]:
  piece(tempo, "ponies",
    phrase(tempo, "little girls like to draw", "HQh", "3", "G", "2", "044323", start=12.68, stop=20.28),
    phrase(tempo, "all the pretty little ponies", "HQqEEEhh", "22233333", "PPPGGGGG", "11122222", "24032100", start=20.28, stop=27.69),
    phrase(tempo, "in her dreams, she walks among", "HQhQQQh", "4443333", "G", "2", "1330022", "DUDUDDU", start=41.61, stop=50.63)
  )

goal("musette", 120, locate("00.35.musette.mp3"))
for tempo in [120]:
  piece(tempo, "musette",
    phrase(lyrics  = "i'm going fishing, i'm going fishing",
           rhythm  = "HEEEE", # "|ma..ta-i.da-i",
           strings = "3", shapes = "W", bases = "2",
           fingers = "43210", # retake second time
           start = 9.77, stop = 14.07, tempo = tempo),

    phrase(lyrics    = "gonna sit down and choose some tackle",
           rhythm    = "EEQQQQQQQ",
           strings   = "3", shapes = "W", bases = "2",
           fingers   = "234321420",
           direction = "DUDUUDUDU",
           dynamics  = "VVVSSVVVV",
           start = 14.07, stop = 17.87, tempo = tempo),

    phrase(lyrics    = "gonna sit down and choose some bait",
           rhythm    = "EEQQQQQH",
           strings   = "3", shapes = "W", bases = "2",
           fingers   = "23432140",
           direction = "DUDUUDUD",
           dynamics  = "VVVSSVVV",
           start = 21.93, stop = 25.84, tempo = tempo),

    phrase(lyrics    = "here it comes, here it comes, more free food",
           rhythm    = "EEQEEQQQH",
           strings   = "222222111",
           shapes    = "W", bases = "2",
           fingers   = "234234050",
           direction = "", # retake
           dynamics  = "VVVVVSSSV",
           start = 25.84, stop = 29.69, tempo = tempo),

    phrase(lyrics    = "carefully, carefully, steal it",
           rhythm    = "EESEESQQH",
           strings   = "2", shapes = "W", bases = "2",
           fingers   = "234234050",
           direction = "UD",
           dynamics  = "VVSVVSSSV",
           start = 29.69, stop = 33.59, tempo = tempo),

    phrase(lyrics    = "big strike, think it got away",
           rhythm    = "QQEEEEF",
           strings   = "1112223",
           shapes    = "W", bases = "2",
           fingers   = "0502102",
           direction = "UUDUDUD",
           dynamics  = "SSVVVVV",
           start = 37.43, stop = 41.55, tempo = tempo),
  )

