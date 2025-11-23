# vim: foldmethod=marker foldmarker=phrase,)) foldtext=getline(v\:foldstart)

import sys; sys.path.append("..")
from violin import *

# open string exercises
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

# first finger exercises
process_piece(Piece("the-door-handle", 4, 94, "37", "07.the-door-handle.mp3", [
  Section("shack", "V", [
    phrase("this-way", 10.25, 12.86, notes("""
      1 0 L44= 42N0 3 turn
      2 7 ==== 3=== 5 it
      3 9 ==== ===1 3 this
      4 7 ==== ===0 5 way
      1 Z ==== 2=== 3 ."""
    )),
    phrase("that-way", 12.86, 15.50, notes("""
      1 2 L44= 22N0 3 turn
      2 7 ==== 3=== 5 it
      3 9 ==== ===1 3 that
      4 7 ==== ===0 5 way
      1 Z ==== 2=== 3 ."""
    )),
    phrase("door", 15.50, 17.91, notes("""
      1 2 L44= 22N0 3 the
      2 2 ==== ==== 5 door
      3 4 ==== ===1 3 o-
      4 2 ==== ===0 5 pens
      1 Z ==== 3=== 3 ."""
    )),
    phrase("inside", 17.91, 21.19, notes("""
      1 7 L44= 32N0 3 go
      2 9 ==== ===1 5 in-
      3 0 ==== 4==0 3 side
      1 Z ==== ==== 5 ."""
    ))
  ])
]))

process_piece(Piece("the-puppy-dog", 3, 104, "49", "08.the-puppy-dog.mp3", [
  Section("park", "V", [
    phrase("puppy", 10.28, 13.80, notes("""
      1 7 L44= 12N0 3 mis-
      2 9 ==== ===1 5 chie-
      3 7 ==== ===0 3 vous
      1 0 ==== 2=== 5 pu-
      2 2 ==== ===1 3 ppy
      3 0 ==== ===0 5 dog
      1 Z ==== 3=== 3 ."""
    )),
    phrase("running", 13.80, 17.26, notes("""
      1 5 L44= 32N0 3 he's
      2 7 ==== ===1 5 run-
      3 5 ==== ===0 3 ning
      1 X ==== 4=== 5 a-
      2 0 ==== ===1 3 round
      3 X ==== ===0 5 me
      1 Z ==== 3=== 3 ."""
    )),
    phrase("play", 17.26, 21.22, notes("""
      1 7 L44= 32N1 3 he
      2 = ==== ==== 5 wants
      3 = ==== ==== 3 to
      1 0 ==== 2==0 5 play
      1 Z ==== ==== 3 ."""
    ))
  ])
]))

process_piece(Piece("hunger", 4, 105, "42", "09.hunger.mp3", [
  Section("baby-chair", "V", [
    phrase("hungry", 9.77, 12.14, notes("""
      1 2 L44= 12N0 3 get-
      2 7 ==== 2=== 5 ting
      3 9 ==== ===1 3 hun-
      4 7 ==== ===0 5 gry
      1 Z ==== 3=== 3 ."""
    )),
    phrase("time", 12.14, 14.45, notes("""
      1 0 L44= 32N0 3 for
      2 7 ==== 2=== 5 the
      3 9 ==== ===1 3 first
      4 7 ==== ===0 5 time
      1 Z ==== ==== 3 ."""
    )),
    phrase("what", 14.45, 16.72, notes("""
      1 7 L44= 22N0 3 what
      2 9 ==== ===1 5 is
      3 7 ==== ===0 3 hap-
      4 9 ==== ===1 5 ning?
      1 Z ==== 1=== 3 ."""
    )),
    phrase("mummy", 16.72, 18.98, notes("""
      1 2 L44= 12N0 3 where's
      2 4 ==== ===1 5 mu-
      3 = ==== ==== 3 mmy
      4 2 ==== ===0 5 now?
      1 Z ==== 2=== 3 ."""
    )),
    phrase("know", 18.98, 22.22, notes("""
      1 7 L44= 22N0 3 i
      2 0 ==== 3=== 5 don't
      3 = ==== ==== 3 know
      1 Z ==== ==== 5 ."""
    ))
  ])
]))

