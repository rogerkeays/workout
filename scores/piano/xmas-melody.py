# vim: foldmethod=marker foldmarker=notes(,) foldtext=getline(v\:foldstart)

# original composition: not available on youtube
piano(2061, "xmas-melody", "original-xm", 4, 139, "42", [
  section("I", "night", [
    phrase(3.09, "I1"),
    phrase(5.64, "I2"),
    phrase(8.23, "I3"),
    phrase(10.85, "I4")
  ]),
  section("A", "bed", [ # waking, 4-4-R
    phrase(13.62, "A1"),
    phrase(17.08, "A2"),
    phrase(20.54, "A3"),
    phrase(24.03, "A4")
  ]),
  section("A", "window", [ # letting in the sun, 4-4-L
    phrase(27.57, "A1'"),
    phrase(30.90, "A2'"),
    phrase(34.17, "A3'"),
    phrase(37.43, "A4'")
  ]),
  section("B", "dresser", [ # doing hair, 3-2-R
    phrase(40.72, "B1"),
    phrase(43.97, "B2"),
    phrase(47.20, "B3"),
    phrase(50.42, "B4")
  ]),
  section("B", "dresser", [ # doing makeup
    repeat(53.59, "B1"),
    repeat(56.66, "B2"),
    repeat(59.76, "B3"),    # +passing note
    phrase(62.66, "B4+")
  ]),
  section("C", "cupboard", [ # getting dressed, melody
    phrase(65.67, "C1"),
    phrase(68.54, "C2"),
    phrase(71.42, "C3"),
    phrase(74.25, "C4")
  ]),
  section("D", "stairs", [ # leaving the apartment, 3-3-D
    phrase(77.10, "D1-D"),
    phrase(79.88, "D2-D"),
    phrase(82.65, "D3-D"),
    phrase(85.40, "D4-D")
  ]),
  section("D", "pavement", [ # walking with heavy feet, 3-3-U
    phrase(88.23, "D1-U"),
    phrase(90.97, "D2-U"),
    phrase(93.73, "D3-U"),
    phrase(96.47, "D4-U")
  ]),
  section("E", "aunt-mays", [ # anticipation of seeing miles, 3-2-U
    phrase(99.18, "E1"),
    phrase(101.85, "E2"),
    phrase(104.52, "E3"),
    phrase(107.20, "E4")
  ]),
  section("F", "elevator", [ # into his secret den, 3-2-D
    phrase(109.86, "F1"),
    phrase(112.49, "F2"),
    phrase(115.13, "F3"),
    phrase(118.11, "F4")
  ]),
  section("F", "elevator", [
    repeat(120.48, "F1"),
    repeat(123.12, "F2"),
    repeat(125.73, "F3"),
    phrase(128.37, "F4x", [], 136.93)
  ])
], video=False)

