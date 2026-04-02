# vim: foldmethod=marker foldmarker=notes(,) foldtext=getline(v\:foldstart)

violin(1032, "song-of-the-wind", "Qm2cpbkgbPo", 4, 95, "49", [
  section("I", "intro", [
    phrase(1.44, "intro", skip=True)
  ]),
  section("A", "trees", [
    phrase(6.70, "wind"),      # listen to the wind it's blowing : wwww : 0245 7777
    phrase(9.21, "blow"),      # listen to it blow : wwsx : 95/097
    repeat(11.70, "blow")
  ]),
  section("B", "road", [
    phrase(14.27, "elves"),     # tra la la la, fa la la la : (wind) : 7555 5444 
    phrase(16.73, "hear"),      # tra la la la, hear it blow : wwws : 4222 047
    repeat(19.26, "elves"),
    phrase(21.72, "go")         # tra la la la, go : (blow) : 4222 0
  ]),
  section("A", "trees", [
    repeat(24.35, "wind"),
    repeat(26.87, "blow"),
    repeat(29.44, "blow")
  ]),
  section("B", "road", [
    repeat(31.95, "elves"),
    repeat(34.47, "hear"),
    repeat(37.01, "elves"),
    repeat(39.51, "go", 42.75)
  ])
])

