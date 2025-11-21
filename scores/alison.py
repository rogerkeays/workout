# vim: foldmethod=marker foldmarker=phrase,\ ) foldtext=getline(v\:foldstart)

import sys; sys.path.append("..")
from violin import *

process_piece(Piece("the-crawl", 4, 90, "37", [
  Section("table", "V", [
    phrase("crawls", notes("""
      1 0 L4== 40N0 3 li-
      2 = ==== ==== 5 ttle
      3 7 ==== 3=== 3 ba-
      4 = ==== ==== 5 by
      1 2 ==== 2=== 3 crawls
      2 = ==== ==== 5 to
      3 9 ==== 1=== 3 dan-
      4 = ==== ==== 5 ger
      1 Z ==== ==== 3 ."""), 10.16, 15.38
    ),
    phrase("scared", notes("""
      1 2 L4== 20N0 3 scared
      2 = ==== ==== 5 he
      3 7 ==== 3=== 3 turns
      4 = ==== ==== 5 round
      1 2 ==== 2=== 3 in
      2 = ==== ==== 5 a
      3 7 ==== 3=== 3 cir-
      4 = ==== ==== 5 cle
      1 Z ==== ==== 3 ."""), 15.38, 21.53
    ),
  ])
], "01.the-crawl.mp3"))

process_piece(Piece("baby-steps", 4, 90, "37", [
  Section("lawn", "V", [
    phrase("left", notes("""
      1 0 L4== 40N0 3 left
      2 = ==== ==== 5 foot
      3 7 ==== 3=== 3 step
      1 Z ==== ==== 5 ."""), 10.30, 13.05
    ),
    phrase("right", notes("""
      1 2 L4== 20N0 5 right
      2 = ==== ==== 3 foot
      3 0 ==== 3=== 5 step
      1 Z ==== ==== 3 ."""), 13.05, 15.67
    ),
    phrase("mummy", notes("""
      1 2 L4== 20N0 3 looks
      2 = ==== ==== 5 for
      3 7 ==== 1=== 3 mu-
      4 = ==== ==== 5 mmy
      1 Z ==== ==== 3 ."""), 15.67, 18.30
    ),
    phrase("falling", notes("""
      1 2 L4== 20N0 3 fall-
      2 = ==== 3=== 5 ing
      3 7 ==== 4=== 3 down
      1 Z ==== ==== 5 ."""), 18.30, 21.75
    ),
  ])
], "02.baby-steps.mp3"))

process_piece(Piece("the-car-trip", 4, 110, "37", [
  Section("car", "V", [
    phrase("baby", notes("""
      1 9 L4== 10N0 3 li-
      2 = ==== ==== 5 ttle
      3 2 ==== 2=== 3 ba-
      4 = ==== ==== 5 by
      1 7 ==== 3=== 3 throw-
      2 = ==== ==== 5 ing
      3 2 ==== 2=== 3 up
      1 Z ==== ==== 5 ."""), 9.72, 12.04
    ),
    phrase("mummy", notes("""
      1 7 L4== 20N0 5 mu-
      2 = ==== ==== 3 mmy
      3 0 ==== 4=== 5 wants
      4 = ==== ==== 3 to
      1 7 ==== 3=== 5 throw
      2 = ==== ==== 3 up
      3 2 ==== 2=== 5 too
      1 Z ==== ==== 3 ."""), 12.04, 14.22
    ),
    phrase("pull", notes("""
      1 9 L4== 10N0 3 pull-
      2 2 ==== 2=== 5 ling
      3 7 ==== 3=== 3 o
      4 0 ==== 4=== 5 ver
      1 Z ==== ==== 3 ."""), 14.22, 16.52
    ),
    phrase("clean", notes("""
      1 7 L4== 20N0 3 clean
      2 = ==== ==== 5 it
      3 2 ==== 3=== 3 up
      1 Z ==== ==== 5 ."""), 16.52, 19.46
    ),
  ])
], "03.the-car-trip.mp3"))

process_piece(Piece("aeroplane-games", 4, 110, "37", [
  Section("airfield", "V", [
    phrase("upwards", notes("""
      1 0 L4== 40N0 3 fly-
      a 7 ==== 3=== 5 ing
      2 2 ==== 2=== 3 up-
      u 9 ==== 1=== 5 wards
      3 Z ==== ==== 3 ."""), 9.59, 10.82
    ),
    phrase("downwards", notes("""
      1 9 L4== 10N0 3 fly-
      a 2 ==== 2=== 5 ing
      2 7 ==== 3=== 3 down-
      u 0 ==== 4=== 5 wards
      3 Z ==== ==== 3 ."""), 10.82, 12.06
    ),
    phrase("terminal", notes("""
      1 7 L4== 30N0 3 land-
      a = ==== ==== 5 ing
      2 2 ==== 2=== 3 at
      u = ==== ==== 5 the
      3 9 ==== 1=== 3 ter-
      e = ==== ==== 5 mi-
      4 2 ==== 2=== 3 nal
      1 Z ==== ==== 5 ."""), 14.24, 17.01
    ),
  ])
], "04.aeroplane-games.mp3"))

