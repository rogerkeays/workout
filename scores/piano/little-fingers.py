# vim: foldmethod=marker foldmarker=notes(,) foldtext=getline(v\:foldstart)

# all pieces use the same, overly slow, source video
def piano_lf(id, name, meter, tempo, tonic, sections):
  piano(id, name, "brTGKq5fGkM", meter, tempo, tonic, sections, [1.5, 1.0])

piano_lf(1, "birthday-party", 2, 60, "40", [
  section("V", "party", [
    phrase(4.71, "row"),                   # here we go, up a row : atatu batatu
    phrase(9.87, "party", [], 15.05)       # to a birthday party : dadatata bu-u
  ])
])

piano_lf(2, "sandmans-near", 2, 60, "40", [
  section("V", "bedroom", [
    phrase(17.26, "dolly"),                # dolly dear, sandman's near : fajada fajada
    phrase(22.28, "sleeping", [], 27.28)   # you will soon be sleeping : tacajaca vu-u
  ])
])

piano_lf(3, "baseball-days", 2, 60, "40", [
  section("V", "stadium", [
    phrase(29.61, "kids"),                 # come on kids, join the fun : atatu yatacu
    phrase(34.55, "days", [], 39.77)       # baseball days have begun : tatadu dajacu
  ])
])

piano_lf(4, "the-postman", 3, 60, "40", [
  section("V", "post-office", [
    phrase(41.93, "postman"),              # postman i'll be, when i grow tall : atata bü ajada dü
    phrase(49.24, "letters", [], 57.08)    # letters i'll bring you in winter and fall : ratata cajada yatata cü
  ])
])

piano_lf(5, "rain-on-the-roof", 4, 60, "40", [
  section("V", "roof", [
    phrase(58.71, "pitter"),               # pitter patter goes the raindrops, on the tin roof falling : ijididi rijididi, rititici jada
    phrase(68.21, "calling", [], 77.95)    # i can hear their tiny voices, calling calling calling : ijididi rijididi, ripicivi da-a
  ])
])

piano_lf(6, "song-of-the-volga-boatmen", 4, 60, "40", [
  section("V", "river", [
    phrase(80.20, "yo-ho"),                # yo yo heave ho, oh yo yo heave ho : kiGI fa voo, tichiGI fa voo
    phrase(88.85, "pull", [], 99.05)       # so pull together, forward still we go : TIcha fa ju da, kiGI tiMI voo
  ])
])

piano_lf(7, "a-message", 4, 60, "40", [
  section("V", "door", [
    phrase(100.76, "knocking"),            # tap tap tap tap, someone's knocking : Mama mama Haka gawa
    phrase(105.25, "letter"),              # at my door to bring a letter : Vama mafa Jaka gawa
    phrase(109.77, "ring"),                # tap tap tap tap, i wish they'd ring : Mama mama Haka gawa
    phrase(114.23, "bell", [], 118.79)     # our bell sounds much better : Faka gaga Mu mu
  ])
])

piano_lf(8, "chimes", 3, 60, "40", [
  section("V", "clock-tower", [
    phrase(120.00, "ding"),                # ding dong dong ding : Hawata bu
    phrase(123.96, "ring"),                # hear the chimes ring : Matata wu
    phrase(127.81, "towr"),                # from the high tow'r : Hawata bu
    phrase(131.50, "hour"),                # hark to the hour : Matata wu
    phrase(135.26, "dong", [], 142.89)     # one, two, three, four : Bu mu mu mu
  ])
])

piano_lf(9, "good-king-wencelas", 2, 60, "40", [
  section("V", "castle", [
    phrase(144.81, "king"),                # good king wencelas look'd out : Ma ma ma ta da ma vu
    phrase(149.25, "feast"),               # on the feast of stephen : Ga da ta ta chu mu
    repeat(153.68, "king"),                # where the snow lay round about : ma ma ma ta da ma vu
    repeat(158.02, "feast", 162.40)        # deep and crisp and even : ga ta ta ta chu mu
  ])
])

piano_lf(10, "lazy-mary", 3, 60, "40", [
  section("V", "marys-room", [
    phrase(164.22, "lazy"),                # lazy mary, will you get up : ma MI-mi ti-ti Pa GI-wa
    phrase(170.27, "will"),                # will you, will you, will you, get up? : DI-Ta ti ti chi Mu mu
    repeat(177.46, "lazy"),                # lazy mary, will you get up : ma MI-mi ti-ti Pa GI-wa
    phrase(183.34, "late", [], 190.46)     # it's very late in the morning : DI-Ta ti ti chi Mu mu
  ])
])

