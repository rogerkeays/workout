#!/bin/bash

source $(dirname $0)/modules/workout.sh

INSTRUMENT=1
OUTDIR=$TARGET/intervals

STEPS=-17
for PITCH in 27 28 29 2X 2Y 30 31 32 33 34 35 36 37 38 39 3X 3Y 40 41 42 43 44 45 46; do
  INTERVAL=-12
  for NOTE in C, _D, D, _E, E, F, _G, G, _A, A, _B, B, C _D D _E E F _G G _A A _B B c; do
    make_mp3 "
      X:0
      M:1/4
      L:1/4
      Q:60
      K:C
      | [I:MIDI program $((INSTRUMENT - 1))] 
      |:C|$NOTE|C|$NOTE|C|$NOTE:|" \
      $OUTDIR ${PITCH}$(printf %+03d $INTERVAL).mp3 $STEPS 100

    INTERVAL=$((INTERVAL+1))
  done
  STEPS=$((STEPS+1))
done

