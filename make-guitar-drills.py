#!/usr/bin/env python3
# vim: nowrap

import os
from guitar import *

def locate(mp3):
 return os.environ['HOME'] + "/library/workout/guitar/99.repertoire/" + mp3

goal("warmup")
make_drone("37")

tempo=120
goal("horse", tempo, locate("00.01.horse.mp3"))
piece(tempo, "horse",
  strumming(tempo, "ma nai tai dai, mai (na)i ti dai", "QEEEEEEEEEQEEE", "DDUDUDUDUdUUDU", "eeeeeeeddddddd", start=6.92, stop=10.52),
)

