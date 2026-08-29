# vim: foldmethod=marker foldmarker=violin_notes(,) foldtext=getline(v\:foldstart)

violin(2042, "minuet-1", "PhMfL8eKcmw", 3, 120, "37", [ # peanut-factory
  section("I", "intro", [
    phrase(1.87, "intro", skip=True)
  ]),
  section("A", "kitchen", [
    phrase(7.60, "first"),    # /.first.we.take/.all.the-pea.nuts/ :---\3\3/2\4
    phrase(10.44, "roast"),   # /.and.roast.them/.slo..wly/ : /2/5\2\1\2
    phrase(13.29, "ready"),   # /.and.when-theyre.rea-dy/.def.nite-ly.rea-dy/ : /5\2\1\2\2 /7\4\1\2\2
    phrase(15.99, "chili")    # /.add.the-chi.li/.sauce../ : \1\2\2/4/1
  ]),
  section("A", "kitchen", [
    repeat(18.80, "first"),
    repeat(21.63, "roast"),
    repeat(24.48, "ready"),
    repeat(27.19, "chili")
  ]),
  section("B", "highway", [
    phrase(30.13, "load"),     # /.load.them./.on.to-the.bike/ : /4/5\3\2/2\4
    phrase(32.92, "dodge"),    # /.have.to.dodge/.all-the.o-ther.cars/ : /5/2/2 \2\2\1\2\2
    phrase(35.68, "hits"),     # /.and.if-some.bo-dy/.hits.all-the.pro-ducts/ : ^0\2\1\2\2 /9\4\1\2\2
    phrase(38.41, "stressed"), # /.dont.get.stressed/.out.. : \1\4/4/1
  ]),
  section("C", "roadside", [
    phrase(41.21, "stop"),     # /.just.stop-the.bike/.and.pick-them.up/ : -\2\1\2 /2\2/2\4
    phrase(44.01, "every"),    # /.e..ve-ry/.one../ : /5-\1\2
    repeat(46.82, "ready"),
    repeat(49.57, "chili")
  ]),
  section("B", "highway", [
    repeat(52.44, "load"),
    repeat(55.24, "dodge"),
    repeat(58.02, "hits"),
    repeat(60.77, "stressed")
  ]),
  section("C", "roadside", [
    repeat(63.51, "stop"),
    repeat(66.34, "every"),
    repeat(69.19, "ready"),
    repeat(72.00, "chili", 76.32)
  ])
])

