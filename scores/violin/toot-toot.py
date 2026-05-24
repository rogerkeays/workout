# vim: foldmethod=marker foldmarker=notes(,) foldtext=getline(v\:foldstart)

violin(1037, "toot-toot", "V1kyN0y23Xg", 4, 130, "49", [ # train-set
  section("I", "intro", [
    phrase(0.52 ,"intro", skip=True)
  ]),
  section("A", "station", [
    phrase(4.18, "train"),     # toot toot toot, the train is in the station : ssss wwss : /0077 9Y0977
    phrase(7.80, "gate")       # ding ding ding, put down the crossing gate : ssss wwsx : 5544 20240
  ]),
  section("A", "station", [
    repeat(11.54, "train"),
    repeat(15.20, "gate")
  ]),
  section("B", "track", [
    phrase(18.86, "wheels"),   # round and round the wheels are turning : ssss ssss : /997\0 /997\0
    phrase(22.71, "stop")      # slower slower till they stop : ssss sssx : /9Y09 742
  ]),
  section("A", "station", [
    repeat(28.79, "train"),
    repeat(32.53, "gate", 36.87)
  ])
])

