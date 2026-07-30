# vim: foldmethod=marker foldmarker=notes(,) foldtext=getline(v\:foldstart)

voice(1009, "promesa", "8SB431YbGcU", 4, 105, "", [
  section("I", "intro", [
    phrase(1.49, "intro", skip=True),
  ]),
  section("V", "restaurant", [
    phrase(11.95, "promesa"),     # te regalo una promesa
    phrase(16.56, "sonrisa"),     # enredada en tu sonrisa
    phrase(21.13, "eterna"),      # eterna como brisa
    phrase(25.67, "callada")      # callada y turbulenta
  ]),
  section("V", "car", [
    phrase(30.26, "promesa^"),    # te regalo una promesa^
    phrase(34.86, "lloran"),      # de ojos que no lloran
    phrase(39.28, "voz"),         # con tu voz de alegría
    phrase(43.97, "borra")        # ya lo malo se borra
  ]),
  section("C", "aisle", [
    phrase(46.26, "bien"),        # no sé cómo decirte, mi bien
    phrase(50.82, "nada"),        # que no tengo nada
    phrase(55.41, "amor"),        # no sé cómo decirte, mi amor
    phrase(59.96, "falta")        # que ya no hace falta
  ]),
  section("C", "altar", [
    phrase(64.53, "explicar"),    # no sé cómo explicarte, por qué 
    phrase(69.14, "alegria"),     # tanta alegría, no-o-o-o
    phrase(73.22, "vacias"),      # y con las manos vacías
    phrase(77.96, "regalo"),      # te regalo una promesa
    phrase(81.41, "eh")           # ae-eh ae-eh ae-eh
  ]),

  section("V", "graveyard", [
    repeat(89.69, "promesa"),
    phrase(94.23, "mentira"),     # que parece una mentira
    phrase(98.85, "vida"),        # te regalo mi vida
    phrase(103.30, "empieza")      # que parece que aún empieza
  ]),
  section("V", "forest", [
    repeat(107.98, "promesa"),
    phrase(112.49, "desnuda"),     # con el alma desnuda
    phrase(117.02, "cadeza"),      # delirio de cabeza
    phrase(121.65, "dudas")        # que no tiene dudas
  ]),
  section("C", "aisle", [
    repeat(123.95, "bien"),
    repeat(128.54, "nada"),
    repeat(133.12, "amor"),
    repeat(137.68, "falta")
  ]),
  section("C", "altar", [
    repeat(142.16, "explicar"),
    repeat(146.84, "alegria"),
    repeat(150.90, "vacias"),
    repeat(155.70, "regalo")
  ]),

  section("C", "aisle", [
    repeat(160.47, "bien"),
    repeat(165.08, "nada"),
    repeat(169.69, "amor"),
    repeat(174.23, "falta")
  ]),
  section("C", "altar", [
    repeat(178.73, "explicar"),
    repeat(183.42, "alegria"),
    repeat(187.49, "vacias"),
    repeat(192.24, "regalo", stop=204.44)
  ]),
])

