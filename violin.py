#!/usr/bin/env python3

from workout import *

#----- drills
def scale_49_major_one_octave(tempo, section, attack, rhythm):
  scale(tempo, 0,
        [2,2,2,2,2,1,1,1, 1,1,1,2,2,2,2], # strings
        [0,2,4,5,7,2,4,5, 4,2,7,5,4,2,0], # frets
        [0,1,2,3,4,1,2,3, 2,1,4,3,2,1,0], # fingers
        section, "elbow", attack, rhythm)
  make_card(locals())

def scale(tempo, base, strings, frets, fingers, section, fulcrum, attack, rhythm):
  for frm, to in zip(strings, strings[1:]):
    if frm != to: string_xings(tempo, frm, to, section, fulcrum, attack, rhythm)
  for i, string in enumerate(strings):
    pitch_hitting(string, frets[i], fingers[i])

def fret_hitting(fret, finger):
  pitch_hitting(4, fret, finger)
  pitch_hitting(3, fret, finger)
  pitch_hitting(2, fret, finger)
  pitch_hitting(1, fret, finger)

def pitch_hitting(string, fret, finger):
  if fret != 0 and finger != 0:
    note = decimal_to_note(note_to_decimal("5Y") - (string * 7) + fret)
    make_card(locals())

def single_string_xings(tempo, section, fulcrum, attack, rhythm="ss"):
  string_xings(tempo, 3, 2, section, fulcrum, attack, rhythm)
  string_xings(tempo, 2, 3, section, fulcrum, attack, rhythm)
  string_xings(tempo, 2, 1, section, fulcrum, attack, rhythm)
  string_xings(tempo, 1, 2, section, fulcrum, attack, rhythm)
  string_xings(tempo, 4, 3, section, fulcrum, attack, rhythm)
  string_xings(tempo, 3, 4, section, fulcrum, attack, rhythm)

def string_xings(tempo, frm, to, section, fulcrum, attack, rhythm="ss", reps=15):
  string_xings(tempo, frm, to, section, fulcrum, "silent", rhythm, reps) if attack != "silent" else 0
  even_bowing(tempo, frm, section, attack, rhythm),
  even_bowing(tempo, to, section, attack, rhythm),
  make_card(locals())

def even_bowing(tempo, string, section, attack, rhythm, reps=15):
  bow_attack(string, section, attack, "D")
  bow_attack(string, section, attack, "U")
  make_card(locals())

def bow_attack(string, section, attack, dir, reps=15):
  string_wiggles(string, section)
  retuning()
  make_card(locals())

def string_wiggles(string, section, reps=30):
  bow_benders(string, section)
  swivel_and_stop(string, section)
  make_card(locals())

def retuning(): make_card(locals())

def bow_benders(string, section, reps=30):
  bow_placement(string, section)
  make_card(locals())

def swivel_and_stop(string, section, reps=5):
  make_card(locals())

def bow_placement(string, section, reps=5):
  violin_hold()
  make_card(locals())

def violin_hold():
  bow_hold()
  no_hands_swivels()

def no_hands_swivels(reps=5): make_card(locals())

def bow_hold():
  jellyfish()
  vertical_bow_raises()
  horizontal_bow_raises()
  itsy_bitsy_spider()
  bow_hand_resets()

def bow_hand_resets(reps=5): make_card(locals())
def itsy_bitsy_spider(): make_card(locals())
def horizontal_bow_raises(reps=15): make_card(locals())
def vertical_bow_raises(reps=30): make_card(locals())
def jellyfish(reps=15): make_card(locals())

# ------ goals
goal("the-crawl")
for tempo in [45, 90]:
  single_string_xings(tempo, "m", "elbow", "detache", "ss")
  phrase(tempo, "li.ttle ba.by crawls.to da.nger", "ssss ssss", "00 /77 22 99")
  phrase(tempo, "scared.he turns.round in.a cir.cle", "ssss ssss", "\\22 77 /22 \\77")
  piece(tempo, "the-crawl")

goal("baby-steps")
for tempo in [45, 90]:
  single_string_xings(tempo, "m", "elbow", "detache", "ss")
  string_xings(tempo, 3, 4, "m", "elbow", "detache", "ssx")
  string_xings(tempo, 2, 3, "m", "elbow", "detache", "ssx")
  phrase(tempo, "left.foot.step", "sssx", "00/7")
  phrase(tempo, "right.foot.step", "sssx", "/22\\7", "U")
  phrase(tempo, "looks.for mu.mmy", "ssss", "/2299")
  phrase(tempo, "fa.lling.down", "sssx", "\\270")
  piece(tempo, "baby-steps")

goal("the-car-trip")
for tempo in [55, 110]:
  single_string_xings(tempo, "m", "elbow", "detache", "ss")
  phrase(tempo, "li.ttle.ba.by throw.ing.up", "wwws", "/77 \\00 55 /0")
  phrase(tempo, "mu.mmy.wants.to throw.up.too", "wwws", "\\55 XX /55 0")
  phrase(tempo, "pu.lling.over", "ssss", "/7\\05X")
  phrase(tempo, "clean.it.up", "sssx", "/550")
  piece(tempo, "the-car-trip")

goal("aeroplane-games")
for tempo in [55, 110]:
  single_string_xings(tempo, "m", "elbow", "detache", "ss")
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

