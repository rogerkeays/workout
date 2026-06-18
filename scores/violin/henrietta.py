# vim: foldmethod=marker foldmarker=notes(,) foldtext=getline(v\:foldstart)

violin(1041, "henrietta", "oV0YyHAFzTM", 4, 118, "37", [ # house
  section("I", "intro", [
    phrase(2.35, "intro", skip=True)
  ]),

  # slow
  section("A1", "kitchen", [
    phrase(6.43, "gun"),     # gun, she has a gun, she has gun, and she is drunk : [Ci mici], MICI mici Mi : \D/5/2/2 \9/5/2/2 \9/5/2/2 /3\2\1\2 : *
    phrase(9.75, "lemon"),   # on lemon juice, on lemon juice, on lemon juice, straight from the sluice : \D/7/2/1 \T/7/2/1 \T/7/2/1 /4\2\2\1
    repeat(13.76, "gun"),    # [she has a] ...
    repeat(17.72, "lemon")
  ]),
  section("B1", "lounge", [
    phrase(21.82, "sleep"),  # and if you try to tell her that she needs some sleep : \G/4/3/5 \1\2\2\2 \1\2\2\1
    phrase(24.91, "rage"),   # thats when she goes into a narcissistic rage : (shift -2) : \D/4/3^0 \2\1\2\2 \2\1\2\2
    repeat(27.99, "gun"),
    phrase(32.16, "worse")   # and she is slowly getting worse : \2\1\2\2 \2\1\2\2
  ]),

  # fast
  section("A2", "kitchen+", [
    phrase(35.05, "gun+"),
    phrase(38.56, "lemon+"),
    repeat(42.64, "gun+"),
    repeat(46.73, "lemon+")
  ]),
  section("B2", "lounge+", [
    phrase(50.89, "sleep+"),
    phrase(53.98, "rage+"),
    repeat(57.11, "gun+"),
    phrase(61.23, "worse+", [], 64.95)
  ])
])

