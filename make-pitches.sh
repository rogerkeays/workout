#!/bin/bash

source $(dirname $0)/modules/workout.sh

INSTRUMENT=57
OUTDIR=$TARGET/pitches

STEPS=-20
for PITCH in 24 25 26 27 28 29 2X 2Y 30 31 32 33 34 35 36 37 38 39 3X 3Y 40 41 42 43 44 45 46 47 48 49 4X 4Y 50 51 52 53 54 55 56; do
  make_mp3 "
    X:0
    M:1/1
    L:1/1
    Q:30
    K:C transpose=$STEPS
    [I:MIDI program $((INSTRUMENT - 1))]
    |C|" $OUTDIR ${PITCH}.mp3 0 100

  STEPS=$((STEPS+1))
done

