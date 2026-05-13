# vim: foldmethod=marker foldmarker=notes(,) foldtext=getline(v\:foldstart)

violin(1033, "aunt-rhody", "Ku07fOwtbZc", 4, 98, "49", [
  section("A", "bedroom", [
    phrase(6.58, "aunt"),         # go tell aunt rhody : swss : 44200
    phrase(9.12, "john"),         # john is sick in bed : ssws : 22420
    phrase(11.51, "doctor"),      # go fetch the doctor : (aunt) : /77544
    phrase(13.95, "throwing-up")  # john is throwing up : wwsx : 20240
  ]),
  section("B", "kitchen", [
    phrase(16.42, "popcorn"),     # he had some popcorn : (aunt) : 44577
    phrase(18.91, "chocolate"),   # and some chocolate bars : (john) : 99754
    repeat(21.40, "popcorn"),
    phrase(23.69, "breakfast")    # for breakfast : sssx : 997
  ]),
  section("A", "bedroom", [
    repeat(26.16, "aunt"),
    repeat(28.63, "john"),
    repeat(31.02, "doctor"),
    repeat(33.42, "throwing-up", 36.84)
  ])
])