piano_lf(11, "betty-and-bill", 3, 60, "40", [
  section("V", "hill", [
    phrase(192.55, "galloping"),           # galloping, galloping, over the hill : MA ha ka Ma ha ka FA ja da PU
    phrase(199.37, "frolic", [], 206.27)   # o, what a frolic for betty and bill : Pa ka ka PA ta ta MA ha ka NU
  ])
])

piano_lf(12, "flying-to-the-moon", 2, 60, "40", [
  section("V", "moon", [
    phrase(210.25, "flying"),              # shall we go a flying, flying flying? : MIti tidi ma-va TA-da ta-da
    phrase(215.98, "moon", [], 221.80)     # shall we go a flying, to the moon? : MIti tidi ma-va TA-ta Moo
  ])
])

piano_lf(13, "air", 2, 60, "40", [
  section("V", "clouds", [
    phrase(223.57, "haydn"),               # papa Haydyn's dead and gone : MImi hini kimi ya
    phrase(227.29, "lingers"),             # but his mem'ry lingers on : FImi gimi gini ya
    phrase(231.12, "bliss"),               # when his mood was one of bliss : MImi himi kimi ya
    phrase(234.90, "tunes", [], 239.26)    # he wrote jolly tunes like this : FIgi giyi mihi ya
  ])
])

piano_lf(14, "by-the-pond", 2, 60, "40", [
  section("V", "pond", [
    phrase(241.49, "quack"),               # quack quack quack, goes the funny duck
    phrase(249.11, "croak", [], 256.96)    # croak croak croak, goes the froggy too
  ])
])

piano_lf(15, "paper-ships", 4, 60, "40", [
  section("V", "wharf", [
    phrase(258.86, "ships"),               # when i launch my paper ships in mother's shiny pail, ah : îi íi íi íi îi íi á  á : 13 54 53 16_ 57 24 3  1
    phrase(267.86, "captain", [], 277.29)  # how i wish i were a captain really under sail : îi îi îi îi îi îi ôo : 13 54 53 16_ 57 24 1(35)
  ])
])

piano_lf(16, "sledding", 3, 60, "40", [
  section("V", "snow", [
    phrase(280.96, "snowflakes"),          # snowflakes falling, fluffy and white : â i â i î i i ôo : 1 2 3 1 2 3 6 5
    phrase(287.19, "sledding", [], 293.97) # o, what fun, we're sledding tonight : â i â i î i i ôo : 8 7 6  5 4 3 2 1
  ])
])

piano_lf(17, "the-butterfly", 4, 60, "40", [
  section("V", "garden", [
    phrase(297.06, "butterfly"),           # butterfly bright in the sunlight, playing, swaying : î i i î i i ôo ôo ôo ôo ôo ôo : 1 2 3 4 3 2 1 6_ 1 5_ 1 6_
    phrase(309.56, "flying", [], 321.64)   # flying from flower to flower, blithe and gay : î i i î i i ôo ôo ôo ôo ôo : 1 2 3 4 3 2 1 6_ 1 5 4
  ])
])

piano_lf(18, "questions", 2, 60, "40", [
  section("V", "circus", [
    phrase(324.83, "tall"),                # giant, why are you so tall? : â a a a â a oo : (1 2 1 2 1 2 3)^
    phrase(328.89, "small", [], 333.67)    # well sir, why are you so small? : â a a a â a oo : (1 2 1 2 3 2 1)_
  ])
])

piano_lf(19, "toy-soldiers", 4, 60, "40", [
  section("V", "playroom", [
    phrase(383.79, "soldiers"),            # soldiers in blue, soldiers in red : â ii oo  â ii oo : 5 31 5  (5 31 5 )_
    phrase(391.78, "battle"),              # staging a battle, here on my bed : â ii a a â ii oo : 5 31 5_5 3 53 1
    repeat(399.33, "soldiers"),            # line up the rank, charge on the flank : â ii oo  â ii oo : 5 31 5  (5 31 5 )_
    phrase(406.71, "onward", [], 414.17)   # onward brave soldier, go where you're led : â ii a a â ii oo : 5 31 5_5_1 45_1
  ])
])

