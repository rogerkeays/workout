#!/usr/bin/env python3

from violin import *

goal("the-crawl")
for tempo in [45, 90]:
  single_string_crossings(tempo, "m", "elbow", "detache", "ss")
  phrase(tempo, "li.ttle ba.by crawls.to da.nger", "ssss ssss", "00 /77 22 99")
  phrase(tempo, "scared.he turns.round in.a cir.cle", "ssss ssss", "\\22 77 /22 \\77")
  piece(tempo, "the-crawl")

goal("baby-steps")
for tempo in [45, 90]:
  single_string_crossings(tempo, "m", "elbow", "detache", "ss")
  string_crossings(tempo, 3, 4, "m", "elbow", "detache", "ssx")
  string_crossings(tempo, 2, 3, "m", "elbow", "detache", "ssx")
  phrase(tempo, "left.foot.step", "sssx", "00/7")
  phrase(tempo, "right.foot.step", "sssx", "/22\\7", "U")
  phrase(tempo, "looks.for mu.mmy", "ssss", "/2299")
  phrase(tempo, "fa.lling.down", "sssx", "\\270")
  piece(tempo, "baby-steps")

goal("the-car-trip")
for tempo in [55, 110]:
  single_string_crossings(tempo, "m", "elbow", "detache", "ss")
  phrase(tempo, "li.ttle.ba.by throw.ing.up", "wwws", "/77 \\00 55 /0")
  phrase(tempo, "mu.mmy.wants.to throw.up.too", "wwws", "\\55 XX /55 0")
  phrase(tempo, "pu.lling.over", "ssss", "/7\\05X")
  phrase(tempo, "clean.it.up", "sssx", "/550")
  piece(tempo, "the-car-trip")

goal("aeroplane-games")
for tempo in [55, 110]:
  single_string_crossings(tempo, "m", "elbow", "detache", "ss")
  phrase(tempo, "fly.ing.up.wards fly.ing.down.wards", "wwww", "\\X/507 7\\05X")
  phrase(tempo, "lan.ding.at.the term.i.nal", "wwws", "/550077\\0")
  piece(tempo, "baby-steps")

goal("first-finger-etudes")
fret_hitting(2, 2)

goal("second-finger-etudes")
fret_hitting(4, 2)

goal("third-and-fourth-finger-etudes")
fret_hitting(5, 3)
fret_hitting(7, 4)

goal("lightly-row")
for tempo in [45, 90]:
  scale_49_major_one_octave(tempo, "m", "detache", "ss")
  phrase(tempo, "lightly row, flamingo", "sssx sssx", "/744 522")
  phrase(tempo, "down the river we will go", "ssss sssx", "0245 777")
  phrase(tempo, "always rowing, never slowing", "ssss ssss", "7444 5222")
  phrase(tempo, "in my bright new red canoe", "ssss sssx", "0477 444")
  phrase(tempo, "see the fishes swimming by", "ssss sssx", "2222 245")
  phrase(tempo, "see the birds up in the sky", "ssss sssx", "4444 457")
  piece(tempo, "lightly-row")

