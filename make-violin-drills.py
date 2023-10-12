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
    phrase(tempo, "little baby crawls to danger", "ssss ssss", "00 /77 22 99", "", 10.16, 15.38,
      string_crossings(tempo, 4, 3, "m", "elbow", "detache", "ss", "ud"),
      string_crossings(tempo, 3, 2, "m", "elbow", "detache", "ss", "ud"),
      string_crossings(tempo, 2, 1, "m", "elbow", "detache", "ss", "ud"),
      string_crossings(tempo, 1, 2, "m", "elbow", "detache", "ss", "ud"),
    ),
    phrase(tempo, "scared he turns round in a circle", "ssss ssss", "\\22 77 /22 \\77", "", 15.38, 21.53,
      string_crossings(tempo, 2, 3, "m", "elbow", "detache", "ss", "ud"),
      string_crossings(tempo, 3, 2, "m", "elbow", "detache", "ss", "ud"),
    )
  )

goal("baby-steps", 90, locate("1002.baby-steps.mp3"))
for tempo in [45, 90]:
  piece(tempo, "baby-steps",
    phrase(tempo, "left foot step", "sssx", "00/7", "", 10.30, 13.05,
      string_crossings(tempo, 4, 3, "m", "elbow", "detache", "ssx", "ud"),
      string_crossings(tempo, 3, 2, "m", "elbow", "detache", "sxs", "du"),
    ),
    phrase(tempo, "right foot step", "sssx", "/22\\7", "U", 13.05, 15.67,
      string_crossings(tempo, 2, 3, "m", "elbow", "detache", "ssx", "du"),
      string_crossings(tempo, 3, 2, "m", "elbow", "detache", "sxs", "ud"),
    ),
    phrase(tempo, "looks for mummy", "ssss", "/2299", "", 15.67, 18.30,
      string_crossings(tempo, 2, 1, "m", "elbow", "detache", "ss", "ud"),
      string_crossings(tempo, 1, 2, "m", "elbow", "detache", "ss", "ud"),
    ),
    phrase(tempo, "falling down", "sssx", "\\270", "", 18.30, 21.75,
      string_crossings(tempo, 2, 3, "m", "elbow", "detache", "ss", "du"),
      string_crossings(tempo, 3, 4, "m", "elbow", "detache", "ss", "ud"),
    ),
  )

goal("the-car-trip", 110, locate("1003.the-car-trip.mp3"))
for tempo in [55, 110]:
  piece(tempo, "the-car-trip",
    phrase(tempo, "little baby throwing up", "wwws", "/77 \\00 55 /0", "", 9.72, 12.04,
      string_crossings(tempo, 1, 2, "m", "elbow", "detache", "ss", "ud"),
      string_crossings(tempo, 2, 3, "m", "elbow", "detache", "ss", "ud"),
      string_crossings(tempo, 3, 2, "m", "elbow", "detache", "ssx", "ud"),
      string_crossings(tempo, 2, 3, "m", "elbow", "detache", "sxs", "du"),
    ),
    phrase(tempo, "mummy wants to throw up too", "wwws", "\\55 XX /55 0", "", 12.04, 14.22,
      string_crossings(tempo, 3, 4, "m", "elbow", "detache", "ss", "du"),
      string_crossings(tempo, 4, 3, "m", "elbow", "detache", "ss", "du"),
      string_crossings(tempo, 3, 2, "m", "elbow", "detache", "ssx", "du"),
      string_crossings(tempo, 2, 1, "m", "elbow", "detache", "sxs", "ud"),
    ),
    phrase(tempo, "pulling over", "ssss", "/7\\05X", "", 14.22, 16.52,
      string_crossings(tempo, 1, 2, "m", "elbow", "detache", "ss", "du"),
      string_crossings(tempo, 2, 3, "m", "elbow", "detache", "ss", "ud"),
      string_crossings(tempo, 3, 4, "m", "elbow", "detache", "ss", "du"),
      string_crossings(tempo, 4, 3, "m", "elbow", "detache", "ss", "ud"),
    ),
    phrase(tempo, "clean it up", "sssx", "/550", "", 16.52, 19.46,
      string_crossings(tempo, 3, 2, "m", "elbow", "detache", "ss", "ud"),
    ),
  )

goal("aeroplane-games", 110, locate("1004.aeroplane-games.mp3"))
for tempo in [55, 110]:
  single_string_crossings(tempo, "m", "elbow", "detache", "ss")
  phrase(tempo, "flying upwards flying downwards", "wwww", "\\X/507 7\\05X", "", 9.59, 12.06)
  phrase(tempo, "landing at the terminal", "wwws", "/550077\\0", "", 14.24, 17.01)
  piece(tempo, "aeroplane-games")

#goal("first-finger-etudes")
#fret_hitting(2, 2)

#goal("second-finger-etudes")
#fret_hitting(4, 2)

#goal("third-and-fourth-finger-etudes")
#fret_hitting(5, 3)
#fret_hitting(7, 4)

goal("lightly-row", 90, locate("1024.lightly-row.mp3"))
for tempo in [45, 90]:
  scale_49_major_one_octave(tempo, "m", "detache", "ss")
  phrase(tempo, "lightly row, flamingo", "sssx sssx", "/744 522", "", 6.92, 10.52)
  phrase(tempo, "down the river we will go", "ssss sssx", "0245 777", "", 10.52, 14.12)
  phrase(tempo, "always rowing, never slowing", "ssss ssss", "7444 5222", "", 14.12, 17.60)
  phrase(tempo, "in my bright new red canoe", "ssss sssx", "0477 444", "", 17.60, 21.23)
  phrase(tempo, "see the fishes swimming by", "ssss sssx", "2222 245", "", 21.23, 24.85)
  phrase(tempo, "see the birds up in the sky", "ssss sssx", "4444 457", "", 24.85, 28.58)
  piece(tempo, "lightly-row")

