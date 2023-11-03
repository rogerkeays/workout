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

goal("lightly-row", 90, locate("1024.lightly-row.mp3"))
for tempo in [45, 90]:
  piece(tempo, "lightly-row",
    phrase(tempo, "lightly row, flamingo", "QQHQQH", "122222", "NWWWWW", "2", "022311", start=6.92, stop=10.52),
    phrase(tempo, "down the river we will go", "QQQQQQH", "2222111", "WWWWNNN", "2", "0123000", start=10.52, stop=14.12),
    phrase(tempo, "always rowing, never slowing", "QQQQQQQQ", "12222222", "NWWWWWWW", "2", "02223111", "UD", start=14.12, stop=17.60),
    phrase(tempo, "in my bright new red canoe", "QQQQQQH", "2211222", "WWNNWWW", "2", "0200222", "UD", start=17.60, stop=21.23),
    phrase(tempo, "see the fishes swimming by", "QQQQQQH", "2", "W", "2", "1111123", start=21.23, stop=24.85),
    phrase(tempo, "see the birds up in the sky", "QQQQQQH", "2222221", "WWWWWWN", "2", "2222230", "UD", start=24.85, stop=28.58)
  )

