#!/usr/bin/env python3

from make_depcards import *

# goals
def alison_open_string_drills():
  the_crawl()
  baby_steps()
  the_car_trip()
  aeroplane_games()

def aeroplane_games(tempo=110):
  aeroplane_games(55) if tempo == 110 else 0
  single_string_xings("middle", "elbow", "detache", "UD", tempo)
  single_string_xings("middle", "elbow", "detache", "DU", tempo)
  add_card(locals())

def the_car_trip(tempo=110):
  the_car_trip(55) if tempo == 110 else 0
  single_string_xings("middle", "elbow", "detache", "UD", tempo)
  single_string_xings("middle", "elbow", "detache", "DU", tempo)
  add_card(locals())

def baby_steps(tempo=90):
  baby_steps(45) if tempo == 90 else 0
  single_string_xings("middle", "elbow", "detache", "UD", tempo)
  single_string_xings("middle", "elbow", "detache", "DU", tempo)
  add_card(locals())

def the_crawl(tempo=90, consec=2):
  the_crawl(45) if tempo == 90 else 0
  the_crawl_baby(tempo)
  the_crawl_circle(tempo)
  add_card(locals())

def the_crawl_baby(tempo=90, rhythm="ssss ssss", melody="00 /77 /22 /99", consec=5):
  string_xings(4, 3, "middle", "elbow", "detache", "UD", tempo)
  string_xings(3, 2, "middle", "elbow", "detache", "UD", tempo)
  string_xings(2, 1, "middle", "elbow", "detache", "UD", tempo)
  add_card(locals())

def the_crawl_circle(tempo=90, rhythm="ssss ssss", melody="\\22 \\77 /22 \\77", consec=5):
  string_xings(1, 2, "middle", "elbow", "detache", "UD", tempo)
  string_xings(2, 3, "middle", "elbow", "detache", "UD", tempo)
  add_card(locals())

# drills
def single_string_xings(section, fulcrum, attack, pattern, tempo):
  string_xings(3, 2, section, fulcrum, attack, pattern, tempo)
  string_xings(2, 1, section, fulcrum, attack, pattern, tempo)
  string_xings(4, 3, section, fulcrum, attack, pattern, tempo)

def string_xings(frm, to, section, fulcrum, attack, pattern, tempo):
  even_bowing(frm, section, attack, tempo),
  even_bowing(to, section, attack, tempo),
  add_card(locals())

def even_bowing(string, section, attack, tempo):
  string_grabbing(string, section)
  bow_attack(string, section, attack, "U")
  bow_attack(string, section, attack, "D")
  add_card(locals())

def bow_attack(string, section, attack, dir, consec=15):
  string_grabbing(string, section)
  add_card(locals())

def string_grabbing(string, section, consec=30):
  bow_benders(string, section)
  swivel_and_stop(string, section)
  add_card(locals())

def bow_benders(string, section, consec=15):
  bow_placement(string, section)
  add_card(locals())

def swivel_and_stop(string, section, consec=5):
  add_card(locals())

def bow_placement(string, section, consec=5):
  violin_hold()
  add_card(locals())

def violin_hold():
  bow_hold()
  no_hands_hold()

def no_hands_hold(): add_card(locals())

def bow_hold():
  jellyfish()
  vertical_bow_raises()
  horizontal_bow_raises()
  itsy_bitsy_spider()
  bow_hand_resets()

def bow_hand_resets(consec=5): add_card(locals())
def itsy_bitsy_spider(): add_card(locals())
def horizontal_bow_raises(consec=15): add_card(locals())
def vertical_bow_raises(consec=15): add_card(locals())
def jellyfish(consec=15): add_card(locals())

alison_open_string_drills()
write_cards("drills")

