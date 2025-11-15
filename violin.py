# vim: foldmethod=expr foldtext=getline(v\:foldstart) foldexpr=indent(v\:lnum)\|\|indent(v\:lnum+1)\|\|getline(v\:lnum)[0]=='@'?1\:'<1' fillchars=fold\:\ 

import re
from workout import *
from dataclasses import dataclass

# globals
SHAPES = "PGWCADKH" # Porcupine, Gun, Westside, Chicken, Alien, Dog, ducK, Huddle

# data structures
@dataclass # ViolinNote
class ViolinNote(Note):
  string: str
  base: int
  shape: str
  finger: int
  bow_position: str

  def to_string(n):
    return f"{n.beat} {n.degree} {n.attack}{n.vol_start}{n.vol_stop}{n.sustain} {n.string}{n.base}{n.shape}{n.finger} {n.bow_position} {n.label}"

  def to_compact_string(n):
    return f"{n.beat} {n.degree} {n.attack}{n.vol_start}{n.vol_stop}{n.sustain} {n.string}{n.base}{n.shape}{n.finger} {n.bow_position} {n.label[0:3]}"

  def hash(n):
    return f"{n.beat} {n.degree} {n.attack}{n.vol_start}{n.vol_stop}{n.sustain} {n.string}{n.base}{n.shape}{n.finger} {n.bow_position}"


# functions
def calculate_defaults(note, next):
  if next.degree == "=": next.degree = note.degree
  if next.attack == "=": next.attack = note.attack
  if next.vol_start == "=": next.vol_start = note.vol_start
  if next.vol_stop == "=": next.vol_stop = next.vol_start
  if next.sustain == "=": next.sustain = note.sustain
  if next.string == "=": next.string = note.string
  if next.base == "=": next.base = note.base
  if next.shape == "=": next.shape = note.shape
  if next.finger == "=": next.finger = note.finger
  if next.bow_position == "=": next.bow_position = note.bow_position

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

def lyrics(id, lyrics, template_id, start, stop):
  """ clone a phrase, but with different lyrics and different start and stops """
  template = all_phrases[template_id]
  split_lyrics = re.split("[- ]", lyrics)
  return phrase(id, list(map(lambda z: ViolinNote(
    beat = z[0].beat,
    degree = z[0].degree,
    attack = z[0].attack,
    vol_start = z[0].vol_start,
    vol_stop = z[0].vol_stop,
    sustain = z[0].sustain,
    string = z[0].string,
    base = z[0].base,
    shape = z[0].shape,
    finger = z[0].finger,
    bow_position = z[0].bow_position,
    label = z[1]), zip(template.notes, split_lyrics))), start, stop)

def note_at(string, fret):
  return decimal_to_note(note_to_decimal("5Y") - (int(string) * 7) + int(fret))

def notes(text: str) -> list[Note]:
  """
    parse a block of notes line by line and return an array of ViolinNotes
  """
  return list(map(parse_violin_note, filter(lambda x: len(x) > 0, map(str.strip, text.split("\n")))))

def parse_violin_note(text: str) -> Note:
  """
    field order: (beat) (degree) (attack vol_start vol_stop sustain) (string base shape finger) (bow_position) (label)
    example:
      1 0 L44= 22W0 3 twin-
      2 = ==== ==== 5 kl-
      3 7 ==== 1==0 3 twin-
      4 = ==== ==== 5 kl-
  """
  return ViolinNote(
    beat = text[0],
    degree = text[2],
    attack = text[4],
    vol_start = text[5],
    vol_stop = text[6],
    sustain = text[7],
    string = text[9],
    base = text[10],
    shape = text[11],
    finger = text[12],
    bow_position = text[14],
    label = text[16:])

def process_note(tempo, note, stop):
  if note.degree != "Z":
    bow_attack(tempo, note.beat + stop.beat, note.string, note.bow_position, stop.bow_position, note.attack, note.vol_start + note.vol_stop)
    hand_placement(note.string, note.shape, note.base)
    pitch_hitting(note.string, fret(note.shape, note.base, note.finger), note.finger)

