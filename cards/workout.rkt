#lang jamaica sweet-exp racket
;; vim: syntax=scheme

require fluent/unicode
provide select

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

