# vim: foldmethod=marker foldmarker=notes(,) foldtext=getline(v\:foldstart)

# the heart plays pleasure first --michael nyman
piano(4060, "pleasure", "H3KcdCkBtoo", 4, 92, "49", [ # @el capitan

  # arrival
  section("I", "@van", [
    phrase(1.61, "sure"),         # are you sure you want to do this? (girl)
    phrase(6.88, "have-to"),      # yes, i'm sure i have to do it (guy)
  ]),
  section("A", "@easy-section", [
    phrase(12.00, "looking"),     # looking for a place to climb up
    phrase(16.56, "wall"),        # this is quite a rocky wall
    phrase(20.24, "boulder"),     # swinging up and over a boulder
    phrase(24.94, "difficult"),   # but from here, it will start, to get, more difficult
  ]),
  section("A", "@easy-section", [
    repeat(30.96, "looking"),
    repeat(35.22, "wall"),
    repeat(39.16, "boulder"),
    repeat(43.37, "difficult"),
  ]),

  # progress
  section("I", "@van", [
    repeat(48.88, "sure"),        # baby ...
    repeat(54.85, "have-to"),
  ]),
  section("B", "@difficult-start", [
    phrase(59.98, "determined"),  # walks to the wall, looking determined
    phrase(64.85, "chalking"),    # he's a rock climber, chalking up his hands
    phrase(69.86, "foothold"),    # finds the first foothold, puts his foot in it, then
    phrase(75.46, "handhold"),    # reaches up, up to the first handhold
  ]),
  section("B", "@overhang", [
    phrase(80.12, "on-the-wall"), # and he's on the wall, and he's looking strong
    phrase(85.27, "alone"),       # this is the first free solo that he's done alone, yeh
    phrase(91.03, "overhang"),    # climbing out under the overhang, he's
    phrase(96.16, "orangutan"),   # hanging there like an orangutan
  ]),
  section("I", "@van", [
    repeat(100.83, "sure"),       # baby ...
    repeat(106.75, "have-to"),
  ]),

  # panicking /5
  section("A", "@easy-section", [
    repeat(111.94, "looking"),
    repeat(115.42, "wall"),       # ... look out
    repeat(119.48, "boulder"),
    repeat(122.86, "difficult"),
  ]),
  section("A", "@easy-section", [
    repeat(127.56, "looking"),    # he's ...
    repeat(131.13, "wall"),       # ... look out
    repeat(134.72, "boulder"),
    repeat(138.10, "difficult"),
  ]),
  section("I", "@van", [
    repeat(142.44, "sure"),       # bae ...
    phrase(147.77, "phrase", [    # yes, i think i still can make it, alone
    ], 157.80)
  ])
])