def process_phrase(piece, section, phrase):
  if len(phrase.notes) == 0: return
  notes = phrase.notes
  tempo = piece.tempo

  # create phrase practise chunks
  if create_phrase(phrase.label, tempo, notes):

    # phrase drills
    make_phrase_drill(1, "lyrics recall", tempo, notes, lambda n: n.label, 1)
    make_phrase_drill(2, "rhythm recall", tempo, notes, lambda n: f"{n.beat} {n.label}", 1)
    make_phrase_drill(3, "melody recall", tempo, notes, lambda n: f"{n.beat} {n.degree} {n.label}", 1)
    make_phrase_drill(4, "bowing recall", tempo, notes, lambda n: f"{n.beat} {n.degree} {n.bow_position} {n.label}", 1)
    make_phrase_drill(5, "open strings", tempo, notes, lambda n: n.to_compact_string(), 5)
    make_phrase_drill(6, "mp3 play", tempo, notes, lambda n: n.to_compact_string(), 5)
    cut_repeating_chunk(find_mp3(piece.mp3), phrase.start_secs, phrase.stop_secs, "00007.mp3")
    make_phrase_drill(8, "metronome play", tempo, notes, lambda n: n.to_compact_string(), 5)
    os.chdir("../..")

    # process notes in reverse order
    for i in reversed(range(len(notes))):
      if i < len(notes) - 1: process_note(tempo, notes[i], notes[i+1])
      if i < len(notes) - 2: process_transition(tempo, notes[i], notes[i+1], notes[i+2])

def process_piece(piece):
  make_metronome(piece.tempo)

  # calculate defaults
  for section in piece.sections:
    for phrase in section.phrases:
      for i, note in enumerate(phrase.notes):
        if i < len(phrase.notes) - 1: calculate_defaults(note, phrase.notes[i + 1])

  # process sections
  for section in reversed(piece.sections): process_section(piece, section)

  # create piece practise chunks
  if len(piece.sections) > 1: create_piece_bracket(find_mp3(piece.mp3), piece.name)
  write_drill_cards()

def process_section(piece, section):
  notes = [note for phrase in section.phrases for note in phrase.notes]

  # process phrases in reverse
  for phrase in reversed(section.phrases): process_phrase(piece, section, phrase)

  # create section practise chunks
  if create_section(section.label, piece.tempo, notes):
    cut_repeating_chunk(find_mp3(piece.mp3), section.phrases[0].start_secs, section.phrases[-1].stop_secs, "00000.mp3")
    os.chdir("../..")

def process_transition(tempo, note, next, stop):
  rhythm = note.beat + next.beat + stop.beat
  strings = note.string + next.string
  bowing = note.bow_position + next.bow_position + stop.bow_position
  attack = note.attack + next.attack
  dynamics = note.vol_start + note.vol_stop + next.vol_start + next.vol_stop

  # transition drills
  if note.string == next.string:
    bow_changes(tempo, rhythm, note.string, bowing, attack, dynamics)
  else:
    string_crossings(tempo, rhythm, strings, bowing, attack, dynamics)
  if note.shape != next.shape:
    jankin_switches(note.shape, next.shape)
  if note.string != next.string:
    hand_jumps_rapid(tempo, strings, note.shape + next.shape, note.base + next.base)

def repeat(template_id, start, stop):
  """
    repeat a phrase with different start and stop times
    this function does not clone the notes
  """
  template = all_phrases[template_id]
  return Phrase(template_id, template.notes, start, stop)


# drills
def air_hammers(finger):
  make_drill(locals(), 30)

def arm_stretches():
  make_drill(locals(), 1)

def beat_clapping(tempo, rhythm):
  make_drill(locals(), 5)

def bow_attack(tempo, rhythm, string, bow_start, bow_stop, attack, dynamics):
  beat_clapping(tempo, rhythm)
  if bow_start != "^" and bow_start != "v":
    string_yanking(tempo, string, bow_start, "D" if bow_stop > bow_start else "U")
    make_drill(locals(), 5)

def bow_benders(string, bowpos):
  bow_placement(string, bowpos)
  make_drill(locals(), 10)

