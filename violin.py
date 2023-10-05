#!/usr/bin/env python3

from workout import *

def jellyfish(reps=15):
  make_card(locals())

def vertical_bow_raises(reps=15):
  make_card(locals())

def horizontal_bow_raises(reps=15):
  make_card(locals())

def itsy_bitsy_spider(reps=5):
  make_card(locals())

def bow_hand_resets(reps=5):
  make_card(locals())

def bow_hold():
  jellyfish()
  vertical_bow_raises()
  horizontal_bow_raises()
  itsy_bitsy_spider()
  bow_hand_resets()

def no_hands_swivels(reps=15):
  make_card(locals())

def violin_hold():
  no_hands_swivels()

def bow_placement(string, section, reps=5):
  violin_hold()
  bow_hold()
  make_card(locals())

def bow_benders(string, section, reps=15):
  bow_placement(string, section)
  make_card(locals())

def string_grabbing(tempo, string, section, reps=15):
  bow_benders(string, section)
  if tempo > SLOW: string_grabbing(half(tempo), string, section, reps)
  make_card(locals())
  make_metronome(tempo)

def bow_attack(tempo, string, section, attack, dir, reps=15):
  string_grabbing(tempo, string, section)
  if tempo > SLOW: bow_attack(half(tempo), string, section, attack, dir, reps)
  make_card(locals())
  make_metronome(tempo)

def even_bowing(tempo, string, section, attack, rhythm, reps=15):
  bow_attack(tempo, string, section, attack, "D")
  bow_attack(tempo, string, section, attack, "U")
  if tempo > SLOW: even_bowing(half(tempo), string, section, attack, rhythm, reps)
  make_card(locals())
  make_metronome(tempo)

def finger_stretches():
  make_card(locals())

def finger_wriggles(frm, to, reps=5):
  if frm != to:
    make_card(locals())

def jankin(frets, reps=15):
  finger_stretches()
  make_card(locals())

def jankin_curls(frets, reps=15):
  jankin(frets)
  make_card(locals())

def jankin_switches(frm, to, reps=5):
  if frm != to:
    jankin(frm)
    jankin(to)
    make_card(locals())

def air_hammers(finger, reps="15"):
  make_card(locals())

def pitch_hitting(string, fret, finger, reps="5"):
  if fret != 0 and finger != 0:
    violin_hold()
    note = decimal_to_note(note_to_decimal("5Y") - (string * 7) + fret)
    make_card(locals())
    make_drone(note)

def fret_hitting(fret, finger):
  pitch_hitting(4, fret, finger)
  pitch_hitting(3, fret, finger)
  pitch_hitting(2, fret, finger)
  pitch_hitting(1, fret, finger)

def finger_hammers(string, fret, finger, reps="15"):
  air_hammers(finger)
  pitch_hitting(string, fret, finger)
  make_card(locals())

def hand_placement_individual(string, frets, reps=5):
  violin_hold()
  jankin_curls(frets)
  make_card(locals())

def hand_placement_block(string, frets, reps=5):
  hand_placement_individual(string, frets)
  make_card(locals())

def half_scale(tempo, string, frets, section, attack, rhythm, reps=5):
  even_bowing(tempo, string, section, attack, rhythm)
  hand_placement_block(string, frets[1:])
  for i in range(1, 5):
    finger_hammers(string, frets[i], i)
  del i
  if tempo > SLOW: half_scale(half(tempo), string, frets, section, attack, rhythm, reps)
  make_card(locals())
  make_mp3("""
  X:0
  M:4/4
  L:1/4
  Q:100
  K:C
  %%MIDI program 56
  |:CDEF|GFED|C4|
  """, note_to_decimal("37") + ((string - 1) * 7) - note_to_decimal("40"), tempo)

def string_switching(tempo, frm, to, section, fulcrum, reps=15):
  bow_hold()
  if frm > to: frm, to = to, frm
  if tempo > SLOW: string_switching(half(tempo), frm, to, section, fulcrum, reps)
  make_card(locals())
  make_metronome(tempo)

def string_crossings(tempo, frm, to, section, fulcrum, attack, rhythm="ss", mechanics="du", reps=15):
  even_bowing(tempo, frm, section, attack, rhythm),
  even_bowing(tempo, to, section, attack, rhythm),
  string_switching(tempo, frm, to, section, fulcrum, reps)
  if tempo > SLOW: string_crossings(half(tempo), frm, to, section, fulcrum, attack, rhythm, mechanics, reps)
  make_card(locals())
  make_metronome(tempo)

def single_string_crossings(tempo, section, fulcrum, attack, rhythm="ss"):
  string_crossings(tempo, 3, 2, section, fulcrum, attack, rhythm)
  string_crossings(tempo, 2, 3, section, fulcrum, attack, rhythm)
  string_crossings(tempo, 2, 1, section, fulcrum, attack, rhythm)
  string_crossings(tempo, 1, 2, section, fulcrum, attack, rhythm)
  string_crossings(tempo, 4, 3, section, fulcrum, attack, rhythm)
  string_crossings(tempo, 3, 4, section, fulcrum, attack, rhythm)

def hand_jumps(from_string, from_frets, to_string, to_frets, reps=5):
  hand_placement_block(from_string, from_frets)
  hand_placement_block(to_string, to_frets)
  jankin_switches(from_frets, to_frets)
  finger_wriggles(from_frets, to_frets)
  make_card(locals())

def scale_49_major_one_octave(tempo, section, attack, rhythm, reps=3):
  half_scale(tempo, 2, [0,2,4,5,7], section, attack, rhythm, reps)
  half_scale(tempo, 1, [0,2,4,5,7], section, attack, rhythm, reps)
  hand_jumps(2, [2,4,5,7], 1, [2,4,5,7])
  scale(tempo, 0,
        [2,2,2,2,2,1,1,1, 1,1,1,2,2,2,2], # strings
        [0,2,4,5,7,2,4,5, 4,2,7,5,4,2,0], # frets
        [0,1,2,3,4,1,2,3, 2,1,4,3,2,1,0], # fingers
        section, "elbow", attack, rhythm)
  if tempo > SLOW: scale_49_major_one_octave(half(tempo), section, attack, rhythm, reps)
  make_card(locals())
  make_metronome(tempo)

def scale(tempo, base, strings, frets, fingers, section, fulcrum, attack, rhythm, reps=5):
  for frm, to in zip(strings, strings[1:]):
    if frm != to: string_crossings(tempo, frm, to, section, fulcrum, attack, rhythm)
  for i in range(0, len(fingers)):
    if fingers[i] != 0:
      finger_hammers(strings[i], frets[i], fingers[i])

