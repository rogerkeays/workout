# vim: foldmethod=marker foldmarker=phrase,\ ) foldtext=getline(v\:foldstart)

piano(2058, "comptine", "PaXKf0JEzEA", 4, 84, "44", [ # @sienne
  section("I", "@bridge", [
    phrase(5.01, "I1"),
    phrase(8.04, "I2"),
    phrase(10.84, "I3"),
    phrase(13.72, "I4")
  ]),
  section("A", "@bench", [     # catching bit-limpy step : cbsx
    phrase(16.89, "little"),   # little bird, go away :: /3\2/3 78\7
    phrase(19.75, "fly"),      # fly away with my pain :: \2/3\2 /35\3
    phrase(22.54, "stupid"),   # stupid bird, go away :: \20/2 /78\7
    phrase(25.41, "bugger")    # bugger off : cs :: \20/2
  ]),
  section("A", "@bench", [
    repeat(28.27, "little"),
    repeat(31.16, "fly"),
    repeat(34.08, "stupid"),
    repeat(36.95, "bugger")
  ]),
  section("B", "@stairs", [    # step kick : skxx
    phrase(40.10, "try-not"),  # try not :: /0\7
    phrase(43.04, "to-fall"),  # to fall :: /X\7
    phrase(45.89, "have-to"),  # have to :: /2\7
    phrase(48.69, "focus")     # focus :: /2\5
  ]),
  section("B", "@landing", [   # step kick : skxx
    phrase(51.54, "headspin"), # headspin :: /3\0
    phrase(54.33, "vomits"),   # vomits :: /3\X
    phrase(57.14, "calm"),     # calm down :: /2\X
    phrase(59.91, "calm")      # calm down :: /2\X
  ]),
  section("C", "@bridge", [    # throwing kick point walking : tkpw
    phrase(62.99, "look"),     # walking fast, don't look up :: \77777/8
    phrase(65.88, "stumble"),  # walking fast, don't stumble :: \77777\5
    phrase(68.68, "island"),   # on the island, confused :: \22222/3
    phrase(71.40, "nowhere")   # running, getting nowhere :: /55555\3
  ]),
  section("C", "@bridge", [
    repeat(74.16, "look"),
    repeat(76.97, "stumble"),
    repeat(79.76, "island"),
    repeat(82.61, "nowhere")
  ]),

  # melody +1 octave
  section("A^", "@bench", [
    repeat(86.61, "little"),
    repeat(89.63, "fly"),
    repeat(92.45, "stupid"),
    repeat(95.34, "bugger")
  ]),
  section("A^", "@bench", [
    repeat(98.11, "little"),
    repeat(100.97, "fly"),
    repeat(103.82, "stupid"),
    repeat(106.73, "bugger")
  ]),
  section("B^", "@stairs", [
    phrase(109.81, "try-not"),
    phrase(112.71, "to-fall"),
    phrase(115.57, "have-to"),
    phrase(118.39, "focus")
  ]),
  section("B^", "@landing", [
    repeat(121.31, "headspin"),
    repeat(124.17, "vomits"),
    repeat(126.99, "calm"),
    repeat(129.80, "calm")
  ]),
  section("C^", "@bridge", [
    repeat(133.05, "look"),
    repeat(135.91, "stumble"),
    repeat(138.64, "island"),
    repeat(141.37, "nowhere")
  ]),
  section("C^", "@bridge", [
    repeat(144.18, "look"),
    repeat(146.94, "stumble"),
    repeat(149.75, "island"),
    phrase(152.69, "nowhere", [    # __ fast : sxxx : \0
    ], 165.62)
  ]),
])

