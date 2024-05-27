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
  score("the-crawl", locate("01.the-crawl.mp3"), [ 10.16, 15.38, 21.53 ], tempo,
    lyrics  = "| >li-ttle ba- by | crawls to dan-ger | >scared he turns round | in a cir-cle ",
    rhythm  = "|  Q   =   =   =  |    =   =   =   =  |    =    =    =    =    | =  =  =  =   ",
    strings = "|  4   =   3   =  |    2   =   1   =  |    2    =    3    =    | 2  =  3  =   ",
    shapes  = "|  N "
  )

def baby_steps(tempo=90):
  score("baby-steps", locate("02.baby-steps.mp3"), [ 10.30, 13.05, 15.67, 18.30, 21.75 ], tempo,
    lyrics  = "| >left foot step | >right foot step | >looks for mu-mmy  | >fall-ing down ",
    rhythm  = "|   Q    =    H   |    Q    =    H   |    Q   =   =   =   |    =   =   H   ",
    strings = "|   4    =    3   |    2    =    3   |    2   =   1   =   |    2   3   4   ",
    bowing  = "|  35    3    5   |    3    5    3   |    5   3   5   3   |    5   3   5   ",
    shapes  = "|   N"
  )

def the_car_trip(tempo=110):
  score("the-car-trip", locate("03.the-car-trip.mp3"), [ 9.72, 12.04, 14.22, 16.52, 19.46 ], tempo,
    lyrics  = "| >li-ttle ba- by | throw-ing up | >mu-mmy wants to | throw up too | >pull-ing o- ver | >clean it up ",
    rhythm  = "|  Q   =   =   =  |   =   =   H  |   Q   =   =   =  |   =   =   H  |   Q   =   =   =  |   =   =   H  ",
    strings = "|  1   =   2   =  |   3   =   2  |   3   =   4   =  |   3   =   2  |   1   2   3   4  |   3   =   2  ",
    bowing  = "| 35   3   5   3  |   5   3   5  |   3   5   3   5  |   3   5   3  |   5   3   5   3  |   5   3   5  ",
    shapes  = "|  N"
  )

def aeroplane_games(tempo=110):
  score("aeroplane-games", locate("04.aeroplane-games.mp3"), [ 9.59, 10.82, 12.06, 14.24, 17.01 ], tempo,
    lyrics  = "| >fly-ing up-wards >fly-ing down-wards | >>land-ing at the term-in-al ",
    rhythm  = "|   E   =   =   =      =   =   =   =    |    =   =   =   =   =   =   Q ",
    strings = "|   4   3   2   1      1   2   3   4    |    3   =   2   =   1   =   2 ",
    shapes  = "|   N"
  )

def lightly_row(tempo=90):
  lyrics   = "| >light-ly row | fla-min- go | >down the ri-ver | we will go "
  rhythm   = "|   Q   =   H   |  Q   =   H  |   Q   =   =   =  |  =   =   H "
  strings  = "|   1   2   =   |  =   =   =  |   =   =   =   =  |  1   =   = "
  bowing   = "|  35   3   5   |  3   5   3  |   5   3   5   3  |  5   3   5 "
  shapes   = "|   N   W   =   |  =   =   =  |   =   =   =   =  |  N   =   = "
  fingers  = "|   0   2   =   |  3   1   =  |   0   1   2   3  |  0   =   = "
  bases    = "|   2"

  lyrics  += "| >al-ways row-ing | ne-ver slow-ing | >in my bright big | red ca- noe "
  rhythm  += "|   Q   =   =   =  |  =   =   =   =  |   =   =   =   =   |  =   =   H  "
  strings += "|   1   2   =   =  |  =   =   =   =  |   =   =   1   =   |  =   =   =  "
  bowing  += "|   3   5   3   5  |  3   5   3   5  |   3   5   3   5   |  3   5   3  "
  shapes  += "|   N   W   =   =  |  =   =   =   =  |   =   =   N   =   |  W   =   =  "
  fingers += "|   0   2   2   2  |  3   1   1   1  |   0   2   0   0   |  2   2   2  "

  lyrics  += "| >see the fish-es | swim-ming by | >see the birds up | in  the sky "
  rhythm  += "|   Q   =   =   =  |   =   =   H  |   Q   =   =   =   |  =   =   H  "
  strings += "|   2   =   =   =  |   =   =   =  |   =   =   =   =   |  =   =   =  "
  bowing  += "|   5   3   5   3  |   5   3   5  |   3   5   3   5   |  3   5   3  "
  shapes  += "|   W   =   =   =  |   =   =   =  |   =   =   =   =   |  =   =   =  "
  fingers += "|   1   =   =   =  |   =   2   3  |   2   =   =   =   |  =   3   4  "

  score("lightly-row", locate("27.lightly-row.mp3"), [ 6.92, 10.52, 14.12, 17.60, 21.23, 24.85, 28.58 ], 
        tempo, lyrics, rhythm, strings, bowing, shapes, bases, fingers)

