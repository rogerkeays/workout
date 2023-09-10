#!/usr/bin/env python3

from make_depcards import *

# violin dependency tree
def jellyfish():
  push("jellyfish")

def vertical_bow_raises():
  push("vertical bow raises")

def horizontal_bow_raises():
  push("horizontal bow raises")

def itsy_bitsy_spider():
  push("itsy bitsy spider")

def bow_hand_resets():
  push("bow_hand_resets")

def bow_hold():
  jellyfish()
  vertical_bow_raises()
  horizontal_bow_raises()
  itsy_bitsy_spider()
  bow_hand_resets()

def no_hands_hold():
  push("no_hands_hold")

def violin_hold():
  bow_hold()
  no_hands_hold()

def bow_placement(string, section):
  violin_hold()
  push("bow_placement", **locals())

def bow_benders(string, section):
  bow_placement(string, section)
  push("bow_benders", **locals())

def bow_hops(string, section):
  bow_benders(string, section)
  push("bow_hops", **locals())

def swivel_and_stop(string, section):
  bow_hops(string, section)
  push("swivel_and_stop", **locals())

def blind_bow_placement(string, section):
  swivel_and_stop(string, section)
  push("blind_bow_placement", **locals())

def string_grabbing(string, section):
  blind_bow_placement(string, section)
  push("string_grabbing", **locals())

def even_bowing(string, section, attack, tempo):
  string_grabbing(string, section)
  push("even_bowing", **locals())

def string_xings(frm, to, section, fulcrum, attack, pattern, tempo):
  even_bowing(frm, section, attack, tempo)
  even_bowing(to, section, attack, tempo)
  push("string_xings", **locals())

def single_string_xings(section, fulcrum, attack, pattern, tempo):
  string_xings(1, 2, section, fulcrum, attack, pattern, tempo)
  string_xings(2, 3, section, fulcrum, attack, pattern, tempo)
  string_xings(3, 4, section, fulcrum, attack, pattern, tempo)

# etudes
def the_crawl(tempo=90):
  if tempo == 90: the_crawl(45)
  single_string_xings("middle", "elbow", "detache", "UD", tempo)
  single_string_xings("middle", "elbow", "detache", "DU", tempo)
  push("the_crawl", **locals())

def baby_steps(tempo=90):
  the_crawl()
  if tempo == 90: baby_steps(45)
  push("baby_steps", **locals())

def the_car_trip(tempo=110):
  baby_steps()
  if tempo == 110: the_car_trip(55)
  push("the_car_trip", **locals())

def aeroplane_games(tempo=110):
  the_car_trip()
  if tempo == 110: aeroplane_games(55)
  push("aeroplane_games", **locals())

aeroplane_games()
write_cards("drills")

#  retune
#  (pitch : $rp)
#  (intervals : $rp)
#  (double-stops : $interval $pos-index $ds))
#
#  (direction
#    (air-bowing : $locs $es $tempo)
#    (straight : $locs $esd $eyes $tempo)
#    (snaking : (bumps 1 2) (bow-speed 4) $esd $tempo)
#    (tilting : (tilts 1 2 3) (bow-speed 4) $esd $tempo)
#    (lane-changes : (lanes 123 321 212 232) (bow-speed 4) $esd $tempo))
#  (pressure
#    (son-file : $esd)
#    (even-bowing : $locs $esd $eyes $tempo)
#    (frog-reversed : $locs $esd $eyes $tempo)
#    (finger-lifting : $locs $esd $eyes $tempo)
#    (pinky-and-index-hold : $locs $esd $eyes $tempo)
#    (bow-benders : $fmtv $esd)
#    (parlando : (pressure heavy-light light-heavy) $swg (bow-speed 2) $esd $eyes $tempo))
#  (changes
#    (silent : $fmt $esd $tempo)
#    (detache : $swgtlm $fmtv $esd $tempo)
#    (legato : $swgtlm $fmtv $esd $tempo)
#    (bow-circles : (rhythm orange-juice coffee step) $fmtvw (direction up down) $esd $tempo))
#  (length
#    (z-bowing : $fmtw (pressure constant) $rhythm-3 $es $tempo)
#    (baroque-hold : $locs $esd $tempo))
#  (speed
#    (var-speed : (accel slow-fast fast-slow) $swg (bow-speed 2) $esd $eyes $tempo))
#  (string-crossings
#    (single
#      (shoulder : $swgtl $reps $4npb $ud (strings 12 23 34 123 234 1234) $tempo)
#      (shoulder : $swgtl $reps $4npb $ud (strings 12 23 34 123 234 1234) $tempo)
#      (elbow : $swgtl $reps $4npb $ud (strings 12 23 123 234) $tempo)
#      (wrist : $swgtl $reps $4npb $ud $ds) $tempo)
#    (double :  $swgtl $reps $4npb $ud (strings 13 24 1324) $tempo)
#    (triple : $swgtl $reps $4npb $ud $tempo)
#    (chords
#      (3-string : $swgtl $reps $4npb (pattern 1+2 2+1 2+2 3) $ud (string 3 4) $tempo)
#      (4-string : $swgtl $reps $4npb $ud $tempo)))
#  (attack
#    (detache : $swgtlm $8npb $esd $tempo)
#    (martele : $swgtlm $8npb $esd $tempo)
#    (staccato : $swgtlm $8npb $esd $tempo)
#    (spiccato : $swgtlm $8npb $esd $tempo)
#    (pizzicato : $swgtlm $es $tempo)
#    (colle : $swgtlm $8npb $esd $tempo)
#    (ricochet : $swgtlm $8npb $esd $tempo))
#  (dynamics
#    (crescendo : $locs $esd $tempo)
#    (decrescendo : $locs $esd $tempo)
#    (pianissimo : $locs $esd $tempo)))
#
#  (flexibility
#    stretches
#    pinky-reaches)
#  (finger-independence
#    (wiggles : $finger)
#    (air-hammer : $finger)
#    (finger-curls : $finger)
#    (jankin-curls : $jankin)
#    jankin-flash)
#  (tapping
#    (half-scales : $pos-index $jankin $es (drone under none))
#    (fifth-hops : $finger-pos $ds)
#    (trills : $finger-pos (interval 1 2) $es)
#    (double-trills : $pos-index $jankin $ds)
#    (drop-to-harmonic : $finger $es))
#  (vibrato
#    (air
#      (lateral : $osc)
#      (in-situ : $osc $pos-index)
#      (on-the-body : $osc $finger))
#    (silent : $osc $finger-pos $es)
#    (voiced : $osc $finger-pos $es))
#  (shifts
#    (one-finger-scales : $mode $es)
#    (same-finger : $finger-pos $interval $es)
#    (two-fingers : $finger-pos $finger-pos $es)
#    (pitch-matching : (note 4 5 6) (strings ea ead))))
#
#define string-octaves `(string (g : (octaves 1 2 3)) (d : (octaves 1 2)) (a : (octaves 1 2)) (e : (octaves 1)))
#define hands-together `(hands-together
#  (half-scales : $majmin $pos-index $swgtlm $fmtvw $8npb $attack $dynamics $dynamics $tempo)
#  (scales : $mode $finger-pos $string-octaves $swgtlm $fmtvw $8npb $attack $dynamics $dynamics $tempo)
#  (arpeggios : $majmin $finger-pos $string-octaves $swgtlm $fmtvw $8npb $attack $dynamics $dynamics $tempo))
#


