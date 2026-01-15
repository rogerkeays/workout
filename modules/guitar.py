# vim: foldmethod=expr foldtext=getline(v\:foldstart) foldexpr=indent(v\:lnum)\|\|indent(v\:lnum+1)\|\|getline(v\:lnum)[0]=='@'?1\:'<1' fillchars=fold\:\ 

from modules.workout import *

# constructors
def guitar(video_id, number, name, meter, tempo, tonic, sections):
  process_piece(Piece("guitar", video_id, number, name, meter, tempo, tonic, sections), None, None, None, None)


# drills
def strumming(tempo, lyrics, rhythm, directions, chords, start, stop):
  # capture parameters
  params = locals()
  del params["start"]
  del params["stop"]

  # scan phrase
  n = len(rhythm)
  for i in range(n):
    chord_shape(chords[i])

    # transition drills
    if i > 0:
      h = i - 1
      j = i + 1
      if chords[i] != chords[h]:
        chord_changes(tempo, chords[h], chords[i])

  # whole phrase
  muted_strumming(tempo, rhythm, directions)

  make_card(params, 5)
  make_metronome(tempo)
  make_chunk(start, stop, tempo)

def muted_strumming(tempo, rhythm, directions):
  make_card(locals(), 5)
  make_metronome(tempo)

def chord_changes(tempo, from_chord, to_chord):
  chord_shape(from_chord)
  chord_shape(to_chord)
  make_card(locals(), 15)
  make_metronome(tempo)

def chord_shape(chord):
  make_card(locals(), 15)


