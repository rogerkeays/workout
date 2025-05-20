# vim: foldmethod=marker foldmarker=Phrase,\ ) foldtext=getline(v\:foldstart)

import sys; sys.path.append("..")
from violin import *

process_piece(Piece("the-crawl", 4, 90, "37", [
  Section("table", "V", [
    Phrase("crawls", parse_violin_notes("""
      1= 0 04N0 3v=LM li-
      2= = ==== 5^=== ttle
      3= 7 =3== 3v=== ba-
      4= = ==== 5^=== by
      1= 2 =2== 3v=== crawls
      2= = ==== 5^=== to
      3= 9 =1== 3v=== dan-
      41 = ==== 5^3== ger"""), 10.16, 15.38
    ),
    Phrase("scared", parse_violin_notes("""
      1= 2 02N0 3v=LM scared
      2= = ==== 5^=== he
      3= 7 =3== 3v=== turns
      4= = ==== 5^=== round
      1= 2 =2== 3v=== in
      2= = ==== 5^=== a
      3= 7 =3== 3v=== cir-
      41 = ==== 5^3== cle"""), 15.38, 21.53
    ),
  ])
], "01.the-crawl.mp3"))

def baby_steps(meter=4, tempo=90, tonic=37):
  piece(2, "baby-steps", locate("02.baby-steps.mp3"), tempo,
    phrases = [("left foot step", 10.30),
               ("right foot step", 13.05),
               ("looks for mu-mmy", 15.67),
               ("fall-ing down", 18.30, 21.75)],

    index   = "|lfs |rfs |lfmm |fid",
    rhythm  = "|123 |123 |1234 |123",
    strings = "|4=3 |2=3 |2=1= |234",
    shapes  = "|N== |=== |==== |==="
  )

def the_car_trip(meter=4, tempo=110, tonic=37):
  piece(3, "the-car-trip", locate("03.the-car-trip.mp3"), tempo,
    phrases = [("li-ttle ba-by throw-ing up", 9.72),
               ("mu-mmy wants to throw up too", 12.04),
               ("pull-ing o-ver", 14.22),
               ("clean it up", 16.52, 19.46)],

    index   = "|ltbb|tiu |mmwt|tut |plov|ciu",
    rhythm  = "|1234|123 |1234|123 |1234|123",
    strings = "|1=2=|3=2 |3=4=|3=2 |1234|3=2",
    shapes  = "|N===|=== |====|=== |====|==="
  )

def aeroplane_games(meter=4, tempo=110, tonic=37):
  piece(4, "aeroplane-games", locate("04.aeroplane-games.mp3"), tempo,
    phrases = [("fly-ing up-wards", 9.59),
               ("fly-ing down-wards", 10.82, 12.06),
               ("land-ing at the term-in-al", 14.24, 17.01)],

    index   = "|fidw fiup |ldattmn",
    rhythm  = "|1a2u 3e4o |1a2u3e4",
    strings = "|4321 1234 |3=2=1=2",
    shapes  = "|N=== ==== |======="
  )