process_piece(Piece("stealing-cookies", 4, 144, "49", "10.stealing-cookies.mp3", [
  Section("kitchen", "V", [
    phrase("cookies", 9.23, 13.48, notes("""
      1 9 L44= 12N1 3 stea-
      3 7 ==== ===0 5 ling
      1 2 ==== 2==1 3 cook-
      3 0 ==== ===0 5 ies
      1 Z ==== 3=== 3 ."""
    )),
    phrase("pockets", 13.48, 15.70, notes("""
      1 5 L44= 32N0 3 shove
      a 7 ==== ===1 5 them
      2 5 ==== ===0 3 in
      u 7 ==== ===1 5 my
      3 0 ==== 2==0 3 po-
      4 2 ==== ===1 5 ckets
      1 Z ==== ==== 3 ."""
    )),
    phrase("eat", 15.70, 18.27, notes("""
      1 7 L44= 12N0 3 go-
      a 9 ==== ===1 5 nna
      2 7 ==== ===0 3 eat
      u 9 ==== ===1 5 them
      3 0 ==== 2==0 3 la-
      4 2 ==== ===1 5 ter
      1 Z ==== ==== 3 ."""
    ))
  ])
]))

process_piece(Piece("puppy-in-the-kitchen", 4, 110, "42", "11.puppy-in-the-kitchen.mp3", [
  Section("kitchen", "V", [
    phrase("puppy", 9.49, 11.74, notes("""
      1 2 L44= 12N0 3 pu-
      a = ==== ==== 5 ppy
      2 = ==== ==== 3 in
      u = ==== ==== 5 the
      3 4 ==== ===1 3 ki-
      4 2 ==== ===0 5 tchen
      1 Z ==== 2=== 3 ."""
    )),
    phrase("running", 11.74, 13.90, notes("""
      1 7 L44= 22N0 3 run-
      a = ==== ==== 5 ning
      2 = ==== ==== 3 in
      u = ==== ==== 5 the
      3 9 ==== ===1 3 ki-
      4 7 ==== ===0 5 tchen
      1 Z ==== 1=== 3 ."""
    )),
    phrase("someone", 13.90, 17.97, notes("""
      1 2 L44= 12N0 3 some-
      a = ==== ==== 5 one's
      2 4 ==== ===1 3 com-
      u = ==== ==== 5 ing,
      3 7 ==== 2==0 3 he
      e = ==== ==== 5 had
      4 9 ==== ===1 3 be-
      o = ==== ==== 5 tter
      1 0 ==== 3==0 3 hide
      1 Z ==== ==== 5 ."""
    ))
  ])
]))

process_piece(Piece("dad goes looking", 2, 104, "37", "12.dad-goes-looking.mp3", [
  Section("lost-kids-house", "V", [
    phrase("kid", 9.77, 12.23, notes("""
      1 0 L44= 42N0 3 some-
      a 2 ==== ===1 5 things
      2 0 ==== ===0 3 ha-
      u 2 ==== ===1 5 ppened,
      3 7 ==== 3=== 3 where
      e 9 ==== ===1 5 is
      4 7 ==== ===0 3 my
      o 9 ==== ===1 5 kid?
      1 Z ==== 2=== 3 ."""
    )),
    phrase("kitchen", 12.23, 14.53, notes("""
      1 4 L44= 22N1 3 must
      a = ==== ==== 5 be
      2 9 ==== 1==0 3 in
      u = ==== ==== 5 the
      3 Y ==== ===1 3 ki-
      4 = ==== ==== 5 tchen
      1 Z ==== ==== 3 ."""
    )),
    phrase("sofa", 14.53, 16.82, notes("""
      1 Y L44= 12N1 3 not
      a 9 ==== ===0 5 the
      2 Y ==== ===1 3 cur-
      u 9 ==== ===0 5 tain,
      3 4 ==== 2==1 3 or
      e 2 ==== ===0 5 the
      4 4 ==== ===1 3 so-
      o 2 ==== ===0 5 fa
      1 Z ==== 3=== 3 ."""
    )),
    phrase("help", 16.82, 19.91, notes("""
      1 7 L44= 32N0 3 should
      a 9 ==== ===1 5 i
      2 = ==== ==== 3 call
      u 7 ==== ===0 5 for
      3 0 ==== 4=== 3 help?
      1 Z ==== ==== 5 ."""
    ))
  ])
]))

