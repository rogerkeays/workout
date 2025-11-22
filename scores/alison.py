# vim: foldmethod=marker foldmarker=phrase,)) foldtext=getline(v\:foldstart)

import sys; sys.path.append("..")
from violin import *

process_piece(Piece("the-crawl", 4, 90, "37", "01.the-crawl.mp3", [
  Section("table", "V", [
    phrase("crawls", 10.16, 15.38, notes("""
      1 0 L4== 40N0 3 li-
      2 = ==== ==== 5 ttle
      3 7 ==== 3=== 3 ba-
      4 = ==== ==== 5 by
      1 2 ==== 2=== 3 crawls
      2 = ==== ==== 5 to
      3 9 ==== 1=== 3 dan-
      4 = ==== ==== 5 ger
      1 Z ==== ==== 3 ."""
    )),
    phrase("scared", 15.38, 21.53, notes("""
      1 2 L4== 20N0 3 scared
      2 = ==== ==== 5 he
      3 7 ==== 3=== 3 turns
      4 = ==== ==== 5 round
      1 2 ==== 2=== 3 in
      2 = ==== ==== 5 a
      3 7 ==== 3=== 3 cir-
      4 = ==== ==== 5 cle
      1 Z ==== ==== 3 ."""
    )),
  ])
]))

process_piece(Piece("baby-steps", 4, 90, "37", "02.baby-steps.mp3", [
  Section("lawn", "V", [
    phrase("left", 10.30, 13.05, notes("""
      1 0 L4== 40N0 3 left
      2 = ==== ==== 5 foot
      3 7 ==== 3=== 3 step
      1 Z ==== ==== 5 ."""
    )),
    phrase("right", 13.05, 15.67, notes("""
      1 2 L4== 20N0 5 right
      2 = ==== ==== 3 foot
      3 0 ==== 3=== 5 step
      1 Z ==== ==== 3 ."""
    )),
    phrase("mummy", 15.67, 18.30, notes("""
      1 2 L4== 20N0 3 looks
      2 = ==== ==== 5 for
      3 7 ==== 1=== 3 mu-
      4 = ==== ==== 5 mmy
      1 Z ==== ==== 3 ."""
    )),
    phrase("falling", 18.30, 21.75, notes("""
      1 2 L4== 20N0 3 fall-
      2 = ==== 3=== 5 ing
      3 7 ==== 4=== 3 down
      1 Z ==== ==== 5 ."""
    )),
  ])
]))

process_piece(Piece("the-first-fall", 4, 100, "37", "05.the-first-fall.mp3", [
  Section ("lounge", "V", [
    phrase("window", 10.19, 12.68, notes("""
      1 0 D44= 40N0 3 runs
      a = ==== ==== 5 in-
      2 = ==== ==== 3 to
      u = ==== ==== 5 the
      3 7 ==== 3=== 3 win-
      4 = ==== ==== 5 dow
      1 Z ==== 1=== 3 ."""
    )),
    phrase("falling", 12.68, 15.13, notes("""
      1 9 D44= 10N0 3 fall-
      a = ==== ==== 5 ing
      2 = ==== ==== 3 on
      a = ==== ==== 5 his
      3 2 ==== 2=== 3 arse
      1 Z ==== ==== 5 ."""
    )),
    phrase("what", 15.13, 17.53, notes("""
      1 2 D44= 20N0 5 what
      a = ==== ==== 3 the
      2 = ==== ==== 5 hell
      a = ==== ==== 3 just
      3 9 ==== 1=== 5 ha-
      4 = ==== ==== 3 ppened?
      1 Z ==== 2=== 5 ."""
    )),
    phrase("dunno", 17.53, 20.18, notes("""
      1 7 D44= 20N0 5 i
      2 2 ==== 3=== 3 don't
      3 0 ==== 4=== 5 know
      1 Z ==== ==== 3 ."""
    ))
  ])
]))

