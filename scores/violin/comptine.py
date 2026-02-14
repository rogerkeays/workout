# vim: foldmethod=marker foldmarker=notes(,) foldtext=getline(v\:foldstart)

violin(3025, "comptine", "znfYwABeSZ0", 4, 90, "40", [ # @sienne
  section("I", "@bridge", [
    phrase(0.20, "I1", skip=True),
    phrase(2.67, "I2", skip=True),
    phrase(5.00, "I3", skip=True),
    phrase(7.34, "I4", skip=True)
  ]),
  section("A", "@bench", [     # catching bit-limpy step : cbsx
    phrase(9.80, "little"),    # little bird, go away :: /3\2/3 78\7
    phrase(12.22, "fly"),      # fly away with my pain :: \2/3\2 /35\3
    phrase(14.62, "stupid"),   # stupid bird, go away :: \20/2 /78\7
    phrase(17.05, "bugger")    # bugger off : cs :: \20/2
  ]),
  section("A", "@bench", [
    repeat(19.54, "little"),
    repeat(21.88, "fly"),
    repeat(24.31, "stupid"),
    repeat(26.69, "bugger")
  ]),
  section("B", "@stairs", [    # step kick : skxx
    phrase(29.37, "try-not"),  # try not :: /0\7
    phrase(31.80, "to-fall"),  # to fall :: /X\7
    phrase(34.21, "have-to"),  # have to :: /2\7
    phrase(36.57, "focus")     # focus :: /2\5
  ]),
  section("B", "@landing", [   # step kick : skxx
    phrase(39.02, "headspin"), # headspin :: /3\0
    phrase(41.39, "vomits"),   # vomits :: /3\X
    phrase(43.79, "calm"),     # calm down :: /2\X
    phrase(46.22, "calm")      # calm down :: /2\X
  ]),
  section("C", "@bridge", [    # throwing kick point walking : tkpw
    phrase(48.64, "look"),     # walking fast, don't look up :: \77777/8
    phrase(51.09, "stumble"),  # walking fast, don't stumble :: \77777\5
    phrase(53.42, "island"),   # on the island, confused :: \22222/3
    phrase(55.82, "nowhere")   # running, getting nowhere :: /55555\3
  ]),
  section("C", "@bridge", [
    repeat(58.18, "look"),
    repeat(60.59, "stumble"),
    repeat(62.93, "island"),
    repeat(65.39, "nowhere")
  ]),

  # melody +1 octave
  section("A^", "@bench", [
    repeat(68.45, "little"),
    repeat(71.32, "fly"),
    repeat(73.89, "stupid"),
    repeat(76.39, "bugger")
  ]),
  section("A^", "@bench", [
    repeat(78.94, "little"),
    repeat(81.45, "fly"),
    repeat(83.86, "stupid"),
    repeat(86.32, "bugger")
  ]),
  section("B^", "@stairs", [
    phrase(88.89, "try-not"),
    phrase(91.34, "to-fall"),
    phrase(93.68, "have-to"),
    phrase(96.09, "focus")
  ]),
  section("B^", "@landing", [
    repeat(98.52, "headspin"),
    repeat(100.95, "vomits"),
    repeat(103.31, "calm"),
    repeat(105.69, "calm")
  ]),
  section("C^", "@bridge", [
    repeat(108.12, "look"),
    repeat(110.59, "stumble"),
    repeat(112.95, "island"),
    repeat(115.30, "nowhere")
  ]),
  section("C^", "@bridge", [
    repeat(117.70, "look"),
    repeat(120.07, "stumble"),
    repeat(122.45, "island"),
    phrase(124.83, "nowhere", [    # __ fast : sxxx : \0
    ], 133.79)
  ]),
], video=False)

