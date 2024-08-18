
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
def piece(num, title, mp3, tempo, phrases, index="-", rhythm="1234", strings="2", bowing="35",
          shapes="W", bases="2", fingers="0", attack="D", dynamics="M"):

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

  # piece drills
  make_bracket(title, tempo, {}, 1)
  make_metronome(tempo)
  make_whole(mp3)

  # process phrases
  left = 0
  lyrics = []
  for i, tupl in enumerate(phrases):

    # split the lyrics, adding the first note of the next phrase if they are sequential
    phrase_lyrics = re.split("[- ]", tupl[0])
    right = left + len(phrase_lyrics)
    lyrics += phrase_lyrics
    if len(tupl) < 3 and i != len(phrases) - 1:
        phrase_lyrics.append(re.split("[- ]", phrases[i + 1][0])[0])
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

    phrase(title, tempo, mp3, start, stop, phrase_lyrics,
           index[left:right], rhythm[left:right + 1], strings[left:right],
           shapes[left:right], bases[left:right], fingers[left:right], bowing[left:right + 1],
           attack[left:right], dynamics[left:right])
    left += len(phrase_lyrics) - 1

  # process words
  for i in range(len(index)):
    if i > 0:
      h = i - 1
      j = i + 1
      word(title, tempo, lyrics[h:j], rhythm[h:j+1], strings[h:j], shapes[h:j], bases[h:j],
           fingers[h:j], bowing[h:j+1], attack[h:j], dynamics[h:j])

  # process notes
  for i in range(len(index)):
    note(title, tempo, lyrics[i], rhythm[i:i+2], strings[i], shapes[i], bases[i], fingers[i],
         bowing[i:i+2], attack[i], dynamics[i])

# break down a phrase into drills
def phrase(title, tempo, mp3, start, stop, lyrics,
    index, rhythm, strings="", shapes="", bases="", fingers="", bowing="", attack="", dynamics=""):
  params = locals()
  del params["mp3"]
  del params["start"]
  del params["stop"]
  make_bracket(title, tempo, params, 5)
  make_chunk(mp3, start, stop, 1, "B")
  make_chunk(mp3, start, stop, 0.5, "C")
  if re.search("[1-4]", fingers):
    open_strings(tempo, lyrics, index, rhythm, strings, bowing, attack, dynamics)

# word drills
def word(title, tempo, lyrics, rhythm, strings, shapes, bases, fingers, bowing, attack, dynamics):
  make_bracket(title, tempo, locals(), 5)
  if strings[0] == strings[1]:
    bow_changes(tempo, lyrics, rhythm, strings, bowing, attack, dynamics)
  else:
    string_crossings(tempo, lyrics, rhythm, strings, bowing, attack, dynamics)
    hand_jumps_rapid(tempo, strings[0:2], shapes[0:2], bases[0:2])
  if shapes[0] != shapes[1]:
    jankin_switches(shapes[0], shapes[1])

# note drills
def note(title, tempo, lyrics, rhythm, string, shape, base, finger, bowing, attack, dynamic):
  make_bracket(title, tempo, locals(), 5)
  hand_placement(string, shape, base)


##################
## BEGIN DRILLS ##
##################

def open_strings(tempo, lyrics, index, rhythm, strings, bowing, attack, dynamics):
  for i in range(len(index)):
    if i > 0:
      h = i - 1
      j = i + 1
      if strings[i] == strings[h]:
        bow_changes(tempo, lyrics[h:j], rhythm[h:j+1], strings[h], bowing[h:j+1], attack[h:j], dynamics[h:j])
      else:
        string_crossings(tempo, lyrics[h:j], rhythm[h:j+1], strings[h:j], bowing[h:j+1], attack[h:j], dynamics[h:j])

  rhythm_clapping(tempo, lyrics, rhythm)
  make_drill(locals(), 5)

def rhythm_clapping(tempo, lyrics, rhythm):
  make_drill(locals(), 5)

def string_crossings(tempo, lyrics, rhythm, strings, bowing, attack, dynamics):
  make_drill(locals(), 5)

def string_switching(tempo, frm, to, bowpos):
  if frm > to: frm, to = to, frm
  bow_hold()
  make_drill(locals(), 15)

