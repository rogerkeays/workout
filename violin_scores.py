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
    lyrics  = "| >li-ttle ba-by | crawls to dan-ger | >scared he turns round | in a cir-cle",
    rhythm  = "|  Q  Q    Q  Q  | Q      Q  Q   Q   |  Q      Q  Q     Q     | Q  Q Q   Q",
    strings = "|  4  4    3  3  | 2      2  1   1   |  2      2  3     3     | 2  2 3   3",
    shapes  = "|  N "
  )

def baby_steps(tempo=90):
  score("baby-steps", locate("02.baby-steps.mp3"), [ 10.30, 13.05, 15.67, 18.30, 21.75 ], tempo,
    lyrics  = "| >left foot step | >right foot step | >looks for mu-mmy | >fall-ing down",
    rhythm  = "|  Q    Q    H    |  Q     Q    H    |  Q     Q   Q  Q   |  Q    Q   H",
    strings = "|  4    4    3    |  2     2    3    |  2     2   1  1   |  2    3   4",
    bowing  = "|  35   3    5    |  3     5    3    |  5     3   5  3   |  5    3   5",
    shapes  = "|  N"
  )

def the_car_trip(tempo=110):
  score("the-car-trip", locate("03.the-car-trip.mp3"), [ 9.72, 12.04, 14.22, 16.52, 19.46 ], tempo,
    lyrics  = "| >li-ttle ba-by | throw-ing up | >mu-mmy wants to | throw up too | >pull-ing o-ver | >clean it up",
    rhythm  = "|  Q  Q    Q  Q  | Q     Q   H  |  Q  Q   Q     Q  | Q     Q  H   |  Q    Q   Q Q   |  Q     Q  H",
    strings = "|  1  1    2  2  | 3     3   2  |  3  3   4     4  | 3     3  2   |  1    2   3 4   |  3     3  2",
    bowing  = "|  35 3    5  3  | 5     3   5  |  3  5   3     5  | 3     5  3   |  5    3   5 3   |  5     3  5",
    shapes  = "|  N"
  )

def aeroplane_games(tempo=110):
  score("aeroplane-games", locate("04.aeroplane-games.mp3"), [ 9.59, 10.82, 12.06, 14.24, 17.01 ], tempo,
    lyrics  = "| >fly-ing up-wards >fly-ing down-wards | >>land-ing at the term-in-al",
    rhythm  = "|  E   E   E  E      E   E   E    E     |   E    E   E  E   E    E  Q",
    strings = "|  4   3   2  1      1   2   3    4     |   3    3   2  2   1    1  2",
    shapes  = "|  N"
  )

def lightly_row(tempo=90):
  lyrics   = "| >light-ly row | fla-min-go | >down the ri-ver | we will go"
  rhythm   = "|  Q     Q  H   | Q   Q   H  |  Q    Q   Q  Q   | Q  Q    H"
  strings  = "|  1     2  2   | 2   2   2  |  2    2   2  2   | 1  1    1"
  bowing   = "|  35    3  5   | 3   5   3  |  5    3   5  3   | 5  3    5"
  shapes   = "|  N     W  W   | W   W   W  |  W    W   W  W   | N  N    N"
  fingers  = "|  0     2  2   | 3   1   1  |  0    1   2  3   | 0  0    0"
  bases    = "|  2"

  lyrics  += "| >al-ways row-ing | ne-ver slow-ing | >in my bright big | red can-oe"
  rhythm  += "|  Q  Q    Q   Q   | Q  Q   Q    Q   |  Q  Q  Q      Q   | Q   Q   H"
  strings += "|  1  2    2   2   | 2  2   2    2   |  2  2  1      1   | 2   2   2"
  bowing  += "|  3  5    3   5   | 3  5   3    5   |  3  5  3      5   | 3   5   3"
  shapes  += "|  N  W    W   W   | W  W   W    W   |  W  W  N      N   | W   W   W"
  fingers += "|  0  2    2   2   | 3  1   1    1   |  0  2  0      0   | 2   2   2"

  lyrics  += "| >see the fish-es | swim-ming by | >see the birds up | in the sky"
  rhythm  += "|  Q   Q   Q    Q  | Q    Q    H  |  Q   Q   Q     Q  | Q   Q   H"
  strings += "|  2   2   2    2  | 2    2    2  |  2   2   2     2  | 2   2   2"
  bowing  += "|  5   3   5    3  | 5    3    5  |  3   5   3     5  | 3   5   3"
  shapes  += "|  W   W   W    W  | W    W    W  |  W   W   W     W  | W   W   W"
  fingers += "|  1   1   1    1  | 1    2    3  |  2   2   2     2  | 2   3   4"

  score("lightly-row", locate("27.lightly-row.mp3"), [ 6.92, 10.52, 14.12, 17.60, 21.23, 24.85, 28.58 ], 
        tempo, lyrics, rhythm, strings, bowing, shapes, bases, fingers)

def ponies(tempo=95):
  goal("ponies", tempo, locate("34.ponies.mp3"))
  piece(tempo, "ponies",
    phrase(tempo, "little girls like to draw", "HQh", "3", "G", "2", "044323", start=12.68, stop=20.28),
    phrase(tempo, "all the pretty little ponies", "HQqEEEhh", "22233333", "PPPGGGGG", "11122222", "24032100", start=20.28, stop=27.69),
    phrase(tempo, "in her dreams, she walks among", "HQhQQQh", "4443333", "G", "2", "1330022", "35353453", start=41.61, stop=50.63)
  )

def musette(tempo=120):
  goal("musette", tempo, locate("35.musette.mp3"))
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
           bowing    = "3535435353",
           dynamics  = "VVVSSVVVV",
           start = 14.07, stop = 17.87, tempo = tempo),

    phrase(lyrics    = "gonna sit down and choose some bait",
           rhythm    = "EEQQQQQH",
           strings   = "3", shapes = "W", bases = "2",
           fingers   = "23432140",
           bowing    = "353543535",
           dynamics  = "VVVSSVVV",
           start = 21.93, stop = 25.84, tempo = tempo),

    phrase(lyrics    = "here it comes, here it comes, more free food",
           rhythm    = "EEQEEQQQH",
           strings   = "222222111",
           shapes    = "W", bases = "2",
           fingers   = "234234050",
           bowing    = "", # retake
           dynamics  = "VVVVVSSSV",
           start = 25.84, stop = 29.69, tempo = tempo),

    phrase(lyrics    = "carefully, carefully, steal it",
           rhythm    = "EESEESQQH",
           strings   = "2", shapes = "W", bases = "2",
           fingers   = "234234050",
           bowing    = "35",
           dynamics  = "VVSVVSSSV",
           start = 29.69, stop = 33.59, tempo = tempo),

    phrase(lyrics    = "big strike, think it got away",
           rhythm    = "QQEEEEH",
           strings   = "1112223",
           shapes    = "W", bases = "2",
           fingers   = "0502102",
           bowing    = "54353535",
           dynamics  = "SSVVVVV",
           start = 37.43, stop = 41.55, tempo = tempo),
  )

