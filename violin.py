#!/usr/bin/env python3

import math
from workout import *

# break down a phrase into drills
def phrase(tempo, lyrics, strings, rhythm="", direction="", section="", fulcrum="", attack="",
    dynamics="", frets="", fingers="", start=0, stop=0):

  # capture parameters
  params = locals()
  del params["start"]
  del params["stop"]

  # default values
  n = len(strings)
  if not rhythm: rhythm = "s" * n
  if not direction: direction = "du" * math.ceil(n/2)
  if not section: section = "m" * n
  if not fulcrum: fulcrum = "e" * n
  if not attack: attack = "d" * n
  if not dynamics: dynamics = "m" * n
  if not frets: frets = "0" * n
  if not fingers: fingers = "0" * n

  # pick out string crossings
  for i in range(len(strings) - 1):
    j = i + 2
    frm = int(strings[i])
    to = int(strings[i + 1])
    if frm != to: string_crossings(tempo, frm, to, section[i:j], fulcrum[i], attack[i:j], rhythm[i:j], direction[i:j])

  # card for this phrase
  make_card(params, 5)
  make_metronome(tempo)
  if goalmp3:
    make_chunk(goalmp3, start, stop, tempo / goaltempo)

def jellyfish():
  make_card(locals(), 15)

def vertical_bow_raises():
  make_card(locals(), 15)

def horizontal_bow_raises():
  make_card(locals(), 15)

def itsy_bitsy_spider():
  make_card(locals(), 5)

def bow_hand_resets():
  make_card(locals(), 5)

def bow_hold():
  jellyfish()
  vertical_bow_raises()
  horizontal_bow_raises()
  itsy_bitsy_spider()
  bow_hand_resets()

def no_hands_swivels():
  make_card(locals(), 15)

def violin_hold():
  bow_hold()
  no_hands_swivels()

def bow_placement(string, section):
  bow_hold()
  violin_hold()
  make_card(locals(), 5)

def bow_benders(string, section):
  bow_placement(string, section)
  make_card(locals(), 15)

def string_grabbing(tempo, string, section):
  if tempo > SLOW: string_grabbing(half(tempo), string, section)
  bow_benders(string, section)
  make_card(locals(), 15)
  make_metronome(tempo)

def bow_attack(tempo, string, section, attack, dir):
  if tempo > SLOW: bow_attack(half(tempo), string, section, attack, dir)
  string_grabbing(tempo, string, section)
  make_card(locals(), 15)
  make_metronome(tempo)

def even_bowing(tempo, string, section, attack, rhythm):
  if tempo > SLOW: even_bowing(half(tempo), string, section, attack, rhythm)
  bow_attack(tempo, string, section[0], attack[0], "D")
  bow_attack(tempo, string, section[0], attack[0], "U")
  make_card(locals(), 15)
  make_metronome(tempo)

def finger_stretches():
  make_card(locals())

def finger_wriggles(frm, to):
  if frm != to:
    make_card(locals(), 5)

def jankin(frets):
  finger_stretches()
  make_card(locals(), 15)

def jankin_curls(frets):
  jankin(frets)
  make_card(locals(), 15)

def jankin_switches(frm, to):
  if frm != to:
    jankin(frm)
    jankin(to)
    make_card(locals(), 5)

def air_hammers(finger):
  make_card(locals(), 15)

def pitch_hitting(string, fret, finger):
  if fret != 0 and finger != 0:
    violin_hold()
    note = decimal_to_note(note_to_decimal("5Y") - (string * 7) + fret)
    make_card(locals(), 5)
    make_drone(note)

def fret_hitting(fret, finger):
  pitch_hitting(4, fret, finger)
  pitch_hitting(3, fret, finger)
  pitch_hitting(2, fret, finger)
  pitch_hitting(1, fret, finger)

def finger_hammers(string, fret, finger):
  air_hammers(finger)
  pitch_hitting(string, fret, finger)
  make_card(locals(), 15)

def hand_placement_individual(string, frets):
  violin_hold()
  jankin_curls(frets)
  make_card(locals(), 5)

def hand_placement_block(string, frets):
  hand_placement_individual(string, frets)
  make_card(locals(), 5)

def half_scale(tempo, string, frets, section, attack, rhythm):
  if tempo > SLOW: half_scale(half(tempo), string, frets, section, attack, rhythm)
  even_bowing(tempo, string, section, attack, rhythm)
  hand_placement_block(string, frets[1:])
  for i in range(1, 5):
    finger_hammers(string, frets[i], i)
  del i
  make_card(locals(), 5)
  make_mp3("""
  X:0
  M:4/4
  L:1/4
  Q:100
  K:C
  %%MIDI program 56
  |:CDEF|GFED|C4|
  """, note_to_decimal("37") + ((string - 1) * 7) - note_to_decimal("40"), tempo)

def string_switching(tempo, frm, to, section, fulcrum):
  if tempo > SLOW: string_switching(half(tempo), frm, to, section, fulcrum)
  bow_hold()
  if frm > to: frm, to = to, frm
  make_card(locals(), 15)
  make_metronome(tempo)

def string_crossings(tempo, frm, to, section, fulcrum, attack, rhythm="ss", mechanics="du"):
  if tempo > SLOW: string_crossings(half(tempo), frm, to, section, fulcrum, attack, rhythm, mechanics)
  even_bowing(tempo, frm, section, attack, rhythm),
  even_bowing(tempo, to, section, attack, rhythm),
  string_switching(tempo, frm, to, section, fulcrum)
  make_card(locals(), 15)
  make_metronome(tempo)

def single_string_crossings(tempo, section, fulcrum, attack, rhythm="ss"):
  string_crossings(tempo, 3, 2, section, fulcrum, attack, rhythm)
  string_crossings(tempo, 2, 3, section, fulcrum, attack, rhythm)
  string_crossings(tempo, 2, 1, section, fulcrum, attack, rhythm)
  string_crossings(tempo, 1, 2, section, fulcrum, attack, rhythm)
  string_crossings(tempo, 4, 3, section, fulcrum, attack, rhythm)
  string_crossings(tempo, 3, 4, section, fulcrum, attack, rhythm)

def hand_jumps(from_string, from_frets, to_string, to_frets):
  hand_placement_block(from_string, from_frets)
  hand_placement_block(to_string, to_frets)
  jankin_switches(from_frets, to_frets)
  finger_wriggles(from_frets, to_frets)
  make_card(locals(), 5)

def scale_49_major_one_octave(tempo, section, attack, rhythm):
  if tempo > SLOW: scale_49_major_one_octave(half(tempo), section, attack, rhythm)
  half_scale(tempo, 2, [0,2,4,5,7], section, attack, rhythm)
  half_scale(tempo, 1, [0,2,4,5,7], section, attack, rhythm)
  hand_jumps(2, [2,4,5,7], 1, [2,4,5,7])
  scale(tempo, 0,
        [2,2,2,2,2,1,1,1, 1,1,1,2,2,2,2], # strings
        [0,2,4,5,7,2,4,5, 4,2,7,5,4,2,0], # frets
        [0,1,2,3,4,1,2,3, 2,1,4,3,2,1,0], # fingers
        section, "elbow", attack, rhythm)
  make_card(locals(), 3)
  make_metronome(tempo)

def scale(tempo, base, strings, frets, fingers, section, fulcrum, attack, rhythm):
  for frm, to in zip(strings, strings[1:]):
    if frm != to: string_crossings(tempo, frm, to, section, fulcrum, attack, rhythm)
  for i in range(0, len(fingers)):
    if fingers[i] != 0:
      finger_hammers(strings[i], frets[i], fingers[i])

