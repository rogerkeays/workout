#!/usr/bin/env python3

from workout import *

def scale_49_major_one_octave(tempo, section, attack, rhythm, reps=3):
  half_scale(tempo, 2, [0,2,4,5,7], section, attack, rhythm, reps)
  half_scale(tempo, 1, [0,2,4,5,7], section, attack, rhythm, reps)
  hand_changes(2, [2,4,5,7], 1, [2,4,5,7])
  scale(tempo, 0,
        [2,2,2,2,2,1,1,1, 1,1,1,2,2,2,2], # strings
        [0,2,4,5,7,2,4,5, 4,2,7,5,4,2,0], # frets
        [0,1,2,3,4,1,2,3, 2,1,4,3,2,1,0], # fingers
        section, "elbow", attack, rhythm)
  make_card(locals())
  make_metronome(tempo)

def scale(tempo, base, strings, frets, fingers, section, fulcrum, attack, rhythm, reps=5):
  for frm, to in zip(strings, strings[1:]):
    if frm != to: string_crossings(tempo, frm, to, section, fulcrum, attack, rhythm)
  for i in range(0, len(fingers)):
    if fingers[i] != 0:
      finger_hammers(strings[i], frets[i], fingers[i])

def half_scale(tempo, string, frets, section, attack, rhythm, reps=5):
  even_bowing(tempo, string, section, attack, rhythm)
  hand_placement_block(string, frets[1:])
  for i in range(1, 5):
    finger_hammers(string, frets[i], i)
  del i
  make_card(locals())
  make_metronome(tempo)

def hand_changes(from_string, from_frets, to_string, to_frets, reps=5):
  hand_placement_block(from_string, from_frets)
  hand_placement_block(to_string, to_frets)
  jankin_switches(from_frets, to_frets)
  finger_wriggles(from_frets, to_frets)
  make_card(locals())

def hand_placement_block(string, frets, reps=5):
  hand_placement_individual(string, frets)
  make_card(locals())

def hand_placement_individual(string, frets, reps=5):
  violin_hold()
  finger_curls(frets)
  make_card(locals())

def finger_curls(frets, reps=15):
  jankin(frets)
  make_card(locals())

def jankin(frets, reps=15):
  finger_stretches()
  make_card(locals())

def finger_stretches():
  make_card(locals())

def jankin_switches(frm, to, reps=5):
  if frm != to:
    jankin(frm)
    jankin(to)
    make_card(locals())

def finger_wriggles(frm, to, reps=5):
  if frm != to:
    make_card(locals())

def finger_hammers(string, fret, finger, reps="15"):
  air_hammers(finger)
  pitch_hitting(string, fret, finger)
  make_card(locals())

def air_hammers(finger, reps="15"):
  make_card(locals())

def fret_hitting(fret, finger):
  pitch_hitting(4, fret, finger)
  pitch_hitting(3, fret, finger)
  pitch_hitting(2, fret, finger)
  pitch_hitting(1, fret, finger)

def pitch_hitting(string, fret, finger, reps="5"):
  if fret != 0 and finger != 0:
    violin_hold()
    note = decimal_to_note(note_to_decimal("5Y") - (string * 7) + fret)
    make_card(locals())
    make_drone(note)

def single_string_crossings(tempo, section, fulcrum, attack, rhythm="ss"):
  string_crossings(tempo, 3, 2, section, fulcrum, attack, rhythm)
  string_crossings(tempo, 2, 3, section, fulcrum, attack, rhythm)
  string_crossings(tempo, 2, 1, section, fulcrum, attack, rhythm)
  string_crossings(tempo, 1, 2, section, fulcrum, attack, rhythm)
  string_crossings(tempo, 4, 3, section, fulcrum, attack, rhythm)
  string_crossings(tempo, 3, 4, section, fulcrum, attack, rhythm)

def string_crossings(tempo, frm, to, section, fulcrum, attack, rhythm="ss", reps=15):
  even_bowing(tempo, frm, section, attack, rhythm),
  even_bowing(tempo, to, section, attack, rhythm),
  string_switching(tempo, frm, to, section, fulcrum, reps)
  make_card(locals())
  make_metronome(tempo)

def string_switching(tempo, frm, to, section, fulcrum, reps=15):
  bow_hold()
  if frm > to: frm, to = to, frm
  make_card(locals())
  make_metronome(tempo)

def even_bowing(tempo, string, section, attack, rhythm, reps=15):
  bow_attack(tempo, string, section, attack, "D")
  bow_attack(tempo, string, section, attack, "U")
  make_card(locals())
  make_metronome(tempo)

def bow_attack(tempo, string, section, attack, dir, reps=15):
  string_grabbing(tempo, string, section)
  make_card(locals())
  make_metronome(tempo)

def string_grabbing(tempo, string, section, reps=15):
  bow_benders(string, section)
  make_card(locals())
  make_metronome(tempo)

def bow_benders(string, section, reps=15):
  bow_placement(string, section)
  make_card(locals())

def bow_placement(string, section, reps=5):
  violin_hold()
  bow_hold()
  make_card(locals())

def violin_hold():
  no_hands_swivels()

def no_hands_swivels(reps=15):
  make_card(locals())

def bow_hold():
  jellyfish()
  vertical_bow_raises()
  horizontal_bow_raises()
  itsy_bitsy_spider()
  bow_hand_resets()

def bow_hand_resets(reps=5): make_card(locals())
def itsy_bitsy_spider(reps=5): make_card(locals())
def horizontal_bow_raises(reps=15): make_card(locals())
def vertical_bow_raises(reps=30): make_card(locals())
def jellyfish(reps=15): make_card(locals())


# ------ goals
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

