
#
# abbreviations
#
# rhythm      1bar2dup3cet4mow
# strings     1234
# bowing      0-8
# shape       NPGWCADKH None, Porcupine, Gun, Westside, Chicken, Alien, Dog, ducK, Huddle
# frets       0..24
# fingers     01234
# attack      DGS      Detache, leGato, Staccato
# dynamics    V        eVen
#

import math, re
from workout import *

FAST_TEMPO = 120
SHAPES = "PGWCADKH"

def locate(mp3):
 return os.environ['HOME'] + "/library/workout/violin/03.pieces/" + mp3

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

  # pad short lines using defaults
  n = len(index)
  if n > 1:
    if len(strings) < n: strings = strings.ljust(n, "2")
    if len(bowing) < n + 1 : bowing = bowing.ljust(n, "4")
    if len(shapes) < n : shapes = shapes.ljust(n, "W")
    if len(bases) < n : bases = bases.ljust(n, "0")
    if len(fingers) < n: fingers = fingers.ljust(n, "0")
    if len(attack) < n: attack = attack.ljust(n, "D")
    if len(dynamics) < n: dynamics = dynamics.ljust(n, "M")
  rhythm += "1"

  # general purpose metronomes
  make_metronome(1)
  make_metronome(tempo/2)
  make_metronome(tempo/1.5)
  make_metronome(tempo)

  # process phrases in reverse order
  lyrics = []
  right = len(index)
  for i, tupl in reversed(list(enumerate(phrases))):

    # split the lyrics, adding the first note of the next phrase if they are sequential
    phrase_lyrics = re.split("[- ]", tupl[0])
    left = right - len(phrase_lyrics)
    lyrics = phrase_lyrics + lyrics
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
           index[left:right], rhythm[left:right + 1], strings[left:right], bowing[left:right + 1],
           shapes[left:right], bases[left:right], fingers[left:right],
           attack[left:right], dynamics[left:right])
    right -= len(phrase_lyrics)

def phrase(title, tempo, mp3, start, stop, lyrics, index, rhythm, strings="", bowing="", 
           shapes="", bases="", fingers="", attack="", dynamics=""):
  params = locals()
  del params["mp3"]
  del params["start"]
  del params["stop"]

  # backing tracks for this phrase
  make_chunk(mp3, start, stop)

  # process in reverse order
  n = len(index)
  e = n + 1
  for i in reversed(range(n - 1)):
    if attack[i] != ".":
      bracket(index[i:e], rhythm[i:e], strings[i:e], bowing[i:e],
              shapes[i:e], bases[i:e], fingers[i:e], attack[i:e], dynamics[i:e])

    # word drills
    if i > 0:
      h = i - 1
      j = i + 1
      word(title, tempo, lyrics[h:j], rhythm[h:j+1], strings[h:j], bowing[h:j+1],
           shapes[h:j], bases[h:j], fingers[h:j], attack[h:j], dynamics[h:j])

  # phrase drills
  if re.search("[1-4]", fingers):
    open_strings(tempo, lyrics, index, rhythm, strings, bowing, attack, dynamics)

def bracket(index, rhythm, strings, bowing, shapes, bases, fingers, attack, dynamics):
  make_bracket(locals(), 5)

def word(title, tempo, lyrics, rhythm, strings, bowing, shapes, bases, fingers, attack, dynamics):

  # process notes in reverse order
  note(title, tempo, lyrics[1], rhythm[1:3], strings[1], bowing[1:3],
       shapes[1], bases[1], fingers[1], attack[1], dynamics[1])
  note(title, tempo, lyrics[0], rhythm[0:2], strings[0], bowing[0:2], 
       shapes[0], bases[0], fingers[0], attack[0], dynamics[0])

  # word drills
  if strings[0] == strings[1]:
    bow_changes(tempo, lyrics, rhythm, strings[0], bowing, attack, dynamics)
  else:
    string_crossings(tempo, lyrics, rhythm, strings, bowing, attack, dynamics)
  if shapes[0] != shapes[1]:
    jankin_switches(shapes[0], shapes[1])
  if strings[0] != strings[1]:
    hand_jumps_rapid(tempo, strings[0:2], shapes[0:2], bases[0:2])

