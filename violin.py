
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

import math, re, shutil
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
  bow_direction: str
  start_bow: str
  stop_bow: str

  def to_string(n):
    return f"{n.start_beat}{n.stop_beat} {n.degree} {n.string}{n.base}{n.shape}{n.finger} {n.bow_direction}{n.start_bow}{n.stop_bow}{n.attack}{n.dynamics} {n.label}"

def parse_violin_note(text: str) -> Note:
  """
    field order: (start_beat stop_beat) degree (string base shape finger) (bow_direction start_bow stop_bow attack dynamic) label
    example: "12 0 02W0 3v5LM twin-"
  """
  return ViolinNote(
    start_beat = text[0],
    stop_beat = text[1],
    degree = text[3],
    string = text[5],
    base = text[6],
    shape = text[7],
    finger = text[8],
    bow_direction = text[10],
    start_bow = text[11],
    stop_bow = text[12],
    attack = text[13],
    dynamics = text[14],
    label = text[16:])

def notes(text: str) -> list[Note]:
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

  # calculate defaults
  for section in piece.sections:
    for phrase in section.phrases:
      for i, note in enumerate(phrase.notes):
        if i < len(phrase.notes) - 1: calculate_note_defaults(note, phrase.notes[i + 1])

  mcd(piece.name)
  shutil.copy(MP3_DIR + piece.mp3, ".")

  # process sections
  for section in reversed(piece.sections): process_section(piece, section)
  os.chdir("..")
  make_metronome(piece.tempo)

def process_section(piece, section):

  # create section practise chunks
  mcd("00" + sectionnum() + "." + section.label)
  cut_timed_chunk(
      mp3 = MP3_DIR + piece.mp3,
      start_secs = section.phrases[0].start_secs,
      stop_secs = section.phrases[-1].stop_secs,
      outfile = section.label + ".mp3");
  notes = [note for phrase in section.phrases for note in phrase.notes]
  make_section(section.label, piece.tempo, notes)

  # process phrases in reverse
  for phrase in reversed(section.phrases): process_phrase(piece, section, phrase)
  os.chdir("..")

def process_phrase(piece, section, phrase):
  if len(phrase.notes) == 0: return

  # create phrase practise chunks
  mcd("00" + phrasenum() + "." + phrase.label)
  cut_timed_chunk(
      mp3 = MP3_DIR + piece.mp3,
      start_secs = phrase.start_secs,
      stop_secs = phrase.stop_secs,
      outfile = phrase.label + ".mp3");
  notes = phrase.notes
  make_phrase(phrase.label, piece.tempo, notes)

  # process notes in reverse order
  for i in reversed(range(len(notes))):
    process_note(piece.tempo, notes[i])
    if i < len(notes) - 1: process_transition(piece.tempo, notes[i], notes[i+1])

  # phrase drills
  phrase_metronome(piece.tempo, notes)
  os.chdir("..")

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

def arm_stretches():
  make_drill(1, locals(), 1)

def jellyfish():
  make_drill(2, locals(), 5)

def finger_stretches():
  make_drill(3, locals())

def jankin(shape):
  if shape in SHAPES:
    finger_stretches()
    make_drill(4, locals(), 15)

def jankin_switches(from_shape, to_shape):
  if to_shape > from_shape: from_shape, to_shape = to_shape, from_shape
  if from_shape != "N" and to_shape != "N" and from_shape != to_shape:
    jankin(from_shape)
    jankin(to_shape)
    make_drill(5, locals(), 15)

def finger_wriggles_straight(from_shape, to_shape):
  if to_shape > from_shape: from_shape, to_shape = to_shape, from_shape
  if from_shape != "N" and to_shape != "N" and from_shape != to_shape:
    make_drill(6, locals(), 30)

def finger_wriggles_curved(from_shape, to_shape):
  if to_shape > from_shape: from_shape, to_shape = to_shape, from_shape
  if from_shape != "N" and to_shape != "N" and from_shape != to_shape:
    finger_wriggles_straight(from_shape, to_shape)
    make_drill(7, locals(), 30)

def air_hammers(finger):
  make_drill(8, locals(), 30)

def violin_hold():
  arm_stretches()
  no_hands_swivels()

def no_hands_swivels():
  make_drill(9, locals(), 10)

def bow_hold():
  jellyfish()
  vertical_bow_raises()
  horizontal_bow_raises()
  itsy_bitsy_spider()
  bow_hand_resets()

def vertical_bow_raises():
  make_drill(10, locals(), 10)

def horizontal_bow_raises():
  make_drill(11, locals(), 10)

def itsy_bitsy_spider():
  make_drill(12, locals(), 5)

def bow_hand_resets():
  make_drill(13, locals(), 5)

def elbow_raises():
  make_drill(14, locals(), 30)

def pinky_reaches():
  elbow_raises()
  make_drill(15, locals(), 30)

