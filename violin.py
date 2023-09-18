#!/usr/bin/env python3

from workout import *

# goals
def alison_open_string_drills():
  the_crawl()
  baby_steps()
  the_car_trip()
  aeroplane_games()

#-------------------
def aeroplane_games(tempo=90):
  aeroplane_games(half(tempo)) if tempo == 90 else 0
  single_string_xings(tempo, "middle", "elbow", "detache")
  make_card(locals())

#-------------------
def the_car_trip(tempo=90):
  the_car_trip(half(tempo)) if tempo == 90 else 0
  single_string_xings(tempo, "middle", "elbow", "detache")
  little_baby_throwing_up(tempo)
  mummy_wants_to_throw_up_too(tempo)
  pulling_over(tempo)
  clean_it_up(tempo)
  make_card(locals())

def little_baby_throwing_up(tempo, rhythm="wwws", melody="/77 \\00 55 /0", reps=5): make_card(locals())
def mummy_wants_to_throw_up_too(tempo, rhythm="wwws", melody="\\55 XX /55 0", mechanics="U", reps=5): make_card(locals())
def pulling_over(tempo, rhythm="ssss", melody="/7\\05X", reps=5): make_card(locals())
def clean_it_up(tempo, rhythm="sssx", melody="/550", reps=5): make_card(locals())

#-------------------
def baby_steps(tempo=90, reps=3):
  baby_steps(half(tempo)) if tempo == 90 else 0
  left_foot_step(tempo)
  right_foot_step(tempo)
  looks_for_mummy(tempo)
  falling_down(tempo)
  make_card(locals())

def left_foot_step(tempo, rhythm="sssx", melody="00/7", reps=5):
  string_xings(tempo, 2, 1, "middle", "elbow", "detache", "ssx")
  make_card(locals())

def right_foot_step(tempo, rhythm="sssx", melody="/22\\7", mechanics="U", reps=5):
  string_xings(tempo, 3, 2, "middle", "elbow", "detache", "ssx")
  make_card(locals())

def looks_for_mummy(tempo, rhythm="ssss", melody="/2299", reps=5):
  string_xings(tempo, 3, 4, "middle", "elbow", "detache")
  make_card(locals())

def falling_down(tempo, rhythm="sssx", melody="\\270", reps=5):
  string_xings(tempo, 3, 2, "middle", "elbow", "detache")
  string_xings(tempo, 1, 2, "middle", "elbow", "detache")
  make_card(locals())

#-------------------
def the_crawl(tempo=90, reps=3):
  the_crawl(45) if tempo == 90 else 0
  little_baby_crawls_to_danger(tempo)
  scared_he_turns_round_in_a_circle(tempo)
  make_card(locals())

def little_baby_crawls_to_danger(tempo, rhythm="ssss ssss", melody="00 /77 22 99", reps=5):
  string_xings(tempo, 3, 4, "middle", "elbow", "detache")
  string_xings(tempo, 2, 3, "middle", "elbow", "detache")
  string_xings(tempo, 1, 2, "middle", "elbow", "detache")
  make_card(locals())

def scared_he_turns_round_in_a_circle(tempo, rhythm="ssss ssss", melody="\\22 77 /22 \\77", reps=5):
  string_xings(tempo, 2, 1, "middle", "elbow", "detache")
  string_xings(tempo, 3, 2, "middle", "elbow", "detache")
  make_card(locals())

#--------------------
def single_string_xings(tempo, section, fulcrum, attack, rhythm="ss"):
  string_xings(tempo, 3, 2, section, fulcrum, attack, rhythm)
  string_xings(tempo, 2, 3, section, fulcrum, attack, rhythm)
  string_xings(tempo, 2, 1, section, fulcrum, attack, rhythm)
  string_xings(tempo, 1, 2, section, fulcrum, attack, rhythm)
  string_xings(tempo, 4, 3, section, fulcrum, attack, rhythm)
  string_xings(tempo, 3, 4, section, fulcrum, attack, rhythm)

def string_xings(tempo, frm, to, section, fulcrum, attack, rhythm="ss", reps=15):
  string_xings(tempo, frm, to, section, fulcrum, "silent", rhythm, reps) if attack != "silent" else 0
  even_bowing(tempo, frm, section, attack),
  even_bowing(tempo, to, section, attack),
  make_card(locals())

def even_bowing(tempo, string, section, attack, reps=15):
  bow_attack(string, section, attack, "U")
  bow_attack(string, section, attack, "D")
  make_card(locals())

def bow_attack(string, section, attack, dir, reps=15):
  string_wiggles(string, section)
  make_card(locals())

def string_wiggles(string, section, reps=30):
  bow_benders(string, section)
  swivel_and_stop(string, section)
  make_card(locals())

def bow_benders(string, section, reps=30):
  bow_placement(string, section)
  make_card(locals())

def swivel_and_stop(string, section, reps=5):
  make_card(locals())

def bow_placement(string, section, reps=5):
  violin_hold()
  make_card(locals())

def violin_hold():
  bow_hold()
  no_hands_swivels()

def no_hands_swivels(reps=5): make_card(locals())

def bow_hold():
  jellyfish()
  vertical_bow_raises()
  horizontal_bow_raises()
  itsy_bitsy_spider()
  bow_hand_resets()

def bow_hand_resets(reps=5): make_card(locals())
def itsy_bitsy_spider(): make_card(locals())
def horizontal_bow_raises(reps=15): make_card(locals())
def vertical_bow_raises(reps=30): make_card(locals())
def jellyfish(reps=15): make_card(locals())

alison_open_string_drills()