def note(title, tempo, lyrics, rhythm, string, bowing, shape, base, finger, attack, dynamics):
  if lyrics != "." and lyrics != "," and attack != ".":
    bow_attack(tempo, lyrics, rhythm, string, bowing, attack, dynamics)
    hand_placement(string, shape, base)
    pitch_hitting(string, fret(shape, base, finger), finger)

##################
## BEGIN DRILLS ##
##################

def open_strings(tempo, lyrics, index, rhythm, strings, bowing, attack, dynamics):
  params = locals()
  for i in range(len(index)):
    if i > 0:
      h = i - 1
      j = i + 1
      if strings[i] == strings[h]:
        bow_changes(tempo, lyrics[h:j], rhythm[h:j+1], strings[h], bowing[h:j+1], attack[h:j], dynamics[h:j])
      else:
        string_crossings(tempo, lyrics[h:j], rhythm[h:j+1], strings[h:j], bowing[h:j+1], attack[h:j], dynamics[h:j])

  rhythm_clapping(tempo, lyrics, rhythm)
  bowing_visualisation(tempo, lyrics, index, rhythm, strings, bowing, attack, dynamics);
  make_drill(params, 5)

def rhythm_clapping(tempo, lyrics, rhythm):
  make_drill(locals(), 5)

def rhythm_solfege(tempo, lyrics, rhythm):
  make_drill(locals(), 5)

def bowing_visualisation(tempo, lyrics, index, rhythm, strings, bowing, attack, dynamics):
  make_drill(locals(), 5)

def string_crossings(tempo, lyrics, rhythm, strings, bowing, attack, dynamics):
  make_drill(locals(), 5)

def string_switching(tempo, frm, to, bowpos):
  if frm > to: frm, to = to, frm
  bow_hold()
  make_drill(locals(), 15)

def bow_changes(tempo, lyrics, rhythm, string, bowing, attack, dynamics):
  if attack[0] != "." and attack[1] != ".":
    bow_attack(tempo, lyrics[0], rhythm[0:2], string, bowing[0:2], attack[0], dynamics[0]),
    bow_attack(tempo, lyrics[1], rhythm[1:3], string, bowing[1:3], attack[1], dynamics[1]),
    rhythm_clapping(tempo, lyrics, rhythm)
    make_drill(locals(), 5)

def pitch_hitting(string, fret, finger):
  if int(fret) != 0 and int(finger) != 0:
    finger_hammers(string, fret, finger)
    if make_drill(locals(), 5):
      make_drone(note_at(string, fret))

def finger_hammers(string, fret, finger):
  air_hammers(finger)
  make_drill(locals(), 15)

def air_hammers(finger):
  make_drill( locals(), 30)

def bow_attack(tempo, lyrics, rhythm, string, bowing, attack, dynamics):
  if attack != ".":
    string_yanking(tempo, string, bowing[0], "D" if bowing[1] < bowing[0] else "U")
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
  stretches()
  no_hands_swivels()

def stretches():
  make_drill(locals(), 1)

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
    jankin(shape)
    pitch_hitting(string, base, "1")
    if make_drill(locals(), 60):
      make_drone(note_at(string, base))

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

def fret(shape, base, finger):
    if shape == "P": frets = [0, 2, 4, 6]   # porcupine
    elif shape == "G": frets = [0, 1, 3, 5] # gun
    elif shape == "W": frets = [0, 2, 3, 5] # westside
    elif shape == "C": frets = [0, 2, 4, 5] # chicken
    elif shape == "A": frets = [0, 1, 3, 4] # alien
    elif shape == "D": frets = [0, 1, 2, 4] # dog
    elif shape == "K": frets = [0, 2, 3, 4] # duck
    elif shape == "H": frets = [0, 1, 2, 3] # huddle
    return str(frets[int(finger) - 1] + int(base))

def note_at(string, fret):
    return decimal_to_note(note_to_decimal("5Y") - (int(string) * 7) + int(fret))

