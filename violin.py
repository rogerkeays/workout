
#
# abbreviations
#
# rhythm      1bar2dup3cet4mow
# strings     1234
# shape       NPGWCADKH None, Porcupine, Gun, Westside, Chicken, Alien, Dog, ducK, Huddle
# fingers     01234
# bowing      0-8
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
  string: str
  base: int
  shape: str
  finger: int
  start_bow: str
  stop_bow: str

  def to_string(n):
    return f"{n.start_beat}{n.stop_beat} {n.degree} {n.string}{n.base}{n.shape}{n.finger} {n.start_bow}{n.stop_bow}{n.attack}{n.dynamics} {n.label}"

def parse_violin_note(text: str) -> Note:
  """
    field order: (start_beat stop_beat) degree (string base shape finger) (start_bow stop_bow attack dynamic) label
    example: "12 0 20W0 35LM twinkle"
  """
  return ViolinNote(
    start_beat = text[0],
    stop_beat = text[1],
    degree = text[3],
    string = text[5],
    base = text[6],
    shape = text[7],
    finger = text[8],
    start_bow = text[10],
    stop_bow = text[11],
    attack = text[12],
    dynamics = text[13],
    label = text[15:])

def parse_violin_notes(text: str) -> list[Note]:
  """
    parse a block of notes line by line and return an array of ViolinNotes
  """
  return list(map(parse_violin_note, filter(lambda x: len(x) > 0, map(str.strip, text.split("\n")))))

def calculate_note_defaults(note, next):
  if note.stop_beat == "=": note.stop_beat = next.start_beat
  if note.stop_bow == "=": note.stop_bow = next.start_bow
  if next.degree == "=": next.degree = note.degree
  if next.attack == "=": next.attack = note.attack
  if next.dynamics == "=": next.dynamics = note.dynamics
  if next.string == "=": next.string = note.string
  if next.start_bow == "=": next.start_bow = note.stop_bow
  if next.base == "=": next.base = note.base
  if next.shape == "=": next.shape = note.shape
  if next.finger == "=": next.finger = note.finger

def process_piece(piece):
  make_metronome(1)

  # calculate defaults
  for section in piece.sections:
    for phrase in section.phrases:
      for i, note in enumerate(phrase.notes):
        if i < len(phrase.notes) - 1: calculate_note_defaults(note, phrase.notes[i + 1])

  # process sections
  for section in reversed(piece.sections): process_section(piece, section)

def process_section(piece, section):
  for phrase in reversed(section.phrases): process_phrase(piece, section, phrase)
  make_metronome(piece.tempo)

def process_phrase(piece, section, phrase):

  # process notes in reverse order
  notes = phrase.notes
  make_chunk(MP3_DIR + piece.mp3, phrase.start_secs, phrase.stop_secs)
  for i in reversed(range(len(notes))):
    make_bracket(piece.tempo, notes[i:])
    process_note(piece.tempo, notes[i])
    if i < len(notes) - 1: process_transition(piece.tempo, notes[i], notes[i+1])

  # phrase drills
  tempo = piece.tempo
  make_phrase_drill("rhythm_clapping", tempo, notes)
  make_phrase_drill("bowing_vis", tempo, notes)
  make_phrase_drill("open_strings", tempo, notes)
  make_phrase_drill("fingering_vis", tempo, notes)
  make_phrase_drill("phrase_vis", tempo, notes)
  make_phrase_drill("phrase_clicks", tempo, notes)

def process_transition(tempo, note, next):
  rhythm = note.start_beat + note.stop_beat + next.start_beat + next.stop_beat
  strings = note.string + next.string
  bowing = note.start_bow + note.stop_bow + next.start_bow + next.stop_bow
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

def process_note(tempo, note):
  if note.label != "." and note.label != "," and note.attack != ".":
    bow_attack(tempo, note.start_beat + note.stop_beat, note.string, note.start_bow + note.stop_bow, note.attack, note.dynamics)
    hand_placement(note.string, note.shape, note.base)
    pitch_hitting(note.string, fret(note.shape, note.base, note.finger), note.finger)


############
## DRILLS ##
############

def string_crossings(tempo, rhythm, strings, bowing, attack, dynamics):
  string_switching(tempo, strings[0], strings[1], bowing[1])
  beat_clapping(tempo, rhythm)
  make_drill(locals(), 5)

def string_switching(tempo, frm, to, bowpos):
  if frm > to: frm, to = to, frm
  bow_hold()
  make_drill(locals(), 15)

def beat_clapping(tempo, rhythm):
  make_drill(locals(), 5)

def bow_changes(tempo, rhythm, string, bowing, attack, dynamics):
  if attack[0] != "." and attack[1] != ".":
    beat_clapping(tempo, rhythm)
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
    beat_clapping(tempo, rhythm)
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

