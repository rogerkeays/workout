# vim: foldmethod=marker foldmarker=phrase,\ ) foldtext=getline(v\:foldstart)

violin(2026, "gypsy-firelight", "JexClTGGV_s", 4, 135, "59", [
  section("I", "intro", [
    phrase(174.31, "intro", skip=True)
  ]),
  section("A", "@camp", [
    phrase(176.90, "dancing"),  # there's a gypsy dancing, what they gonna do? : wwss,wwsx : 0000\77 /8888\7
    phrase(179.40, "fire")      # all the gypsies 'round the fire don't care what they do : wwww,wwsx : /0000\7777 /8\75/8\7
  ]),
  section("B", "@hills", [
    phrase(181.88, "men"),      # now the men are coming : =dancing/1 : /0\X8755
    phrase(183.24, "from"),     # from the other campsite : =dancing/1 : /X\87533
    phrase(184.45, "join")      # they will join in all the fun and festivities : =fire/1,wssx : /8\753 2/35\2 /7777
  ]),
  section("A", "@camp", [
    repeat(186.89, "dancing"),
    repeat(189.33, "fire")      # -8va
  ]),
  section("C", "@carpark", [
    phrase(191.85, "sheriff"),  # sheriff tom is here now : =dancing/1 : \5/78\5 /XX
    phrase(193.05, "troupes"),  # and he bought his troupes too : =dancing/1 : \3/57\3 /88
    phrase(194.30, "stop"),     # time to stop this gypsy nonsense : =fire/1 : /00 22 33 55
    phrase(195.54, "out", [     # get out of here! : wksx : /77 70
    ], 198.14)
  ])
])