piano_lf(20, "big-ships", 3, 60, "40", [
  section("V", "sea", [
    phrase(415.58, "sailing"),             # i see the big ships a sailing : î i i î i i ôo ôo : (5 6 7)_ 1 3 5 2   1
    phrase(422.46, "sea"),                 # over the pretty blue sea : î i i î i i ôoo : (5 6 7)_ 1 3 5 2
    repeat(429.46, "sailing"),             # i'd like to know where they're going : î i i î i i ôo ôo : (5 6 7)_ 1 3 5 2   1
    phrase(436.37, "tell", [], 444.01)     # but they will never tell me : î i i î i i ôoo : 5 3 1   2 3 2 1
  ])
])

piano_lf(21, "steamboat-round-the-bend", 2, 60, "40", [
  section("V", "steamboat", [
    phrase(446.32, "mississippi"),         # on the mississippi steamboat round the bend : îi ii a a îi ii oo : 12 34 5 8 12 34 5
    phrase(454.96, "chug", [], 463.17)     # chug chug chug chug, to the journey's end : â  a  a a îi ii oo : 5(4) 5(4) 5(4) 5(4) 54 32 1
  ])
])

piano_lf(22, "comin-round-the-mountain", 4, 60, "45", [
  section("V", "mountain", [
    phrase(467.27, "1"),                   # : ii îi ii ii ii ôo : (56)_ 11 11 (65 35)_ 1
    phrase(476.93, "2"),                   # : ii îi ii ii ii ôo : 12 33 33  53 21   2
    phrase(486.47, "3"),                   # : ii îi ii ii ii îi ii ii : 54 33 33  21 11  (66 66)_21
    phrase(495.75, "4", [], 505.75)        # : ii îi ii ii ii ôooo : 16_ (55 56)_ 32 (56)_ 1
  ])
])

piano_lf(23, "the-long-trail", 3, 60, "40", [
  section("V", "rockies", [
    phrase(507.72, "hiking"),              # hiking the trails of the rockies
    phrase(514.56, "fun"),                 # lots of fun
    phrase(521.36, "climbing"),            # climbing uphill very slowly
    phrase(527.94, "down", [], 534.48)     # come down on the run
  ])
])

piano_lf(24, "the-bee", 2, 60, "40", [
  section("V", "grass", [
    phrase(538.93, "buzzing"),             # buzzing buzzing, buzzing buzzing, bee in the grass
    phrase(546.03, "pass", [], 553.30)     # please to be polite enough to let me pass
  ])
])

piano_lf(25, "my-bonnie", 4, 60, "40", [
  section("V", "island", [
    phrase(555.13, "bonnie"),              # my bonnie is over the ocean
    phrase(561.98, "sea"),                 # my bonnie is over the sea
    repeat(568.65, "bonnie"),              # my bonnie is over the ocean
    phrase(575.40, "me", [], 582.24)       # o bring back my bonnie to me
  ])
])

piano_lf(26, "vacation-time", 3, 60, "40", [
  section("V", "kooralbyn", [
    phrase(583.74, "waltzing"),            # i'm waltzing around in a merry mood
    phrase(590.37, "fun"),                 # i'm having a great deal of fun
    phrase(596.99, "cloud"),               # there's never a cloud in the sky today
    phrase(601.91, "vacation", [], 610.42) # vacation has begun
  ])
])

piano_lf(27, "home-on-the-range", 3, 60, "45", [
  section("V", "range", [
    phrase(614.52, "give"),                # oh give me a home where the buffalo roam
    phrase(620.55, "where-deer"),          # where deer and antelope play
    phrase(626.45, "seldom"),              # where seldom is heard a discouraging word
    phrase(632.44, "skies", [])            # and skies are not cloudy all day
  ]),
  section("V", "home", [
    phrase(638.72, "home"),                # home, home on the range
    phrase(644.20, "the-deer"),            # the deer and the antelope play
    repeat(650.44, "seldom"),              # where seldom is heard a discouraging word
    repeat(656.64, "skies", 661.85)        # and skies are not cloudy all day
  ])
])

piano_lf(28, "the-juggler", 4, 60, "40", [
  section("V", "circus", [
    phrase(664.97, "juggler"),             # juggler, juggler, what's your name?
    phrase(670.92, "posters"),             # all the circus posters advertise your fame
    phrase(676.65, "cup"),                 # if i tried to toss a cup
    phrase(682.20, "pieces", [], 688.32)   # i would only have to pick the pieces up
  ])
])

piano_lf(1029, "from-a-wigwam", 4, 60, "40", [
  section("V", "wigwam", [
    phrase(690.50, "1"),
    phrase(698.20, "2"),
    phrase(705.93, "3"),
    repeat(713.97, "1", 721.63)
  ])
])

