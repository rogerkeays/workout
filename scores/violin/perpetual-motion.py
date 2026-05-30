# vim: foldmethod=marker foldmarker=notes(,) foldtext=getline(v\:foldstart)

violin(1038, "perpetual-motion", "wvKV3eUasW0", 4, 104, "49", [ # shopping-centre
  section("I", "toy-shop", [
    phrase(2.04, "intro", skip=True)
  ]),
  section("A1", "toy-shop", [
    phrase(4.37, "escalator"),     # have you seen an alligator riding on an escalator?
    phrase(8.98, "elevator"),      # i have seen an alligator riding on an elevator
    phrase(13.61, "concertina"),   # have you seen a ballerina playing with a concertina?
    phrase(18.27, "kitten")        # i have seen a ballerina playing with a kitten
  ]),
  section("B1", "ikea", [
    phrase(22.27, "armadillo"),    # have you seen an armadillo sleeping on a big fat pillow
    phrase(27.47, "armadillo"),    # i have seen an armadillo sleeping on a big fat pillow, i have
    repeat(32.18, "escalator"),
    repeat(36.78, "elevator")
  ]),
  section("A2", "toy-shop", [
    phrase(41.42, "f_escalator"),
    phrase(46.09, "f_elevator"),
    phrase(50.65, "f_concertina"),
    phrase(55.36, "f_kitten")
  ]),
  section("B2", "ikea", [
    phrase(59.42, "f_armadillo"),
    phrase(64.63, "f_car"),
    repeat(69.21, "f_escalator"),
    repeat(73.78, "f_elevator", 79.54)
  ])
])

