
#
# abbreviations
#
# rhythm      SEQHW    Sixteenth, Eight, Quarter, Half, Whole
# strings     1234
# shape       NPGWCADK None, Porcupine, Gun, Westside, Chicken, Alien, Dog, ducK
# frets       0..24
# fingers     01234
# direction   DU       Down, Up
# section     FMT      Frog, Middle, Tip
# fulcrum     LRI      eLbow, wRist, fIngers
# attack      AG       detAche, leGato
# dynamics    VC       eVen, staCcato
#

import math
from workout import *

# break down a phrase into drills
def phrase(tempo, lyrics, rhythm, strings="", shapes="", bases="", fingers="",
    direction="", section="", fulcrum="", attack="", dynamics="",
    start=0, stop=0):

  # capture parameters
  params = locals()
  del params["start"]
  del params["stop"]

  # default values
  n = len(rhythm)
  if not strings: strings = "2" * n
  if not shapes: shapes = "W" * n
  if not bases: bases = "2" * n
  if not fingers: fingers = "0" * n
  if not direction: direction = "DU" * math.ceil(n/2)
  if not section: section = "M" * n
  if not fulcrum: fulcrum = "L" * n
  if not attack: attack = "A" * n
  if not dynamics: dynamics = "V" * n

  # expand abbreviated parameters
  def repeat_to_fit(string, length):
    return (string * math.ceil(length / len(string)))[0:length]

  if n > 1:
    if len(strings) < n: strings = repeat_to_fit(strings, n)
    if len(shapes) < n : shapes = repeat_to_fit(shapes, n)
    if len(bases) < n : bases = repeat_to_fit(bases, n)
    if len(direction) < n : direction = repeat_to_fit(direction, n)

  # scan phrase
  open_strings(tempo, rhythm, strings, direction, section, fulcrum, attack, dynamics)
  for i in range(n):
    hand_placement_block(strings[i], shapes[i], bases[i])

    # transition drills
    if i > 0:
      h = i - 1
      j = i + 1
      if strings[i] != strings[h]:
        hand_jumps_rapid(tempo, strings[h:j], shapes[h:j], bases[h:j])
      if shapes[i] != shapes[h]:
        jankin_switches(shapes[h], shapes[i])

  # card for this phrase
  if re.search("[1-4]", fingers):
    make_card(params, 5)
    make_metronome(tempo)
    make_chunk(start, stop, tempo)

def open_strings(tempo, rhythm, strings, direction, section, fulcrum, attack, dynamics):
  params = locals()

  # scan phrase
  for i in range(len(rhythm)):
    if i > 0:
      h = i - 1
      j = i + 1
      if strings[i] == strings[h]:
        bow_changes(tempo, rhythm[h:j], strings[h], direction[h:j], section[h:j], fulcrum[h:j], attack[h:j], dynamics[h:j])
      else:
        string_crossings(tempo, rhythm[h:j], strings[h:j], direction[h:j], section[h:j], fulcrum[h:j], attack[h:j], dynamics[h:j])

  # card for this phrase
  make_card(params, 5)
  make_metronome(tempo)

def string_crossings(tempo, rhythm, strings, direction, section, fulcrum, attack, dynamics):
  #if tempo > SLOW: string_crossings(half(tempo), rhythm, strings, direction, section, fulcrum, attack, dynamics)
  bow_attack(tempo, strings[0], direction[0], section[0], fulcrum[0], attack[0], dynamics[0])
  bow_attack(tempo, strings[1], direction[1], section[1], fulcrum[1], attack[1], dynamics[1])
  string_switching(tempo, strings[0], strings[1], section, fulcrum)
  make_card(locals(), 15)
  make_metronome(tempo)

def string_switching(tempo, frm, to, section, fulcrum):
  #if tempo > SLOW: string_switching(half(tempo), frm, to, section, fulcrum)
  if frm > to: frm, to = to, frm
  bow_hold()
  make_card(locals(), 15)
  make_metronome(tempo)

def bow_changes(tempo, rhythm, string, direction, section, fulcrum, attack, dynamic):
  #if tempo > SLOW: bow_changes(half(tempo), rhythm, string, direction, section, fulcrum, attack, dynamic)
  bow_attack(tempo, string, direction[0], section[0], fulcrum[0], attack[0], dynamic[0]),
  bow_attack(tempo, string, direction[1], section[1], fulcrum[1], attack[1], dynamic[1]),
  make_card(locals(), 15)
  make_metronome(tempo)

def note(tempo, string, fret, finger, direction, section, fulcrum, attack, dynamic):
  bow_attack(tempo, string, direction, section, fulcrum, attack, dynamic)
  if int(fret) != 0 and int(finger) != 0:
    pitch_hitting(string, fret, finger)
    make_card(locals(), 15)

def pitch_hitting(string, fret, finger):
  if int(fret) != 0 and int(finger) != 0:
    finger_placement(string, finger)
    note = decimal_to_note(note_to_decimal("5Y") - (int(string) * 7) + int(fret))
    make_card(locals(), 5)
    make_drone(note)

def finger_placement(string, finger):
  finger_hammers(string, finger)

def finger_hammers(string, finger):
  air_hammers(finger)
  make_card(locals(), 30)

def air_hammers(finger):
  make_card(locals(), 30)