def bow_changes(tempo, lyrics, rhythm, string, bowing, attack, dynamic):
  if attack[0] != "." and attack[1] != ".":
    bow_attack(tempo, lyrics[0], rhythm[0:2], string, bowing[0:2], attack[0], dynamic[0]),
    bow_attack(tempo, lyrics[1], rhythm[1:3], string, bowing[1:3], attack[1], dynamic[1]),
    rhythm_clapping(tempo, lyrics, rhythm)
    make_drill(locals(), 5)

def pitch_hitting(string, fret, finger):
  if int(fret) != 0 and int(finger) != 0:
    finger_hammers(string, fret, finger)
    note = decimal_to_note(note_to_decimal("5Y") - (int(string) * 7) + int(fret))
    make_drone(note)
    make_drill(locals(), 5)

def finger_hammers(string, fret, finger):
  air_hammers(finger)
  make_drill(locals(), 15)

def air_hammers(finger):
  make_drill( locals(), 30)

def bow_attack(tempo, lyrics, rhythm, string, bowing, attack, dynamic):
  string_yanking(tempo, string, bowing[0], "D" if bowing[0] < bowing[1] else "U")
  rhythm_clapping(tempo, lyrics, rhythm)
  make_drill(locals(), 5)

def string_yanking(tempo, string, bowpos, direction):
  bow_benders(string, bowpos)
  make_drill(locals(), 15)

def bow_benders(string, bowpos):
  bow_placement(string, bowpos)
  make_drill(locals(), 10)

def bow_placement(string, bowpos):
  violin_hold()
  bow_hold()
  make_drill(locals(), 5)

def violin_hold():
  no_hands_swivels()

def no_hands_swivels():
  make_drill(locals(), 10)

def bow_hold():
  jellyfish()
  vertical_bow_raises()
  horizontal_bow_raises()
  itsy_bitsy_spider()
  bow_hand_resets()

def bow_hand_resets():
  make_drill(locals(), 5)

def itsy_bitsy_spider():
  make_drill(locals(), 5)

def horizontal_bow_raises():
  make_drill(locals(), 10)

def vertical_bow_raises():
  make_drill(locals(), 10)

def jellyfish():
  make_drill(locals(), 5)

def hand_jumps_rapid(tempo, strings, shapes, bases):
  if shapes[0] != "N" and shapes[1] != "N":
    hand_jumps_exact(strings, shapes, bases)
    make_drill(locals(), 5)

def hand_jumps_exact(strings, shapes, bases):
  if shapes[0] != "N" and shapes[1] != "N":
    hand_jumps_silent(strings, shapes, bases)
    make_drill(locals(), 5)

def hand_jumps_silent(strings, shapes, bases):
  if shapes[0] != "N" and shapes[1] != "N":
    finger_wriggles_curved(shapes[0], shapes[1])
    jankin_switches(shapes[0], shapes[1])
    hand_placement(strings[1], shapes[1], bases[1])
    hand_placement(strings[0], shapes[0], bases[0])
    make_drill(locals(), 15)

def hand_placement(string, shape, base):
  if shape in SHAPES:
    violin_hold()
    jankin(shape)
    params = locals()
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
    make_drill(params, 60)

def jankin(shape):
  if shape in SHAPES:
    finger_stretches()
    make_drill(locals(), 15)

def finger_stretches():
  make_drill(locals())

def jankin_switches(from_shape, to_shape):
  if to_shape > from_shape: from_shape, to_shape = to_shape, from_shape
  if from_shape != "N" and to_shape != "N" and from_shape != to_shape:
    jankin(from_shape)
    jankin(to_shape)
    make_drill(locals(), 15)

def finger_wriggles_curved(from_shape, to_shape):
  if to_shape > from_shape: from_shape, to_shape = to_shape, from_shape
  if from_shape != "N" and to_shape != "N" and from_shape != to_shape:
    finger_wriggles_straight(from_shape, to_shape)
    make_drill(locals(), 30)

def finger_wriggles_straight(from_shape, to_shape):
  if to_shape > from_shape: from_shape, to_shape = to_shape, from_shape
  if from_shape != "N" and to_shape != "N" and from_shape != to_shape:
    make_drill(locals(), 30)

def pinky_reaches():
  elbow_raises()
  make_drill(locals(), 30)

def elbow_raises():
  make_drill(locals(), 30)

def son_file():
  make_metronome(60)
  make_drill(locals(), 4)

