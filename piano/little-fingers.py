# vim: foldmethod=marker foldmarker=phrase,)) foldtext=getline(v\:foldstart)

import sys; sys.path.append("..")
from piano import *

process_all([

Piece("birthday-party", 2, 90, "40", "01.birthday-party.mp3", [
  Section("party", "V", [
    phrase("row", 0.66, 5.22),
    phrase("party", 5.22, 9.72)
  ])
]),

Piece("sandmans-near", 2, 90, "40", "02.sandmans-near.mp3", [
  Section("bedroom", "V", [
    phrase("dolly", 2.52, 6.97),
    phrase("sleeping", 6.97, 11.52)
  ])
]),

Piece("baseball-days", 2, 90, "40", "03.baseball-days.mp3", [
  Section("stadium", "V", [
    phrase("boys", 3.37, 7.61),
    phrase("days", 7.61, 11.96)
  ])
]),

Piece("the postman", 3, 90, "40", "04.the-postman.mp3", [
  Section("post-office", "V", [
    phrase("postman", 1.45, 6.37),
    phrase("letters", 6.37, 10.97)
  ])
]),

Piece("rain-on-the-roof", 4, 90, "40", "05.rain-on-the-roof.mp3", [
  Section("roof", "V", [
    phrase("pitter", 1.77, 6.44),
    phrase("calling", 6.44, 11.30)
  ])
]),

Piece("song-of-the-volga-boatmen", 4, 90, "40", "06.song-of-the-volga-boatmen.mp3", [
  Section("river", "V", [
    phrase("yo-ho", 2.10, 8.70),
    phrase("pull", 8.70, 16.09)
  ])
]),

Piece("a-message", 4, 90, "40", "07.a-message.mp3", [
  Section("door", "V", [
    phrase("knocking", 1.56, 4.61),
    phrase("letter", 4.61, 7.59),
    phrase("ring", 7.59, 10.61),
    phrase("bell", 10.61, 13.84)
  ])
]),

Piece("chimes", 3, 90, "40", "08.chimes.mp3", [
  Section("clock-tower", "V", [
    phrase("ding", 1.43, 3.91),
    phrase("ring", 3.91, 6.32),
    phrase("towr", 6.32, 8.73),
    phrase("hour", 8.73, 11.17),
    phrase("dong", 11.17, 16.78)
  ])
]),

Piece("good-king-wencelas", 2, 90, "40", "09.good-king-wencelas.mp3", [
  Section("castle", "V", [
    phrase("king", 2.96, 6.15),
    phrase("feast", 6.15, 9.22),
    phrase("snow", 9.22, 12.34),
    phrase("crisp", 12.34, 15.61)
  ])
]),

Piece("lazy-mary", 3, 90, "40", "10.lazy-mary.mp3", [
  Section("marys-room", "V", [
    phrase("lazy", 1.42, 5.76),
    phrase("will", 5.76, 10.83),
    repeat("lazy", 10.83, 15.03),
    phrase("late", 15.03, 20.25)
  ])
]),

Piece("betty-and-bill", 3, 90, "40", "11.betty-and-bill.mp3", [
  Section("hill", "V", [
    phrase("galloping", 1.55, 5.74),
    phrase("frolic", 5.74, 10.05)
  ])
]),

Piece("flying-to-the-moon", 2, 90, "40", "12.flying-to-the-moon.mp3", [
  Section("moon", "V", [
    phrase("flying", 2.02, 5.98),
    phrase("moon", 5.98, 9.55)
  ])
]),

Piece("air", 2, 90, "40", "13.air.mp3", [
  Section("clouds", "V", [
    phrase("haydn", 1.44, 3.77),
    phrase("lingers", 3.77, 6.00),
    phrase("bliss", 6.00, 8.16),
    phrase("tunes", 8.16, 10.64)
  ])
]),

Piece("by-the-pond", 2, 90, "40", "14.by-the-pond.mp3", [
  Section("pond", "V", [
    phrase("quack", 3.45, 7.54),
    phrase("croak", 7.54, 11.28)
  ])
]),

Piece("paper-ships", 4, 90, "40", "15.paper-ships.mp3", [
  Section("wharf", "V", [
    phrase("ships", 2.63, 7.45),
    phrase("captain", 7.45, 12.41)
  ])
]),

Piece("sledding", 3, 90, "40", "16.sledding.mp3", [
  Section("snow", "V", [
    phrase("snowflakes", 2.8, 8.06),
    phrase("sledding", 8.06, 13.37)
  ])
]),

Piece("the-butterfly", 4, 90, "40", "17.the-butterfly.mp3", [
  Section("garden", "V", [
    phrase("butterfly", 1.07, 10.32),
    phrase("flying", 10.32, 19.13)
  ])
]),

Piece("questions", 2, 90, "40", "18.questions.mp3", [
  Section("circus", "V", [
    phrase("tall", 2.01, 5.66),
    phrase("small", 5.66, 9.49)
  ])
]),

Piece("toy-soldiers", 4, 90, "40", "19.toy-soldiers.mp3", [
  Section("playroom", "V", [
    phrase("soldiers", 2.05, 6.83),
    phrase("battle", 6.83, 11.66),
    phrase("rank", 11.66, 16.46),
    phrase("onward", 16.46, 21.67)
  ])
]),

Piece("big-ships", 3, 90, "40", "20.big-ships.mp3", [
  Section("sea", "V", [
    phrase("sailing", 1.27, 4.82),
    phrase("sea", 4.82, 8.43),
    phrase("going", 8.43, 11.89),
    phrase("tell", 11.89, 15.73)
  ])
]),

Piece("steamboat-round-the-bend", 2, 90, "40", "21.steamboat-round-the-bend.mp3", [
  Section("steamboat", "V", [
    phrase("mississippi", 4.00, 8.80),
    phrase("chug", 8.80, 13.14)
  ])
]),

Piece("comin-round-the-mountain", 4, 90, "45", "22.comin-round-the-mountain.mp3", [
  Section("mountain", "V", [
    phrase("1", 1.53, 5.74),
    phrase("2", 5.74, 9.99),
    phrase("3", 9.99, 14.10),
    phrase("4", 14.10, 18.44)
  ])
]),

Piece("the-long-trail", 3, 90, "40", "23.the-long-trail.mp3", [
  Section("rockies", "V", [
    phrase("hiking", 3.78, 8.55),
    phrase("fun", 8.55, 13.45),
    phrase("climbing", 13.45, 18.20),
    phrase("down", 18.20, 22.62)
  ])
]),

Piece("the-bee", 2, 90, "40", "24.the-bee.mp3", [
  Section("grass", "V", [
    phrase("buzzing", 2.53, 5.83),
    phrase("pass", 5.83, 9.34)
  ])
]),

Piece("my-bonnie", 4, 90, "40", "25.my-bonnie.mp3", [
  Section("island", "V", [
    phrase("bonnie", 1.70, 5.92),
    phrase("sea", 5.92, 10.07),
    repeat("bonnie", 10.07, 14.21),
    phrase("me", 14.21, 17.64)
  ])
]),

Piece("vacation-time", 3, 90, "40", "26.vacation-time.mp3", [
  Section("kooralbyn", "V", [
    phrase("waltzing", 3.02, 6.73),
    phrase("fun", 6.73, 10.47),
    phrase("cloud", 10.47, 14.09),
    phrase("vacation", 14.09, 18.29)
  ])
]),

Piece("home-on-the-range", 3, 90, "45", "27.home-on-the-range.mp3", [
  Section("range", "V", [
    phrase("give", 1.20, 5.63),
    phrase("where-deer", 5.63, 10.10),
    phrase("seldom", 10.10, 14.41),
    phrase("skies", 14.41, 19.20)
  ]),
  Section("home", "V", [
    phrase("home", 19.20, 23.35),
    phrase("the-deer", 23.35, 27.65),
    repeat("seldom", 27.65, 31.87),
    repeat("skies", 31.87, 36.51)
  ])
]),

Piece("the-juggler", 4, 90, "40", "28.the-juggler.mp3", [
  Section("circus", "V", [
    phrase("juggler", 0.55, 4.13),
    phrase("posters", 4.13, 7.77),
    phrase("cup", 7.77, 11.38),
    phrase("pieces", 11.38, 15.10)
  ])
]),

Piece("from-a-wigwam", 4, 90, "40", "29.from-a-wigwam.mp3", [
  Section("wigwam", "V", [
    phrase("1", 0.69, 4.65),
    phrase("2", 4.65, 8.48),
    phrase("3", 8.48, 12.49),
    repeat("1", 12.49, 17.10)
  ])
]),

])
