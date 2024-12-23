
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
from dataclasses import dataclass

MP3_DIR = os.environ['HOME'] + "/library/workout/violin/04.pieces/"
FAST_TEMPO = 120
SHAPES = "PGWCADKH"

@dataclass
class ViolinNote(Note):
  base: int
  shape: str
  finger: int
  string: str
  bowing: str

  def to_string(self):
    return f"{self.beat} {self.degree} {self.base}{self.shape}{self.finger} {self.string}{self.bowing}{self.attack}{self.dynamics} {self.lyrics}"

def parse_violin_note(text: str) -> Note:
  """
    field order: rhythm degree " " string bowing attack dynamic " " base shape finger " " lyrics
    example: "1 0 0W0 23DM twinkle"
  """
  return ViolinNote(
    beat = text[0],
    degree = text[2],
    base = text[4],
    shape = text[5],
    finger = text[6],
    string = text[8],
    bowing = text[9],
    attack = text[10],
    dynamics = text[11],
    lyrics = text[13:])

def parse_violin_notes(text: str) -> list[Note]:
  """
    parse a block of notes line by line and return an array of ViolinNotes
  """
  return list(map(parse_violin_note, filter(lambda x: len(x) > 0, map(str.strip, text.split("\n")))))

def copy_note_defaults(to, frm):
  if to.degree == "=": to.degree = frm.degree
  if to.attack == "=": to.attack = frm.attack
  if to.dynamics == "=": to.dynamics = frm.dynamics
  if to.string == "=": to.string = frm.string
  if to.bowing == "=": to.bowing = frm.bowing
  if to.base == "=": to.base = frm.base
  if to.shape == "=": to.shape = frm.shape
  if to.finger == "=": to.finger = frm.finger

def process_piece(piece):
  make_metronome(1)

  # set defaults
  for section in piece.sections:
    for phrase in section.phrases:
      for i, note in enumerate(phrase.notes):
        if i > 0: copy_note_defaults(note, phrase.notes[i - 1])

  # process sections
  for section in reversed(piece.sections): process_section(piece, section)

def process_section(piece, section):
  make_metronome(section.tempo/2)
  make_metronome(section.tempo/1.5)
  make_metronome(section.tempo)
  for phrase in reversed(section.phrases): process_phrase(piece, section, phrase)

def process_phrase(piece, section, phrase):
  make_chunk(MP3_DIR + piece.mp3, phrase.start_secs, phrase.stop_secs)

  # process notes in reverse order
  notes = phrase.notes
  for i in reversed(range(len(notes))):
    if notes[i].attack != ".": make_bracket(notes[i:], 5)
    if i > 0: process_note(section.tempo, notes[i-1], notes[i])
    if i > 0 and i < len(notes) - 1: process_transition(section.tempo, notes[i-1], notes[i], notes[i+1])

  # phrase drills
  open_strings(section.tempo, phrase.notes)

def process_transition(tempo, note, next, stop):
  rhythm = note.beat + next.beat + stop.beat
  strings = note.string + next.string
  bowing = note.bowing + next.bowing + stop.bowing
  attack = note.attack + next.attack
  dynamics = note.dynamics + next.dynamics

  # transition drills
  if note.string == next.string:
    bow_changes(tempo, rhythm, note.string, bowing, attack, dynamics)
  else:
    string_crossings(tempo, rhythm, strings, bowing, attack, dynamics)
  if note.shape != next.shape:
    jankin_switches(note.shape, next.shape)
  if note.string != next.string:
    hand_jumps_rapid(tempo, strings, note.shape + next.shape, note.base + next.base)

def process_note(tempo, note, next):
  if note.lyrics != "." and note.lyrics != "," and note.attack != ".":
    bow_attack(tempo, note.beat + next.beat, note.string, note.bowing + next.bowing, note.attack, note.dynamics)
    hand_placement(note.string, note.shape, note.base)
    pitch_hitting(note.string, fret(note.shape, note.base, note.finger), note.finger)

###################
## PHRASE DRILLS ##
###################

def open_strings(tempo, notes):
  rhythm_clapping(tempo, notes)
  bowing_visualisation(tempo, notes);
  make_drill(notes, 5)

def rhythm_clapping(tempo, notes):
  make_drill(notes, 5)

def bowing_visualisation(tempo, notes):
  make_drill(notes, 5)

#################
## NOTE DRILLS ##
#################

def string_crossings(tempo, rhythm, strings, bowing, attack, dynamics):
  string_switching(tempo, strings[0], strings[1], bowing[1])
  note_clapping(tempo, rhythm)
  make_drill(locals(), 5)

def string_switching(tempo, frm, to, bowpos):
  if frm > to: frm, to = to, frm
  bow_hold()
  make_drill(locals(), 15)

def note_clapping(tempo, rhythm):
  make_drill(locals(), 5)

def bow_changes(tempo, rhythm, string, bowing, attack, dynamics):
  if attack[0] != "." and attack[1] != ".":
    note_clapping(tempo, rhythm)
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

def bow_attack(tempo, rhythm, string, bowing, attack, dynamics):
  if attack != ".":
    string_yanking(tempo, string, bowing[0], "D" if bowing[1] > bowing[0] else "U")
    note_clapping(tempo, rhythm)
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
    if shape == "N": return base
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

