
#
# abbreviations
#
# rhythm      1bar2dup3cet4mow
# strings     1234
# shape       NPGWCADK None, Porcupine, Gun, Westside, Chicken, Alien, Dog, ducK
# frets       0..24
# fingers     01234
# bowing      0-8
# attack      DGS      Detache, leGato, Staccato
# dynamics    V        eVen
#

import math, re
from workout import *

SHAPES = "PGWCADK"
FAST_TEMPO = 120

# divide a score into phrases
def score(title, mp3, tempo, phrases, index="-", rhythm="1234", strings="2", bowing="35",
          shapes="W", bases="2", fingers="0", attack="D", dynamics="M"):

  # update the global state
  goal(title, tempo, mp3)

  # normalise tab lines
  index = normalise_tab(index)
  rhythm = normalise_tab(rhythm)
  strings = normalise_tab(strings)
  bowing = normalise_tab(bowing)
  shapes = normalise_tab(shapes)
  bases = normalise_tab(bases)
  fingers = normalise_tab(fingers)
  attack = normalise_tab(attack)
  dynamics = normalise_tab(dynamics)

  # expand abbreviated parameters
  def repeat_to_fit(string, length): return (string * math.ceil(length / len(string)))[0:length]
  n = len(index)
  if n > 1:
    if len(strings) < n: strings = repeat_to_fit(strings, n)
    if len(bowing) < n + 1 : bowing = repeat_to_fit(bowing, n + 1)
    if len(shapes) < n : shapes = repeat_to_fit(shapes, n)
    if len(bases) < n : bases = repeat_to_fit(bases, n)
    if len(fingers) < n: fingers = repeat_to_fit(fingers, n)
    if len(attack) < n: attack = repeat_to_fit(attack, n)
    if len(dynamics) < n: dynamics = repeat_to_fit(dynamics, n)
  rhythm += "1"

  # generate slow drill cards if necessary
  tempos = [ tempo ]
  while tempos[0] > FAST_TEMPO:
    tempos = [ int(tempos[0] * 0.75) ] + tempos
  for tempo in tempos:
    piece(tempo, title)

    # process phrases
    left = 0
    for i, tupl in enumerate(phrases):

      # split the lyrics, adding the first note of the next phrase if they are sequential
      lyrics = re.split("[- ]", tupl[0])
      right = left + len(lyrics)
      if len(tupl) < 3 and i != len(phrases) - 1:
          lyrics.append(re.split("[- ]", phrases[i + 1][0])[0])
          right += 1

      # calculate ommitted mp3 splits
      if len(tupl) == 3:
        start = tupl[1]
        stop = tupl[2]
      elif len(tupl) == 2:
        start = tupl[1]
        stop = phrases[i + 1][1]
      else:
        start = 0
        stop = 0

      phrase(tempo, lyrics, index[left:right], rhythm[left:right + 1], strings[left:right],
             shapes[left:right], bases[left:right], fingers[left:right], bowing[left:right + 1],
             attack[left:right], dynamics[left:right], start, stop)
      left += len(lyrics) - 1

    end_card()

# break down a phrase into drills
def phrase(tempo, lyrics, index, rhythm, strings="", shapes="", bases="", fingers="",
    bowing="", attack="", dynamics="", start=0, stop=0):

  # make a card for this drill
  params = locals()
  del params["start"]
  del params["stop"]
  if make_card(params, 5, tempo, start, stop):

    # scan phrase
    open_strings(tempo, lyrics, index, rhythm, strings, bowing, attack, dynamics)
    for i in range(len(index)):
      hand_placement(strings[i], shapes[i], bases[i])

      # transition drills
      if i > 0:
        h = i - 1
        j = i + 1
        if strings[i] != strings[h]:
          hand_jumps_rapid(tempo, strings[h:j], shapes[h:j], bases[h:j])
        if shapes[i] != shapes[h]:
          jankin_switches(shapes[h], shapes[i])

    end_card()

def open_strings(tempo, lyrics, index, rhythm, strings, bowing, attack, dynamics):
  params = locals()

  # card for this phrase
  if make_card(params, 5, tempo):
    rhythm_clapping(tempo, lyrics, rhythm)

    # scan phrase
    for i in range(len(index)):
      if i > 0:
        h = i - 1
        j = i + 1
        if strings[i] == strings[h]:
          bow_changes(tempo, lyrics[h:j], rhythm[h:j+1], strings[h], bowing[h:j+1], attack[h:j], dynamics[h:j])
        else:
          string_crossings(tempo, lyrics[h:j], rhythm[h:j+1], strings[h:j], bowing[h:j+1], attack[h:j], dynamics[h:j])

    end_card()

def rhythm_clapping(tempo, lyrics, rhythm):
  if make_card(locals(), 5, tempo): end_card()

def string_crossings(tempo, lyrics, rhythm, strings, bowing, attack, dynamics):
  if make_card(locals(), 5, tempo):
    bow_attack(tempo, lyrics[0], rhythm[0:2], strings[0], bowing[0:2], attack[0], dynamics[0])
    bow_attack(tempo, lyrics[1], rhythm[1:3], strings[1], bowing[1:3], attack[1], dynamics[1])
    string_switching(tempo, strings[0], strings[1], bowing[1])
    end_card()

