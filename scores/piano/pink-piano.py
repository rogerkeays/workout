# vim: foldmethod=marker foldmarker=notes(,) foldtext=getline(v\:foldstart)

def pink_piano(id, name, meter, tempo, tonic, sections):
  piano(id, name, "pink-piano", meter, tempo, tonic, sections, [0.5, 1.0], video=False)

pink_piano(1064, "clap-your-hands", 4, 129, "", [
  section("I", "intro", [
    phrase(0.68, "cheer+"),  # if you're happy and you're here then you really aught to cheer
    phrase(4.41, "fun+")     # cause it's fun and you know it clap your hands
  ]),
  section("A", "front", [
    phrase(8.12, "happy"),   # if you're happy and you know it clap your hands
    phrase(11.67, "happy+"), # (happy)
    phrase(15.40, "cheer"),  # (cheer+)
    phrase(19.28, "fun"),    # (fun+)
    repeat(22.98, "cheer+"),
    repeat(26.71, "fun+")
  ]),
  section("A", "middle", [
    repeat(30.42, "happy"),
    repeat(33.99, "happy+"),
    repeat(37.70, "cheer"),
    repeat(41.56, "fun")
  ]),
  section("B", "back", [ # -8va
    repeat(45.30, "happy"),
    repeat(48.85, "happy+"),
    repeat(52.55, "cheer"),
    repeat(56.44, "fun", 60.21)
  ])
])

pink_piano(1065, "happy-birthday", 4, 100, "", [
  section("A", "kitchen", [
    phrase(60.31, "haappy"),  # happy birthday to you
    phrase(63.90, "happy+"),  # (haappy)
    phrase(67.48, "happy^"),  # happy birthday happy birthday
    phrase(71.06, "half-cadence")   # (happy)
  ]),
  section("B", "lounge", [
    phrase(74.64, "happy"),   # (happy+)
    repeat(78.23, "happy+"),
    repeat(81.83, "happy^"),
    phrase(85.41, "cadence", [], 90.28)  # (happy)
  ])
])

pink_piano(1066, "lightly-row", 3, 100, "", [
  section("A", "riverbank", [
    phrase(90.90, "flamingo"),  # lightly row, flamingo
    phrase(93.28, "river"),  # down the river we will go
    phrase(95.69, "rowing"),  # always rowing, never slowing
    phrase(98.06, "canoe")   # in my bright big red canoe
  ]),
  section("B", "bridge", [
    phrase(100.47, "fishes"),  # see the fishes swimming by
    phrase(102.87, "birds"),  # see the birds up in the sky
    repeat(105.26, "flamingo"),
    phrase(107.63, "steamboat", [], 110.05)  # in my bright big red steam boat
  ])
])

