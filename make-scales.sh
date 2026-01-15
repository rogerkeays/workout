#!/bin/bash

INSTRUMENT=57

source make-patterns.sh

generate_scales scales/major-1 "
  X:0
  M:4/4
  L:1/4
  Q:100
  K:C
  | [I:MIDI program 115] 
  |cccc| [I:MIDI program $((INSTRUMENT - 1))] 
  |CDEF|GABc|BAGF|EDC2|z4| [I:MIDI program 115] 
  |cccc
  |CCCC|CCCC|CCCC|CCC2|z4|
  " "37 38 39 3X 3Y 40 41 42 43 44 45 46 47 48 49 4X 4Y 50 51 52 53 54 55 56"

generate_scales scales/minor-nat-1 "
  X:0
  M:4/4
  L:1/4
  Q:100
  K:C 
  | [I:MIDI program 115]
  |cccc| [I:MIDI program $((INSTRUMENT - 1))] 
  |CD_EF|G_ABc|BAGF|EDC2|z4| [I:MIDI program 115]
  |cccc
  |CCCC|CCCC|CCCC|CCC2|z4|
  " "37 38 39 3X 3Y 40 41 42 43 44 45 46 47 48 49 4X 4Y 50 51 52 53 54 55 56"

generate_scales scales/major-2 "
  X:0
  M:4/4
  L:1/4
  Q:100
  K:C 
  | [I:MIDI program 115]
  |cccc| [I:MIDI program $((INSTRUMENT - 1))] 
  |CDEF|GABc|defg|abc'b|agfe|dcBA|GFED|C4|z4| [I:MIDI program 115]
  |cccc
  |CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|C4|z4|
  " "37 38 39 3X 3Y 40 41 42 43 44 45 46"

generate_scales scales/minor-nat-2 "
  X:0
  M:4/4
  L:1/4
  Q:100
  K:C
  | [I:MIDI program 115]
  |cccc| [I:MIDI program $((INSTRUMENT - 1))] 
  |CD_EF|G_ABc|d_efg|_abc'b|_agf_e|dcB_A|GF_ED|C4|z4| [I:MIDI program 115]
  |cccc
  |CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|C4|z4|
  " "37 38 39 3X 3Y 40 41 42 43 44 45 46"

generate_scales scales/major-3 "
  X:0
  M:4/4
  L:1/4
  Q:100
  K:C
  | [I:MIDI program 115]
  |cccc| [I:MIDI program $((INSTRUMENT - 1))] 
  |CDEF|GABc|defg|abc'd'|e'f'g'a'|b'c''b'a'|g'f'e'd'|c'bag|fedc|BAGF|EDC2|z4| [I:MIDI program 115]
  |cccc
  |CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|CCC2|z4|
  " "37 38 39 3X 3Y 40 41 42 43 44 45 46"

generate_scales scales/minor-nat-3 "
  X:0
  M:4/4
  L:1/4
  Q:100
  K:C
  | [I:MIDI program 115]
  |cccc| [I:MIDI program $((INSTRUMENT - 1))] 
  |CD_EF|G_ABc|d_efg|_abc'd'|_e'f'g'_a'|b'c''b'_a'|g'f'_e'd'|c'b_ag|f_edc|B_AGF|_EDC2|z4| [I:MIDI program 115]
  |cccc
  |CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|CCC2|z4|
  " "37 38 39 3X 3Y 40 41 42 43 44 45 46"

generate_tempos scales/chromatic-1 "
  X:0
  M:4/4
  L:1/4
  Q:100
  K:C transpose=-5
  | [I:MIDI program 115]
  |cccc| [I:MIDI program $((INSTRUMENT - 1))] 
  |C^CD^D|EF^FG|^GA^AB|cB_BA|_AG_GF|E_ED_D|C4| [I:MIDI program 115]
  |cccc
  |CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|
  "

generate_tempos scales/chromatic-2 "
  X:0
  M:4/4
  L:1/4
  Q:100
  K:C transpose=-5
  | [I:MIDI program 115]
  |cccc| [I:MIDI program $((INSTRUMENT - 1))] 
  |C^CD^D|EF^FG|^GA^AB|c^cd^d|ef^fg|^ga^ab
  |c'b_ba|_ag_gf|e_ed_d|cB_BA|_AG_GF|E_ED_D|C4| [I:MIDI program 115]
  |cccc
  |CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|
  "

generate_tempos scales/chromatic-3 "
  X:0
  M:4/4
  L:1/4
  Q:100
  K:C transpose=-5
  | [I:MIDI program 115]
  |cccc| [I:MIDI program $((INSTRUMENT - 1))] 
  |C^CD^D|EF^FG|^GA^AB|c^cd^d|ef^fg|^ga^ab|c'^c'd'^d'|e'f'^f'g'|^g'a'^a'b'
  |c''b'_b'a'|_a'g'_g'f'|e'_e'd'_d'|c'b_ba|_ag_gf|e_ed_d|cB_BA|_AG_GF|E_ED_D|C4| [I:MIDI program 115]
  |cccc
  |CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|CCCC|
  "

