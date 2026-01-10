#!/usr/bin/env python3
# vim: nowrap

from workout import *

# globals
set_mp3_dir(os.environ['HOME'] + "/library/workout/guitar/00.inbox")

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

