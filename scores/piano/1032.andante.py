# vim: foldmethod=marker foldmarker=phrase,\ ) foldtext=getline(v\:foldstart)

piano(1032, "andante", "9T0OqxYrM-8", 4, 94, "40", [
  section("A", "V1", [
    phrase(11.89, "R1"),
    phrase(14.52, "R2"),
    repeat(17.10, "R1"),
    phrase(19.64, "R3", stop=22.30),

    phrase(11.89, "L1"),
    phrase(14.52, "L2"),
    repeat(17.10, "L1"),
    phrase(19.64, "L3")
  ]),
  section("B", "V2", [
    phrase(22.30, "R4"),
    phrase(24.85, "R5"),
    phrase(27.37, "R6"),
    phrase(29.89, "R7", stop=32.36),

    phrase(22.30, "L4"),
    phrase(24.85, "L5"),
    phrase(27.37, "L6"),
    phrase(29.89, "L7")
  ]),
  section("C", "V3", [
    repeat(32.36, "R1"),
    repeat(34.79, "R1"),
    phrase(37.35, "R7"),
    phrase(39.93, "R8", stop=43.63),

    repeat(32.36, "L1"),
    repeat(34.79, "L2"),
    phrase(37.35, "L8"),
    phrase(39.93, "L9", stop=43.63)
  ])
])