def ponies(tempo=95):
  lyrics   = "| >li-ttle | girls | like to  | draw | >all the | pre-tty li-ttle | po- | nies "
  rhythm   = "|   H   Q  |   h   |   H   Q  |  h   |   H   Q  |  q   E   =   =  |  h  |  =   "
  strings  = "|   3   =  |   =   |   =   =  |  =   |   2   =  |  =   3   =   =  |  =  |  =   "
  bowing   = "|  35   3  |   5   |   3   5  |  3   |   5   3  |  5   3   5   3  |  5  |  3   "
  shapes   = "|   G   =  |   =   |   =   =  |  =   |   P   =  |  =   G   =   =  |  =  |  =   "
  bases    = "|   2   =  |   =   |   =   =  |  =   |   1   =  |  =   2   =   =  |  =  |  =   "
  fingers  = "|   0   4  |   =   |   3   2  |  3   |   2   4  |  0   3   2   1  |  0  |  0   "

  lyrics  += "| >>in her | dreams | she walks a- | mong "
  rhythm  += "|   H   Q  |   h    |   Q   =   =  |  h   "
  strings += "|   4   =  |   =    |   3   =   =  |  =   "
  bowing  += "|   5   3  |   5    |   3   4   5  |  3   "
  shapes  += "|   G   =  |   =    |   =   =   =  |  =   "
  fingers += "|   1   3  |   =    |   0   =   2  |  =   "

  score("ponies", locate("34.ponies.mp3"), [ 12.68, 20.28, 27.69, 41.61, 50.63 ],
        tempo, lyrics, rhythm, strings, bowing, shapes, bases, fingers)

def musette(tempo=120):
  lyrics   = "| >i'm go-ing fish-ing | i'm go-ing fish-ing | >go-nna sit down and | choose some ta-ckle "
  rhythm   = "|   H   E   =   =   =  |  H   E   =   =   =  |   =   =   Q   =   =  |    =   =   =   =    "
  strings  = "|   3   =   =   =   =  |  =   =   =   =   =  |   =   =   =   =   =  |    =   =   =   =    "
  bowing   = "|  35   3   5   3   5  |  3   5   3   5   3  |   5   3   5   4   3  |    5   3   5   3    "
  shapes   = "|   W "
  bases    = "|   2 "
  fingers  = "|   4   3   2   1   0  |  4   3   2   1   0  |   2   3   4   3   2  |    1   4   2   0    "
  attack   = "|   D   =   =   =   =  |  =   =   =   =   =  |   =   =   S   S   S  |    D   =   =   =    "

  lyrics  += "| >go-nna sit down and | choose some bait .  | >>here it comes, here it comes | more free food "
  rhythm  += "|   E   =   Q   =   =  |    =    =    H   .  |   E    =    Q    E    =    Q   |  =    =    H   "
  strings += "|   3   =   =   =   =  |    =    =    =   =  |   2    =    =    =    =    =   |  1    =    =   "
  bowing  += "|   5   3   5   4   3  |    5    3    5   3  |   5    3    5    3    5    3   |  5    3    5   "
  fingers += "|   2   3   4   3   2  |    1    4    0   -  |   2    3    4    2    3    4   |  0    5    0   "
  attack  += "|   D   =   S   S   S  |    D    =    =   -  |   D    =    S    D    =    S   |  S    =    D   "

  lyrics  += "| >care-ful-ly, care-ful-ly | ste-al it | >>big strike, think it got a- | way "
  rhythm  += "|    E   =   Q   E   =   Q  | =   =   H |    Q    =    E    =    =    = |  W  "
  strings += "|    2   =   =   =   =   =  | =   =   = |    1    =    =    2    =    = |  3  "
  fingers += "|    2   3   4   2   3   4  | 0   5   0 |    0    5    0    2    1    0 |  2  "
  bowing  += "|    3   5   3   5   3   5  | 3   5   3 |    4    3    5    3    5    3 |  5  "
  attack  += "|    D   =   S   D   =   S  | S   =   D |    S    =    D    =    =    = |  =  "

  score("musette", locate("35.musette.mp3"), [ 9.77, 14.07, 17.87, 21.93, 25.84, 29.69, 33.59, 37.43, 41.55 ],
        tempo, lyrics, rhythm, strings, bowing, shapes, bases, fingers, attack)

