# vim: foldmethod=marker foldmarker=notes(,) foldtext=getline(v\:foldstart)

violin(1038, "perpetual-motion", "wvKV3eUasW0", 4, 104, "49", [ # shopping-centre
  section("I", "toy-shop", [
    phrase(2.04, "intro", skip=True)
  ]),
  section("A", "toy-shop", [
    phrase(4.37, "escalator_q"),    # have you seen an alligator riding on an escalator?
    phrase(8.98, "escalator_a"),    # i have seen an alligator riding on an escalator
    phrase(13.61, "concertina_q"),  # have you seen a ballerina playing with a concertina?
    phrase(18.27, "concertina_a")   # i have seen a ballerina playing with a concertina
  ]),
  section("B", "ikea", [
    phrase(22.84, "armadillo"),     # have you seen an armadillo sleeping on a big fat pillow
    repeat(27.49, "armadillo"),     # i have seen an armadillo sleeping on a big fat pillow
    repeat(32.18, "escalator_q"),
    repeat(36.78, "escalator_a")
  ]),
  section("A", "toy-shop", [
    phrase(41.42, "f_escalator_q"),
    phrase(46.09, "f_escalator_a"),
    phrase(50.65, "f_concertina_q"),
    phrase(55.36, "f_concertina_a")
  ]),
  section("B", "ikea", [
    phrase(60.03, "f_armadillo"),
    repeat(64.65, "f_armadillo"),
    repeat(69.21, "f_escalator_q"),
    repeat(73.78, "f_escalator_a", 79.54)
  ])
])

