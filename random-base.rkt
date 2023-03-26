#lang jamaica sweet-exp racket
;; vim: syntax=scheme

require fluent/unicode
provide (all-defined-out)

;; musical shorthand
define locs `(rhythm limau-panas orange-juice coffee step)
define swg `(rhythm ma mici meneceke)
define swgtl (swg → append `(make mena))
define swgtlm (swgtl → append `(masala))
define rhythm (swgtlm → append `(ca neca na ka niki ceka meneci miceke neceki))
define rhythm-3 `(rhythm masala meneci miceke neceki)
define rhythm-even `(rhythm mici niki make neca mena ceka meneceke)
define tonic `(tonic 0 1 2 3 4 5 6 7 8 9 X L)
define interval `(interval 0 1 2 3 4 5 6 7 8 9 X L)
define majmin `(mode major minor)
define mode `(mode major (minor natural harmonic melodic) pentatonic chromatic)
define progression `(progression 1545 1654 6415 1514)
define finger `(finger 1 2 3 4)
define eyes `(eyes open closed)

;;
;; select and print num drills from the drills tree at random
;;
define (select drills [num 20] [padding 5])
  for ((i padding)) (newline)
  for ((i num))
    begin
      drills → walk
      for ((j padding)) (newline)
      (read-line)

;;
;; traverse the tree, either by choosing one element at random (the normal), 
;; or by walking all of the children (if a : is specified)
;;
define (walk tree)
  if (tree → list?) 
    if (not (tree → list-ref 1 → eq? ':))
      begin 
        display (tree → first)
        display " : "
        tree → get-random 1 → walk
      begin
        displayln (tree → first)
        tree → list-tail 2 → iterate walk
    displayln tree

;;
;; get a random element from a list, ignoring the first `start` elements
;; as a label
;;
define (get-random list [start 0])
  list → list-ref (random start (list → length))

