
#
# abbreviations
#
# rhythm      SEQHW    Sixteenth, Eight, Quarter, Half, Whole
# strings     1234
# shape       NPGWCADK None, Porcupine, Gun, Westside, Chicken, Alien, Dog, ducK
# frets       0..24
# fingers     01234
# bowing      0-8
# attack      AG       detAche, leGato
# dynamics    VC       eVen, staCcato
# fulcrum     LRI      eLbow, wRist, fIngers
#

import math, re
from workout import *

# divide a score into phrases
def score(title, mp3, splits, tempo, lyrics, rhythm, strings="", bowing="",
          shapes="", bases="", fingers="", attack="", dynamics="", fulcrum="", index=""):

  # normalise tab lines
  lyrics = re.split("[- ]+", lyrics.replace("|", "").strip())
  rhythm = normalise_tab(rhythm)
  strings = normalise_tab(strings)
  bowing = normalise_tab(bowing)
  shapes = normalise_tab(shapes)
  bases = normalise_tab(bases)
  fingers = normalise_tab(fingers)
  attack = normalise_tab(attack)
  dynamics = normalise_tab(dynamics)
  fulcrum = normalise_tab(fulcrum)

  # default values
  n = len(rhythm)
  if not strings: strings = "2" * n
  if not bowing: bowing = "35" * math.ceil(n/2)
  if not shapes: shapes = "W" * n
  if not bases: bases = "2" * n
  if not fingers: fingers = "0" * n
  if not attack: attack = "A" * n
  if not dynamics: dynamics = "V" * n
  if not fulcrum: fulcrum = "L" * n

  # expand abbreviated parameters
  def repeat_to_fit(string, length): return (string * math.ceil(length / len(string)))[0:length]
  if n > 1:
    if len(strings) < n: strings = repeat_to_fit(strings, n)
    if len(bowing) < n + 1 : bowing = repeat_to_fit(bowing, n + 1)
    if len(shapes) < n : shapes = repeat_to_fit(shapes, n)
    if len(bases) < n : bases = repeat_to_fit(bases, n)

  # process phrases
  goal(title, tempo, mp3)
  split = 0
  start = 0
  for i, word in enumerate(lyrics):
    if word[0] == ">" and i > start:
      stop = i + 1
      phrase(tempo, lyrics[start:stop], rhythm[start:stop], strings[start:stop],
             shapes[start:stop], bases[start:stop], fingers[start:stop], bowing[start:stop + 1],
             attack[start:stop], dynamics[start:stop], fulcrum[start:stop], splits[split], splits[split + 1])
      start = i
      split += 1 if word[1] != ">" else 2

  # process last phrase
  stop = len(lyrics)
  phrase(tempo, lyrics[start:stop], rhythm[start:stop], strings[start:stop],
         shapes[start:stop], bases[start:stop], fingers[start:stop], bowing[start:stop + 1],
         attack[start:stop], dynamics[start:stop], fulcrum[start:stop], splits[split], splits[split + 1])

  # card for the whole score
  piece(tempo, title)

# break down a phrase into drills
def phrase(tempo, lyrics, rhythm, strings="", shapes="", bases="", fingers="",
    bowing="", attack="", dynamics="", fulcrum="", start=0, stop=0):

  # capture parameters
  params = locals()
  del params["start"]
  del params["stop"]

  # scan phrase
  open_strings(tempo, lyrics, rhythm, strings, bowing, attack, dynamics, fulcrum)
  for i in range(len(rhythm)):
    hand_placement(strings[i], shapes[i], bases[i])

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

def open_strings(tempo, lyrics, rhythm, strings, bowing, attack, dynamics, fulcrum):
  params = locals()

  # scan phrase
  for i in range(len(rhythm)):
    if i > 0:
      h = i - 1
      j = i + 1
      if strings[i] == strings[h]:
        bow_changes(tempo, rhythm[h:j], strings[h], bowing[h:j+1], attack[h:j], dynamics[h:j], fulcrum[h:j])
      else:
        string_crossings(tempo, rhythm[h:j], strings[h:j], bowing[h:j+1], attack[h:j], dynamics[h:j], fulcrum[h:j])

  # card for this phrase
  make_card(params, 5)
  make_metronome(tempo)

def string_crossings(tempo, rhythm, strings, bowing, attack, dynamics, fulcrum):
  #if tempo > SLOW: string_crossings(half(tempo), rhythm, strings, bowing, attack, dynamics, fulcrum)
  bow_attack(tempo, strings[0], bowing[0:2], attack[0], dynamics[0], fulcrum[0])
  bow_attack(tempo, strings[1], bowing[1:3], attack[1], dynamics[1], fulcrum[1])
  string_switching(tempo, strings[0], strings[1], bowing[1], fulcrum)
  make_card(locals(), 15)
  make_metronome(tempo)

def string_switching(tempo, frm, to, bowpos, fulcrum):
  #if tempo > SLOW: string_switching(half(tempo), frm, to, bowpos, fulcrum)
  if frm > to: frm, to = to, frm
  bow_hold()
  make_card(locals(), 15)
  make_metronome(tempo)

def bow_changes(tempo, rhythm, string, bowing, attack, dynamic, fulcrum):
  #if tempo > SLOW: bow_changes(half(tempo), rhythm, string, bowing, attack, dynamic, fulcrum)
  bow_attack(tempo, string, bowing[0:2], attack[0], dynamic[0], fulcrum[0]),
  bow_attack(tempo, string, bowing[1:3], attack[1], dynamic[1], fulcrum[1]),
  make_card(locals(), 15)
  make_metronome(tempo)

def note(tempo, string, fret, finger, bowing, attack, dynamic, fulcrum):
  bow_attack(tempo, string, bowing, attack, dynamic, fulcrum)
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

def bow_attack(tempo, string, bowing, attack, dynamic, fulcrum):
  #if tempo > SLOW: bow_attack(half(tempo), string, bowing, attack, dynamic, fulcrum)
  string_yanking(tempo, string, bowing[0], "D" if bowing[0] < bowing[1] else "U")
  make_card(locals(), 15)
  make_metronome(tempo)

def string_yanking(tempo, string, bowpos, direction):
  #if tempo > SLOW: string_yanking(half(tempo), bowpos, direction)
  bow_benders(string, bowpos)
  make_card(locals(), 15)
  make_metronome(tempo)

def bow_benders(string, bowpos):
  bow_placement(string, bowpos)
  make_card(locals(), 15)

def bow_placement(string, bowpos):
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
    hand_placement(strings[0], shapes[0], bases[0])
    hand_placement(strings[1], shapes[1], bases[1])
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

def hand_placement(string, shape, base):
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