def string_switching(tempo, frm, to, bowpos):
  if frm > to: frm, to = to, frm
  if make_card(locals(), 15, tempo):
    bow_hold()
    end_card()

def bow_changes(tempo, lyrics, rhythm, string, bowing, attack, dynamic):
  if attack[0] != "." and attack[1] != ".":
    if make_card(locals(), 5, tempo):
      bow_attack(tempo, lyrics[0], rhythm[0:2], string, bowing[0:2], attack[0], dynamic[0]),
      bow_attack(tempo, lyrics[1], rhythm[1:3], string, bowing[1:3], attack[1], dynamic[1]),
      rhythm_clapping(tempo, lyrics, rhythm)
      end_card()

def pitch_hitting(string, fret, finger):
  if int(fret) != 0 and int(finger) != 0:
    if make_card(locals(), 5):
      note = decimal_to_note(note_to_decimal("5Y") - (int(string) * 7) + int(fret))
      make_drone(note)
      finger_hammers(string, fret, finger)
      end_card()

def finger_hammers(string, fret, finger):
  if make_card(locals(), 15):
    air_hammers(finger)
    end_card()

def air_hammers(finger):
  if make_card(locals(), 30):
    end_card()

def bow_attack(tempo, lyrics, rhythm, string, bowing, attack, dynamic):
  if make_card(locals(), 5, tempo):
    string_yanking(tempo, string, bowing[0], "D" if bowing[0] < bowing[1] else "U")
    rhythm_clapping(tempo, lyrics, rhythm)
    end_card()

def string_yanking(tempo, string, bowpos, direction):
  if make_card(locals(), 15, tempo):
    bow_benders(string, bowpos)
    end_card()

def bow_benders(string, bowpos):
  if make_card(locals(), 10):
    bow_placement(string, bowpos)
    end_card()

def bow_placement(string, bowpos):
  if make_card(locals(), 5):
    bow_hold()
    violin_hold()
    end_card()

def violin_hold():
  no_hands_swivels()

def no_hands_swivels():
  if make_card(locals(), 10): end_card()

def bow_hold():
  jellyfish()
  vertical_bow_raises()
  horizontal_bow_raises()
  itsy_bitsy_spider()
  bow_hand_resets()

def bow_hand_resets():
  if make_card(locals(), 5): end_card()

def itsy_bitsy_spider():
  if make_card(locals(), 5): end_card()

def horizontal_bow_raises():
  if make_card(locals(), 10): end_card()

def vertical_bow_raises():
  if make_card(locals(), 10): end_card()

def jellyfish():
  if make_card(locals(), 5): end_card()

def hand_jumps_rapid(tempo, strings, shapes, bases):
  if shapes[0] != "N" and shapes[1] != "N":
    if make_card(locals(), 5):
      hand_jumps_exact(strings, shapes, bases)
      end_card()

def hand_jumps_exact(strings, shapes, bases):
  if shapes[0] != "N" and shapes[1] != "N":
    if make_card(locals(), 5):
      hand_jumps_silent(strings, shapes, bases)
      end_card()

def hand_jumps_silent(strings, shapes, bases):
  if shapes[0] != "N" and shapes[1] != "N":
    if make_card(locals(), 15):
      hand_placement(strings[0], shapes[0], bases[0])
      hand_placement(strings[1], shapes[1], bases[1])
      jankin_switches(shapes[0], shapes[1])
      finger_wriggles_curved(shapes[0], shapes[1])
      end_card()

def hand_placement(string, shape, base):
  if shape in SHAPES:
    if make_card(locals(), 60):
      violin_hold()
      jankin(shape)
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
      end_card()

def jankin(shape):
  if shape in SHAPES:
    if make_card(locals(), 15):
      finger_stretches()
      end_card()

def finger_stretches():
  if make_card(locals()): end_card()

def jankin_switches(from_shape, to_shape):
  if to_shape > from_shape: from_shape, to_shape = to_shape, from_shape
  if from_shape != "N" and to_shape != "N" and from_shape != to_shape:
    if make_card(locals(), 15):
      jankin(from_shape)
      jankin(to_shape)
      end_card()

def finger_wriggles_curved(from_shape, to_shape):
  if to_shape > from_shape: from_shape, to_shape = to_shape, from_shape
  if from_shape != "N" and to_shape != "N" and from_shape != to_shape:
    if make_card(locals(), 30):
      finger_wriggles_straight(from_shape, to_shape)
      end_card()

def finger_wriggles_straight(from_shape, to_shape):
  if to_shape > from_shape: from_shape, to_shape = to_shape, from_shape
  if from_shape != "N" and to_shape != "N" and from_shape != to_shape:
    if make_card(locals(), 30): end_card()

def pinky_reaches():
  if make_card(locals(), 30):
    elbow_raises()
    end_card()

def elbow_raises():
  if make_card(locals(), 30): end_card()

def son_file():
  if make_card(locals(), 4, 60): end_card()

