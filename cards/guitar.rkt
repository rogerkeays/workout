#!/usr/bin/racket 
#lang jamaica sweet-exp racket
;; vim: syntax=scheme

require fluent/unicode "workout.rkt" "music.rkt"

;; bridge-hand drills
define es `(string 1 2 3 4 5 6)
define picking `(picking (flat alternate economic) (finger 12 123 1234))
define bridge-hand `(bridge-hand
 (strumming : $rhythm)
 (palm-muting : (direction up down))
 (string-walking : $picking $es $es)
 (string-skipping 
   (2 : $picking $es $es)
   (3 : $picking $es $es $es)
   (4 : $picking $es $es $es $es)
   (5 : $picking $es $es $es $es $es)))

;; fret-hand drills
define base-chord `(chord A Am B C D Dm E Em F Fm G)
define bar-chord `(chord-shape A Am C D Dm E Em G)
define pos-index `(pos 1 2 3 4 5 6 7 8 9 X L 10)
define pos-middle `(pos 3 4 5 6 7 8 9 X L 10 11 12)
define pos-ring `(pos 5 6 7 8 9 X L 10 11 12 13 14)
define pos-pinky `(pos 7 8 9 X L 10 11 12 13 14 15 16)
define finger-pos `(finger (1 : $pos-index) (2 : $pos-middle) (3 : $pos-ring) (4 : $pos-pinky))
define fret-hand `(fret-hand
 (flexibility
   finger-stretches)
 (chords
   (shapes : $base-chord)
   (changes
     (base : $base-chord $base-chord)
     (bar : $bar-chord $pos-index $bar-chord $pos-index)
     (base-bar : $bar-chord $pos-index $base-chord))
   (shifts : $bar-chord $pos-index $pos-index))
 (dropping
   (half-scales : $es $majmin)
   (trills : $finger-pos $es (interval 1 2))
   (hammer-ons : $finger-pos $es) ; should specify two fingers
   ; 3-finger-hammer-ons : all 3-finger patterns
   ; 4-finger-hammer-ons
   (flick-offs : $finger-pos $es))
   ; 3-finger-flick-offs
   ; 4-finger-flick-offs
 (muting : $rhythm))

;; combination drills
define string-octaves `(string (e : (octaves 1 2 3)) (a : (octaves 1 2 3)) (d : (octaves 1 2)) (b : (octaves 1 2)) (ee : (octaves 1)))
define hands-together `(hands-together
 (scales : $mode $picking $finger-pos $string-octaves)
 (arpeggios : $majmin $picking $finger-pos $string-octaves)
 (chord-progressions : $tonic $majmin $progression $rhythm)
 (arpeggiation-progressions 
   (3 : $tonic $majmin $progression $rhythm-3 $es $es $es)
   (4 : $tonic $majmin $progression $rhythm-even $es $es $es $es)))
#|
   (riffs
     glycerine-pineapple-pineapple-apple
     glycerine-watermelon-apple
     tengo-tu-love-intro
     tengo-tu-love-riff
     snow-riff
     rainbow-strumming
     butterfly-blue-dots
     butterfly-what-i-want
     tocarte-riff-slow-3-notes
     tocarte-riff-slow-4-notes
     tocarte-riff-fast-top
     tocarte-riff-fast-bottom
     wrong-direction-arpeggiations))
|#

module+ main
  for ((i 30))
    select bridge-hand 1
    select fret-hand 1
    select hands-together 1