def bow_attack(tempo, string, direction, section, fulcrum, attack, dynamic):
  #if tempo > SLOW: bow_attack(half(tempo), string, direction, section, fulcrum, attack, dynamic)
  string_yanking(tempo, string, direction, section)
  make_card(locals(), 15)
  make_metronome(tempo)

def string_yanking(tempo, string, direction, section):
  #if tempo > SLOW: string_yanking(half(tempo), string, direction, section)
  bow_benders(string, section)
  make_card(locals(), 15)
  make_metronome(tempo)

def bow_benders(string, section):
  bow_placement(string, section)
  make_card(locals(), 15)

def bow_placement(string, section):
  bow_hold()
  violin_hold()
  make_card(locals(), 5)

def violin_hold():
  no_hands_swivels()

def no_hands_swivels():
  make_card(locals(), 15)

def bow_hold():
  jellyfish()
  vertical_bow_raises()
  horizontal_bow_raises()
  itsy_bitsy_spider()
  bow_hand_resets()

def bow_hand_resets():
  make_card(locals(), 5)

def itsy_bitsy_spider():
  make_card(locals(), 5)

def horizontal_bow_raises():
  make_card(locals(), 15)

def vertical_bow_raises():
  make_card(locals(), 15)

def jellyfish():
  make_card(locals(), 15)

def hand_jumps_rapid(tempo, strings, shapes, bases):
  if shapes[0] != "N" and shapes[1] != "N":
    hand_jumps_exact(strings, shapes, bases)
    make_card(locals(), 5)

def hand_jumps_exact(strings, shapes, bases):
  if shapes[0] != "N" and shapes[1] != "N":
    finger_wriggles_curved(shapes[0], shapes[1])
    jankin_switches(shapes[0], shapes[1])
    hand_placement_block(strings[0], shapes[0], bases[0])
    hand_placement_block(strings[1], shapes[1], bases[1])
    make_card(locals(), 5)

def jankin_switches(from_shape, to_shape):
  if from_shape != "N" and to_shape != "N" and from_shape != to_shape:
    jankin(from_shape)
    jankin(to_shape)
    make_card(locals(), 15)

def finger_wriggles_curved(from_shape, to_shape):
  if from_shape != "N" and to_shape != "N" and from_shape != to_shape:
    finger_wriggles_straight(from_shape, to_shape)
    make_card(locals(), 30)

def finger_wriggles_straight(from_shape, to_shape):
  if from_shape != "N" and to_shape != "N" and from_shape != to_shape:
    make_card(locals(), 30)

def hand_placement_block(string, shape, base):
  if shape != "N":
    hand_placement_individual(string, shape, base)
    make_card(locals(), 5)

def hand_placement_individual(string, shape, base):
  if shape != "N":
    violin_hold()
    jankin_curls(shape)
    if shape == "P": frets = [0, 2, 4, 6]
    elif shape == "G": frets = [0, 1, 3, 5]
    elif shape == "W": frets = [0, 2, 3, 5]
    elif shape == "C": frets = [0, 2, 4, 5]
    elif shape == "A": frets = [0, 1, 3, 4]
    elif shape == "D": frets = [0, 1, 2, 4]
    elif shape == "K": frets = [0, 2, 3, 4]
    pitch_hitting(string, frets[0] + int(base), 1)
    pitch_hitting(string, frets[1] + int(base), 2)
    pitch_hitting(string, frets[2] + int(base), 3)
    pitch_hitting(string, frets[3] + int(base), 4)
    del frets
    make_card(locals(), 5)

def jankin_curls(shape):
  if shape != "N":
    jankin(shape)
    make_card(locals(), 15)

def jankin(shape):
  if shape != "N":
    finger_stretches()
    make_card(locals(), 15)

def finger_stretches():
  make_card(locals())

def pinky_reaches():
  elbow_raises()
  make_card(locals(), 15)

def elbow_raises():
  make_card(locals(), 15)

def son_file():
  make_card(locals(), 4)
  make_metronome(60)

###

def scale_49_major_one_octave(tempo, section, attack, rhythm):
  #if tempo > SLOW: scale_49_major_one_octave(half(tempo), section, attack, rhythm)
  half_scale(tempo, 2, [0,2,4,5,7], section, attack, rhythm)
  half_scale(tempo, 1, [0,2,4,5,7], section, attack, rhythm)
  hand_jumps_rapid(2, [2,4,5,7], 1, [2,4,5,7])
  scale(tempo, 0,
        [2,2,2,2,2,1,1,1, 1,1,1,2,2,2,2], # strings
        [0,2,4,5,7,2,4,5, 4,2,7,5,4,2,0], # frets
        [0,1,2,3,4,1,2,3, 2,1,4,3,2,1,0], # fingers
        section, "elbow", attack, rhythm)
  make_card(locals(), 3)
  make_metronome(tempo)

def scale(tempo, base, strings, frets, fingers, section, fulcrum, attack, rhythm):
  for frm, to in zip(strings, strings[1:]):
    if frm != to: string_crossings(tempo, rhythm, frm, to, section, fulcrum, attack)
  for i in range(0, len(fingers)):
    if fingers[i] != 0:
      finger_hammers(strings[i], frets[i], fingers[i])

def half_scale(tempo, string, frets, section, attack, rhythm):
  #if tempo > SLOW: half_scale(half(tempo), string, frets, section, attack, rhythm)
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