process_piece(Piece("into-the-kitchen", 4, 100, "37", "06.into-the-kitchen.mp3", [
  Section("kitchen", "V", [
    phrase("no-one", 10.04, 12.59, notes("""
      1 0 D44= 40N0 3 here
      a 7 ==== 3=== 5 there's
      2 = ==== ==== 3 no-
      u = ==== ==== 5 one,
      3 2 ==== 2=== 3 there
      e 7 ==== 3=== 5 there's
      4 = ==== ==== 3 no-
      o = ==== ==== 5 one
      1 Z ==== 1=== 3 ."""
    )),
    phrase("sneak", 12.59, 14.89, notes("""
      1 9 D44= 10N0 3 sneak
      a = ==== ==== 5 in-
      2 = ==== ==== 3 to
      u = ==== ==== 5 the
      3 2 ==== 2=== 3 ki-
      4 = ==== ==== 5 tchen
      1 Z ==== ==== 3 ."""
    )),
    phrase("climbing", 14.89, 17.19, notes("""
      1 2 D44= 20N0 3 climb-
      a = ==== ==== 5 ing
      2 = ==== ==== 3 up
      u = ==== ==== 5 the
      3 9 ==== 1=== 3 coun-
      4 = ==== ==== 5 ter
      1 Z ==== 2=== 3 ."""
    )),
    phrase("hanging", 17.19, 20.46, notes("""
      1 2 D44= 20N0 3 hang-
      a 7 ==== 3=== 5 ing
      2 = ==== ==== 3 off
      u = ==== ==== 5 the
      3 2 ==== 2=== 3 door
      1 Z ==== ==== 5 ."""
    )),
  ])
]))

process_piece(Piece("the-car-trip", 4, 110, "37", "03.the-car-trip.mp3", [
  Section("car", "V", [
    phrase("baby", 9.72, 12.04, notes("""
      1 9 L4== 10N0 3 li-
      2 = ==== ==== 5 ttle
      3 2 ==== 2=== 3 ba-
      4 = ==== ==== 5 by
      1 7 ==== 3=== 3 throw-
      2 = ==== ==== 5 ing
      3 2 ==== 2=== 3 up
      1 Z ==== ==== 5 ."""
    )),
    phrase("mummy", 12.04, 14.22, notes("""
      1 7 L4== 20N0 5 mu-
      2 = ==== ==== 3 mmy
      3 0 ==== 4=== 5 wants
      4 = ==== ==== 3 to
      1 7 ==== 3=== 5 throw
      2 = ==== ==== 3 up
      3 2 ==== 2=== 5 too
      1 Z ==== ==== 3 ."""
    )),
    phrase("pull", 14.22, 16.52, notes("""
      1 9 L4== 10N0 3 pull-
      2 2 ==== 2=== 5 ling
      3 7 ==== 3=== 3 o
      4 0 ==== 4=== 5 ver
      1 Z ==== ==== 3 ."""
    )),
    phrase("clean", 16.52, 19.46, notes("""
      1 7 L4== 20N0 3 clean
      2 = ==== ==== 5 it
      3 2 ==== 3=== 3 up
      1 Z ==== ==== 5 ."""
    )),
  ])
]))

process_piece(Piece("aeroplane-games", 4, 110, "37", "04.aeroplane-games.mp3", [
  Section("airfield", "V", [
    phrase("upwards", 9.59, 10.82, notes("""
      1 0 L4== 40N0 3 fly-
      a 7 ==== 3=== 5 ing
      2 2 ==== 2=== 3 up-
      u 9 ==== 1=== 5 wards
      3 Z ==== ==== 3 ."""
    )),
    phrase("downwards", 10.82, 12.06, notes("""
      1 9 L4== 10N0 3 fly-
      a 2 ==== 2=== 5 ing
      2 7 ==== 3=== 3 down-
      u 0 ==== 4=== 5 wards
      3 Z ==== ==== 3 ."""
    )),
    phrase("terminal", 14.24, 17.01, notes("""
      1 7 L4== 30N0 3 land-
      a = ==== ==== 5 ing
      2 2 ==== 2=== 3 at
      u = ==== ==== 5 the
      3 9 ==== 1=== 3 ter-
      e = ==== ==== 5 mi-
      4 2 ==== 2=== 3 nal
      1 Z ==== ==== 5 ."""
    )),
  ])
]))