def tuning():
  if make_drill(16, locals(), 1):
    make_drone(49)

def hand_placement(string, shape, base):
  if shape in SHAPES:
    jankin(shape)
    pitch_hitting(string, base, "1")
    if make_drill(17, locals(), 60):
      make_drone(note_at(string, base))

def finger_hammers(string, fret, finger):
  air_hammers(finger)
  make_drill(18, locals(), 15)

def bow_placement(string, bowpos):
  violin_hold()
  bow_hold()
  make_drill(19, locals(), 5)

def bow_benders(string, bowpos):
  bow_placement(string, bowpos)
  make_drill(20, locals(), 10)

def string_yanking(tempo, string, bowpos, direction):
  bow_benders(string, bowpos)
  make_drill(21, locals(), 15)

def son_file():
  make_metronome(60)
  make_drill(22, locals(), 4)

def beat_clapping(tempo, rhythm):
  make_drill(23, locals(), 5)

def bow_attack(tempo, rhythm, string, bowing, attack, dynamics):
  if attack != ".":
    string_yanking(tempo, string, bowing[0], "D" if bowing[1] > bowing[0] else "U")
    beat_clapping(tempo, rhythm)
    make_drill(24, locals(), 5)

def bow_changes(tempo, rhythm, string, bowing, attack, dynamics):
  if attack[0] != "." and attack[1] != ".":
    beat_clapping(tempo, rhythm)
    make_drill(25, locals(), 5)

def pitch_hitting(string, fret, finger):
  if int(fret) != 0 and int(finger) != 0:
    finger_hammers(string, fret, finger)
    tuning()
    if make_drill(26, locals(), 5):
      make_drone(note_at(string, fret))

def string_switching(tempo, frm, to, bowpos):
  if frm > to: frm, to = to, frm
  bow_hold()
  make_drill(27, locals(), 15)

def hand_jumps_silent(strings, shapes, bases):
  if shapes[0] != "N" and shapes[1] != "N":
    finger_wriggles_curved(shapes[0], shapes[1])
    jankin_switches(shapes[0], shapes[1])
    hand_placement(strings[1], shapes[1], bases[1])
    hand_placement(strings[0], shapes[0], bases[0])
    make_drill(28, locals(), 15)

def hand_jumps_exact(strings, shapes, bases):
  if shapes[0] != "N" and shapes[1] != "N":
    hand_jumps_silent(strings, shapes, bases)
    make_drill(29, locals(), 5)

def hand_jumps_rapid(tempo, strings, shapes, bases):
  if shapes[0] != "N" and shapes[1] != "N":
    hand_jumps_exact(strings, shapes, bases)
    make_drill(30, locals(), 5)

def string_crossings(tempo, rhythm, strings, bowing, attack, dynamics):
  string_switching(tempo, strings[0], strings[1], bowing[1])
  beat_clapping(tempo, rhythm)
  make_drill(31, locals(), 5)

def rhythm_clapping(tempo, notes):
  make_phrase_drill(32, "rhythm_clapping", tempo, notes)

def bowing_visualisation(tempo, notes):
  make_phrase_drill(33, "bowing_vis", tempo, notes)

def fingering_visualisation(tempo, notes):
  make_phrase_drill(34, "fingering_vis", tempo, notes)

def phrase_visualisation(tempo, notes):
  rhythm_clapping(tempo,notes)
  fingering_visualisation(tempo, notes)
  bowing_visualisation(tempo, notes)
  make_phrase_drill(35, "phrase_vis", tempo, notes)

def open_strings(tempo, notes):
  make_phrase_drill(36, "open_strings", tempo, notes)

def phrase_metronome(tempo, notes):
  phrase_visualisation(tempo, notes)
  open_strings(tempo, notes)
  make_phrase_drill(37, "phrase_metronome", tempo, notes)

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

# repeat a phrase with different start and stop times
# this function does not clone the notes
def repeat(template_id, start, stop):
    template = all_phrases[template_id]
    return Phrase(template_id, template.notes, start, stop)

# clone a phrase, but with different lyrics and different start and stops
def lyrics(id, lyrics, template_id, start, stop):
    template = all_phrases[template_id]
    split_lyrics = re.split("[- ]", lyrics)
    return phrase(id, list(map(lambda z: ViolinNote(
        start_beat = z[0].start_beat,
        stop_beat = z[0].stop_beat,
        degree = z[0].degree,
        base = z[0].base,
        string = z[0].string,
        shape = z[0].shape,
        finger = z[0].finger,
        start_bow = z[0].start_bow,
        bow_direction = z[0].bow_direction,
        stop_bow = z[0].stop_bow,
        attack = z[0].attack,
        dynamics = z[0].dynamics,
        label = z[1]), zip(template.notes, split_lyrics))), start, stop)