def bow_changes(tempo, rhythm, string, bowing, attack, dynamics):
  if attack[0] != "." and attack[1] != ".":
    beat_clapping(tempo, rhythm)
    make_drill(locals(), 5)

def bow_hand_resets():
  make_drill(locals(), 5)

def bow_hold():
  jellyfish()
  vertical_bow_raises()
  horizontal_bow_raises()
  itsy_bitsy_spider()
  bow_hand_resets()

def bow_placement(string, bowpos):
  violin_hold()
  bow_hold()
  make_drill(locals(), 5)

def elbow_raises():
  make_drill(locals(), 30)

def finger_hammers(string, fret, finger):
  air_hammers(finger)
  make_drill(locals(), 15)

def finger_stretches():
  make_drill(locals())

def finger_wriggles_curved(from_shape, to_shape):
  if to_shape > from_shape: from_shape, to_shape = to_shape, from_shape
  if from_shape != "N" and to_shape != "N" and from_shape != to_shape:
    finger_wriggles_straight(from_shape, to_shape)
    make_drill(locals(), 30)

def finger_wriggles_straight(from_shape, to_shape):
  if to_shape > from_shape: from_shape, to_shape = to_shape, from_shape
  if from_shape != "N" and to_shape != "N" and from_shape != to_shape:
    make_drill(locals(), 30)

def hand_jumps_silent(strings, shapes, bases):
  if shapes[0] != "N" and shapes[1] != "N":
    finger_wriggles_curved(shapes[0], shapes[1])
    jankin_switches(shapes[0], shapes[1])
    hand_placement(strings[1], shapes[1], bases[1])
    hand_placement(strings[0], shapes[0], bases[0])
    make_drill(locals(), 15)

def hand_jumps_exact(strings, shapes, bases):
  if shapes[0] != "N" and shapes[1] != "N":
    hand_jumps_silent(strings, shapes, bases)
    make_drill(locals(), 5)

def hand_jumps_rapid(tempo, strings, shapes, bases):
  if shapes[0] != "N" and shapes[1] != "N":
    hand_jumps_exact(strings, shapes, bases)
    make_drill(locals(), 5)

def hand_placement(string, shape, base):
  if shape in SHAPES:
    jankin(shape)
    pitch_hitting(string, base, "1")
    if make_drill(locals(), 60):
      make_drone(note_at(string, base))

def horizontal_bow_raises():
  make_drill(locals(), 10)

def itsy_bitsy_spider():
  make_drill(locals(), 5)

def jankin(shape):
  if shape in SHAPES:
    finger_stretches()
    make_drill(locals(), 15)

def jankin_switches(from_shape, to_shape):
  if to_shape > from_shape: from_shape, to_shape = to_shape, from_shape
  if from_shape != "N" and to_shape != "N" and from_shape != to_shape:
    jankin(from_shape)
    jankin(to_shape)
    make_drill(locals(), 15)

def jellyfish():
  make_drill(locals(), 5)

def no_hands_swivels():
  make_drill(locals(), 10)

def pinky_reaches():
  elbow_raises()
  make_drill(locals(), 30)

def pitch_hitting(string, fret, finger):
  if int(fret) != 0 and int(finger) != 0:
    finger_hammers(string, fret, finger)
    tuning()
    if make_drill(locals(), 5):
      make_drone(note_at(string, fret))

def son_file():
  make_metronome(60)
  make_drill(locals(), 4)

def string_crossings(tempo, rhythm, strings, bowing, attack, dynamics):
  string_switching(tempo, strings[0], strings[1], bowing[1])
  beat_clapping(tempo, rhythm)
  make_drill(locals(), 5)

def string_switching(tempo, frm, to, bowpos):
  if frm > to: frm, to = to, frm
  bow_hold()
  make_drill(locals(), 15)

def string_yanking(tempo, string, bowpos, direction):
  bow_benders(string, bowpos)
  make_drill(locals(), 15)

def tuning():
  if make_drill(locals(), 1):
    make_drone("49")

def vertical_bow_raises():
  make_drill(locals(), 10)

def violin_hold():
  arm_stretches()
  no_hands_swivels()


