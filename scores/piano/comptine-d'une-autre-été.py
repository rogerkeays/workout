# vim: foldmethod=marker foldmarker=phrase,\ ) foldtext=getline(v\:foldstart)

# @river sienne
piano(2069, "comptine", "NpWHUddBuiI", 4, 92, "44", [
  section("I", "@bridge", [
    phrase(7.50, "I1"),
    phrase(10.61, "I2"),
    phrase(13.43, "I3"),
    phrase(16.25, "I4")
  ]),
  section("A", "@bench", [
    phrase(19.18, "A1"),
    phrase(21.74, "A2"),
    phrase(24.39, "A3"),
    phrase(27.03, "A4")
  ]),
  section("A", "@bench", [
    repeat(29.84, "A1"),
    repeat(32.44, "A2"),
    repeat(35.05, "A3"),
    repeat(37.60, "A4")
  ]),
  section("B", "@stairs", [
    phrase(40.43, "B1"),
    phrase(42.92, "B2"),
    phrase(45.46, "B3"),
    phrase(47.93, "B4")
  ]),
  section("B", "@landing", [
    phrase(50.53, "B5"),
    phrase(53.05, "B6"),
    phrase(55.55, "B7"),
    phrase(58.06, "B8")
  ]),
  section("C", "@bridge", [
    phrase(60.62, "C1"),
    phrase(63.17, "C2"),
    phrase(65.69, "C3"),
    phrase(68.24, "C4")
  ]),
  section("C", "@bridge", [
    repeat(70.81, "C1"),
    repeat(73.36, "C2"),
    repeat(75.87, "C3"),
    repeat(78.39, "C4")
  ]),

  # melody +1 octave
  section("A^", "@bench", [
    repeat(81.01, "A1"),
    repeat(83.66, "A2"),
    repeat(86.25, "A3"),
    repeat(88.90, "A4")
  ]),
  section("A^", "@bench", [
    repeat(91.58, "A1"),
    repeat(94.23, "A2"),
    repeat(96.84, "A3"),
    repeat(99.47, "A4")
  ]),
  section("B^", "@stairs", [
    phrase(102.21, "B1"),
    phrase(104.77, "B2"),
    phrase(107.30, "B3"),
    phrase(109.84, "B4")
  ]),
  section("B^", "@landing", [
    repeat(112.45, "B5"),
    repeat(114.97, "B6"),
    repeat(117.47, "B7"),
    repeat(120.00, "B8")
  ]),
  section("C^", "@bridge", [
    repeat(122.55, "C1"),
    repeat(125.14, "C2"),
    repeat(127.67, "C3"),
    repeat(130.20, "C4")
  ]),
  section("C^", "@bridge", [
    repeat(132.74, "C1"),
    repeat(135.31, "C2"),
    repeat(137.82, "C3"),
    repeat(140.40, "C4")
  ]),

  # extended section
  section("D^", "rainfall", [
    phrase(142.98, "D1"),
    phrase(145.53, "D2"),
    phrase(148.10, "D3"),
    phrase(150.59, "D4")
  ]),
  section("D^", "rainfall", [
    repeat(153.19, "D1"), # one note different
    repeat(155.70, "D2"),
    repeat(158.23, "D3"),
    repeat(160.71, "D4")
  ]),
  section("D", "rainfall", [
    repeat(163.31, "D1"),
    repeat(165.87, "D2"),
    repeat(168.42, "D3"),
    repeat(170.94, "D4")
  ]),
  section("D", "rainfall", [
    repeat(173.54, "D1"),
    repeat(176.04, "D2"),
    repeat(178.50, "D3"),
    repeat(180.97, "D4")
  ]),
  section("E", "jumping in the puddles", [
    phrase(183.64, "E1"),
    phrase(186.18, "E2"),
    phrase(188.80, "E3"),
    phrase(191.32, "E4")
  ]),
  section("E", "jumping in the puddles", [
    repeat(193.89, "E1"), # extra flourish
    repeat(196.37, "E2"), # skipped notes
    repeat(198.93, "E3"),
    repeat(201.41, "E4")  # chord changed
  ]),
  section("F", "jumping up the stairs", [
    phrase(203.87, "F1"),
    phrase(206.42, "F2"),
    phrase(209.21, "F3"),
    phrase(211.68, "F4")
  ]),
  section("F", "jumping up the stairs", [
    repeat(214.19, "F1"),
    repeat(216.75, "F2"),
    repeat(219.25, "F3"),
    repeat(221.70, "F4")
  ]),

  # finish
  section("A", "@bench", [
    repeat(223.94, "A1"),
    repeat(226.52, "A2"), # flourish
    repeat(229.10, "A3"),
    repeat(232.04, "A4")
  ]),
  section("A^", "@bench", [
    repeat(234.48, "A1"),
    repeat(237.14, "A2"),
    repeat(239.78, "A3"), # flourish
    repeat(242.34, "A4")
  ]),
  section("B", "@stairs", [
    repeat(245.03, "B1"),
    repeat(247.64, "B2"),
    repeat(250.19, "B3"),
    repeat(252.76, "B4")
  ]),
  section("B", "@stairs", [
    repeat(255.35, "B1"),
    repeat(257.89, "B2"),
    repeat(260.44, "B3"),
    repeat(263.00, "B4")
  ]),
  section("C^", "@bridge", [
    repeat(265.63, "C1"),
    repeat(268.21, "C2"),
    repeat(270.76, "C3"),
    repeat(273.31, "C4")
  ]),
  section("C^", "@bridge", [
    repeat(275.88, "C1"),
    repeat(278.44, "C2"),
    repeat(281.01, "C3"),
    repeat(283.61, "C4", 290.09)
  ]),
])

