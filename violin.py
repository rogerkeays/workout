
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

  # generate slow drill cards if necessary
  tempos = [ tempo ]
  while tempos[0] > FAST_TEMPO:
    tempos = [ int(tempos[0] * 0.75) ] + tempos
  for tempo in tempos:

    # descend the directory hierarchy
    dirname = "." + title + ("." + str(tempo).zfill(3) if len(tempos) > 1 else "") + "/"
    mcd(str(num).zfill(2) + dirname + "00" + dirname)

    # piece drills
    speed = tempo / tempos[0]
    make_card({"title": title, "tempo": tempo}, 1)
    make_whole(mp3, speed)
    os.chdir("..")
    make_metronome(tempo)

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

      phrase(i + 1, tempo, mp3, speed, start, stop, lyrics,
             index[left:right], rhythm[left:right + 1], strings[left:right],
             shapes[left:right], bases[left:right], fingers[left:right], bowing[left:right + 1],
             attack[left:right], dynamics[left:right])
      left += len(lyrics) - 1

    os.chdir("..")

# break down a phrase into drills
def phrase(num, tempo, mp3, speed, start, stop, lyrics,
    index, rhythm, strings="", shapes="", bases="", fingers="", bowing="", attack="", dynamics=""):

  # descend the directory hierarchy
  params = locals()
  del params["num"]
  del params["mp3"]
  del params["speed"]
  del params["start"]
  del params["stop"]
  dirname = "." + "-".join(lyrics) + "/"
  mcd(str(num).zfill(2) + dirname + "00" + dirname)

  # phrase drills
  make_card(params, 5)
  make_chunk(mp3, speed, start, stop)
  open_strings(tempo, lyrics, index, rhythm, strings, bowing, attack, dynamics)
  rhythm_clapping(tempo, lyrics, rhythm)

  # process words
  os.chdir("..")
  for i in range(len(index)):
    if i > 0:
      h = i - 1
      j = i + 1
      word(i, tempo, lyrics[h:j], index[h:j], rhythm[h:j+1], strings[h:j], shapes[h:j], bases[h:j],
           fingers[h:j], bowing[h:j+1], attack[h:j], dynamics[h:j])

  os.chdir("..")

def word(num, tempo, lyrics, index, rhythm, strings, shapes, bases, fingers, bowing, attack, dynamics):

  # descend the directory hierarchy
  params = locals()
  del params["num"]
  dirname = "." + "-".join(lyrics) + "/"
  mcd(str(num).zfill(2) + dirname + "00" + dirname)

  # word drills
  make_card(params, 5)
  if strings[0] == strings[1]:
    bow_changes(tempo, lyrics[0:2], rhythm[0:3], strings[0],
                bowing[0:3], attack[0:2], dynamics[0:2])
  else:
    string_crossings(tempo, lyrics[0:2], rhythm[0:3], strings[0:2],
                     bowing[0:3], attack[0:2], dynamics[0:2])
    hand_jumps_rapid(tempo, strings[0:2], shapes[0:2], bases[0:2])
  if shapes[0] != shapes[1]:
    jankin_switches(shapes[0], shapes[1])
  rhythm_clapping(tempo, lyrics, rhythm)

  # process notes
  os.chdir("..")
  note(1, tempo, lyrics[0], rhythm[0:2], strings[0], shapes[0], bases[0], fingers[0],
       bowing[0:2], attack[0], dynamics[0])
  note(2, tempo, lyrics[1], rhythm[1:3], strings[1], shapes[1], bases[1], fingers[1],
       bowing[1:3], attack[1], dynamics[1])
  os.chdir("..")

def note(num, tempo, lyric, rhythm, string, shape, base, finger, bowing, attack, dynamic):

  # descend the directory hierarchy
  params = locals()
  del params["num"]
  mcd(str(num).zfill(2) + "." + lyric)

  # note drills
  make_card(params)
  bow_attack(tempo, lyric, rhythm, string, bowing, attack, dynamic)
  hand_placement(string, shape, base)
  os.chdir("..")

def open_strings(tempo, lyrics, index, rhythm, strings, bowing, attack, dynamics):
  make_card(locals(), 5)

def rhythm_clapping(tempo, lyrics, rhythm):
  make_card(locals(), 5)

