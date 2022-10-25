#!/usr/bin/racket 
#lang jamaica sweet-exp racket
;; vim: syntax=scheme
;; screenshot size: 25x15

require fluent/unicode "workout.rkt" "music.rkt"

;; bowing drills
define tempo `(tempo 60 70 80 90)
define es `(string 1 2 3 4)
define ds `(strings 12 23 34)
define esd (es → append `(12 23 34))
define ud `(bow up down)
define fmt `(bow-position middle frog tip)
define fmtv  (fmt → append `(traveling))
define fmtw (fmt → append `(whole-bow))
define fmtvw (fmtv → append `(whole-bow))
define 4npb `(npb 1 2 3 4)
define 8npb `(npb 1 2 3 4 5 6 7 8)
define reps `(reps silent 1 2 1..2)
define attack `(attack detache martele staccato spiccato pizzicato colle) ; ricochet
define dynamics `(dynamics ppp pp p mf f ff fff)
define bowing `(bowing
  (hold
    jellyfish
    vertical-bow-raises
    windscreen-wiper
    (itsy-bitsy-spider : $eyes)
    (bow-hand-resets : $eyes))
  (placement
    (blind : $fmt $esd)
    (swivel-and-stop : $fmt $esd $eyes)
    (hops : $fmtv $esd))
  (direction
    (air-bowing : $locs $es $tempo)
    (straight : $locs $esd $eyes $tempo)
    (snaking : (bumps 1 2) (bow-speed 4) $esd $tempo)
    (tilting : (tilts 1 2 3) (bow-speed 4) $esd $tempo)
    (lane-changes : (lanes 123 321 212 232) (bow-speed 4) $esd $tempo))
  (pressure
    (son-file : $esd)
    (even-bowing : $locs $esd $eyes $tempo)
    (frog-reversed : $locs $esd $eyes $tempo)
    (finger-lifting : $locs $esd $eyes $tempo)
    (pinky-and-index-hold : $locs $esd $eyes $tempo)
    (bow-benders : $fmtv $esd)
    (parlando : (pressure heavy-light light-heavy) $swg (bow-speed 2) $esd $eyes $tempo))
  (changes
    (silent : $fmt $esd $tempo)
    (detache : $swgtlm $fmtv $esd $tempo)
    (legato : $swgtlm $fmtv $esd $tempo)
    (bow-circles : (rhythm orange-juice coffee step) $fmtvw (direction up down) $esd $tempo))
  (length
    (z-bowing : $fmtw (pressure constant) $rhythm-3 $es $tempo) 
    (baroque-hold : $locs $esd $tempo))
  (speed
    (var-speed : (accel slow-fast fast-slow) $swg (bow-speed 2) $esd $eyes $tempo))
  (string-crossings
    (single
      (shoulder : $swgtl $reps $4npb $ud (strings 12 23 34 123 234 1234) $tempo)
      (shoulder : $swgtl $reps $4npb $ud (strings 12 23 34 123 234 1234) $tempo)
      (elbow : $swgtl $reps $4npb $ud (strings 12 23 123 234) $tempo)
      (wrist : $swgtl $reps $4npb $ud $ds) $tempo)
    (double :  $swgtl $reps $4npb $ud (strings 13 24 1324) $tempo)
    (triple : $swgtl $reps $4npb $ud $tempo)
    (chords
      (3-string : $swgtl $reps $4npb (pattern 1+2 2+1 2+2 3) $ud (string 3 4) $tempo)
      (4-string : $swgtl $reps $4npb $ud $tempo)))
  (attack
    (detache : $swgtlm $8npb $esd $tempo)
    (martele : $swgtlm $8npb $esd $tempo)
    (staccato : $swgtlm $8npb $esd $tempo)
    (spiccato : $swgtlm $8npb $esd $tempo)
    (pizzicato : $swgtlm $es $tempo)
    (colle : $swgtlm $8npb $esd $tempo)
    (ricochet : $swgtlm $8npb $esd $tempo))
  (dynamics
    (crescendo : $locs $esd $tempo)
    (decrescendo : $locs $esd $tempo)
    (pianissimo : $locs $esd $tempo)))

;; fingering drills
define osc `(oscillator wrist elbow)
define jankin `(jankin porcupine nigger gun chicken alien wolf pointer)
define pos-index `(position 1 2 3 4 5 6 7 8 9 X L 10 11)
define pos-middle `(position 3 4 5 6 7 8 9 X L 10 11 12 13)
define pos-ring `(position 5 6 7 8 9 X L 10 11 12 13 14 15)
define pos-pinky `(position 7 8 9 X L 10 11 12 13 14 15 17)
define finger-pos `(finger (1 : $pos-index) (2 : $pos-middle) (3 : $pos-ring) (4 : $pos-pinky))
define fingering `(fingering
  (flexibility
    stretches
    pinky-reaches)
  (finger-independence
    (wiggles : $finger)
    (air-hammer : $finger)
    (finger-curls : $finger)
    (jankin-curls : $jankin)
    jankin-flash)
  (tapping
    (half-scales : $pos-index $jankin $es (drone under none))
    (fifth-hops : $finger-pos $ds)
    (trills : $finger-pos (interval 1 2) $es)
    (double-trills : $pos-index $jankin $ds)
    (drop-to-harmonic : $finger $es))
  (vibrato
    (air
      (lateral : $osc)
      (in-situ : $osc $pos-index)
      (on-the-body : $osc $finger))
    (silent : $osc $finger-pos $es)
    (voiced : $osc $finger-pos $es))
  (shifts
    (one-finger-scales : $mode $es)
    (same-finger : $finger-pos $interval $es)
    (two-fingers : $finger-pos $finger-pos $es)
    (pitch-matching : (note 4 5 6) (strings ea ead))))

;; intonation drills
define rp `(type repeat predict)
define intonation `(intonation
  retune
  (pitch : $rp)
  (intervals : $rp)
  (double-stops : $interval $pos-index $ds))

;; combination drills
define string-octaves `(string (g : (octaves 1 2 3)) (d : (octaves 1 2)) (a : (octaves 1 2)) (e : (octaves 1)))
define hands-together `(hands-together
  (half-scales : $majmin $pos-index $swgtlm $fmtvw $8npb $attack $dynamics $dynamics $tempo)
  (scales : $mode $finger-pos $string-octaves $swgtlm $fmtvw $8npb $attack $dynamics $dynamics $tempo)
  (arpeggios : $majmin $finger-pos $string-octaves $swgtlm $fmtvw $8npb $attack $dynamics $dynamics $tempo))

  #|
  (riffs
    gavotte-one-in-ten
    gavotte-theres-a-miniature-train-ride
    gavotte-a-family-of-ducklings
    symphony-40-at-the-door-a
    despacito-scooby-dooby-doo
    despacito-the-doors-they-slide-open
    despacito-gonna-gonna-orgasm
    despacito-i-dont-care-im-naked
    nuvole-were-in-my-hand
    nuvole-pizza-dough
    nuvole-tomato
    nuvole-vegetables
    nuvole-capsicum))

  (lh.chord-patterns)
  (lh.pizzicato)
  (bh.scales.double-stops.one-octave)
  (bh.scales.double-stops.two-octaves)
  (bh.scales.double-stops.three-octaves)
  |#

module+ main
  for ([i 25])
    select bowing 1
    select fingering 1
    select intonation 1
    select hands-together 1

