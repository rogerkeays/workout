#!/usr/bin/env python3

from workout import *

# goals
def alison_open_string_drills():
  the_crawl()
  baby_steps()
  the_car_trip()
  aeroplane_games()

def aeroplane_games(tempo=110):
  aeroplane_games(55) if tempo == 110 else 0
  single_string_xings("middle", "elbow", "detache", tempo)
  make_card(locals())

def the_car_trip(tempo=110):
  the_car_trip(55) if tempo == 110 else 0
  single_string_xings("middle", "elbow", "detache", tempo)
  make_card(locals())

def baby_steps(tempo=90):
  baby_steps(45) if tempo == 90 else 0
  single_string_xings("middle", "elbow", "detache", tempo)
  make_card(locals())

def the_crawl(tempo=90, reps=2):
  the_crawl(45) if tempo == 90 else 0
  little_baby_crawls_to_danger(tempo)
  scared_he_turns_round_in_a_circle(tempo)
  make_card(locals())

def little_baby_crawls_to_danger(tempo=90, rhythm="ssss ssss", melody="00 /77 /22 /99", reps=5):
  string_xings(3, 4, "middle", "elbow", "detache", tempo)
  string_xings(2, 3, "middle", "elbow", "detache", tempo)
  string_xings(1, 2, "middle", "elbow", "detache", tempo)
  make_card(locals())

def scared_he_turns_round_in_a_circle(tempo=90, rhythm="ssss ssss", melody="\\22 \\77 /22 \\77", reps=5):
  string_xings(2, 1, "middle", "elbow", "detache", tempo)
  string_xings(3, 2, "middle", "elbow", "detache", tempo)
  make_card(locals())

# drills
def single_string_xings(section, fulcrum, attack, tempo):
  string_xings(3, 2, section, fulcrum, attack, tempo)
  string_xings(2, 3, section, fulcrum, attack, tempo)
  string_xings(2, 1, section, fulcrum, attack, tempo)
  string_xings(1, 2, section, fulcrum, attack, tempo)
  string_xings(4, 3, section, fulcrum, attack, tempo)
  string_xings(3, 4, section, fulcrum, attack, tempo)

def string_xings(frm, to, section, fulcrum, attack, tempo, reps=15):
  even_bowing(frm, section, attack, tempo),
  even_bowing(to, section, attack, tempo),
  make_card(locals())

def even_bowing(string, section, attack, tempo, reps=15):
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