def string_crossings(tempo, lyrics, rhythm, strings, bowing, attack, dynamics):
  make_card(locals(), 5)

def string_switching(tempo, frm, to, bowpos):
  if frm > to: frm, to = to, frm
  if make_card(locals(), 15):
    bow_hold()

def bow_changes(tempo, lyrics, rhythm, string, bowing, attack, dynamic):
  if attack[0] != "." and attack[1] != ".":
    make_card(locals(), 5)

def pitch_hitting(string, fret, finger):
  if int(fret) != 0 and int(finger) != 0:
    if make_card(locals(), 5):
      note = decimal_to_note(note_to_decimal("5Y") - (int(string) * 7) + int(fret))
      make_drone(note)
      finger_hammers(string, fret, finger)

def finger_hammers(string, fret, finger):
  if make_card(locals(), 15):
    air_hammers(finger)

def air_hammers(finger):
  make_card( locals(), 30)

def bow_attack(tempo, lyrics, rhythm, string, bowing, attack, dynamic):
  if make_card(locals(), 5):
    rhythm_clapping(tempo, lyrics, rhythm)
    string_yanking(tempo, string, bowing[0], "D" if bowing[0] < bowing[1] else "U")

def string_yanking(tempo, string, bowpos, direction):
  if make_card(locals(), 15):
    bow_benders(string, bowpos)

def bow_benders(string, bowpos):
  if make_card(locals(), 10):
    bow_placement(string, bowpos)

def bow_placement(string, bowpos):
  if make_card(locals(), 5):
    bow_hold()
    violin_hold()

def violin_hold():
  no_hands_swivels()

def no_hands_swivels():
  make_card(locals(), 10)

def bow_hold():
  bow_hand_resets()
  itsy_bitsy_spider()
  horizontal_bow_raises()
  vertical_bow_raises()
  jellyfish()

def bow_hand_resets():
  make_card(locals(), 5)

def itsy_bitsy_spider():
  make_card(locals(), 5)

def horizontal_bow_raises():
  make_card(locals(), 10)

def vertical_bow_raises():
  make_card(locals(), 10)

def jellyfish():
  make_card(locals(), 5)

def hand_jumps_rapid(tempo, strings, shapes, bases):
  if shapes[0] != "N" and shapes[1] != "N":
    if make_card(locals(), 5):
      hand_jumps_exact(strings, shapes, bases)

def hand_jumps_exact(strings, shapes, bases):
  if shapes[0] != "N" and shapes[1] != "N":
    if make_card(locals(), 5):
      hand_jumps_silent(strings, shapes, bases)

def hand_jumps_silent(strings, shapes, bases):
  if shapes[0] != "N" and shapes[1] != "N":
    if make_card(locals(), 15):
      hand_placement(strings[0], shapes[0], bases[0])
      hand_placement(strings[1], shapes[1], bases[1])
      jankin_switches(shapes[0], shapes[1])
      finger_wriggles_curved(shapes[0], shapes[1])

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

def jankin(shape):
  if shape in SHAPES:
    if make_card(locals(), 15):
      finger_stretches()

def finger_stretches():
  make_card(locals())

def jankin_switches(from_shape, to_shape):
  if to_shape > from_shape: from_shape, to_shape = to_shape, from_shape
  if from_shape != "N" and to_shape != "N" and from_shape != to_shape:
    if make_card(locals(), 15):
      jankin(from_shape)
      jankin(to_shape)

def finger_wriggles_curved(from_shape, to_shape):
  if to_shape > from_shape: from_shape, to_shape = to_shape, from_shape
  if from_shape != "N" and to_shape != "N" and from_shape != to_shape:
    if make_card(locals(), 30):
      finger_wriggles_straight(from_shape, to_shape)

def finger_wriggles_straight(from_shape, to_shape):
  if to_shape > from_shape: from_shape, to_shape = to_shape, from_shape
  if from_shape != "N" and to_shape != "N" and from_shape != to_shape:
    make_card(locals(), 30)

def pinky_reaches():
  if make_card(locals(), 30):
    elbow_raises()

def elbow_raises():
  make_card(locals(), 30)

def son_file():
  make_card(locals(), 4)
  make_metronome(60)

