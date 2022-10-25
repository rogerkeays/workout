#!/usr/bin/racket 
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

