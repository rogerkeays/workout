#!/usr/bin/env bash
#
# creates a drill hierarchy, where each level of the hierarchy
# can be rotated by incrementing the leading zeros
#

source rotations-base.sh

# shorthand
es=string=1,2,3,4,5,6
picking=picking=finger,flat,alternate,economic
chords=chord=A,Am,B,C,D,Dm,E,E,F,Fm,G
bar_chords=shape=A,Am,C,D,Dm,E,Em,G
shifts=shift=1,2,3,4,5,6,7,8,9,X,Y,Z
frets=fret=0,1,2,3,4,5,6,7,8,9,X,Y,Z
tonics=tonic=0,1,2,3,4,5,6,7,8,9,X,Y
modes=mode=maj,nmin,mmin,hmin
scale_vars=tempo=30,60,90,120,240 octaves=1,2,3 pos=$frets
progressions=progression=1545,1654,6415,1514
rhythms=rhythm=a,u,i,o,au,ai,ao,ui,uo,io,aui,auo,uio,auio

# build the drill hierarchy
mkdir guitar; cd guitar
drill 0001.G4
drill 0002.bridge-hand/0001.strumming rhythms=auio,auo,uo
drill 0002.bridge-hand/0002.palm-muting direction=up,down
drill 0002.bridge-hand/0003.string-walking strings=1,2,3,4,5,6 $picking
drill 0002.bridge-hand/0004.string-skipping strings=1,2,3,4 string=random $picking
drill 0003.fret-hand/0001.flexibility/0001.finger-stretches
drill 0003.fret-hand/0002.chords/0001.chord-shapes $chords
drill 0003.fret-hand/0002.chords/0002.shifts $shifts $bar_chords
drill 0003.fret-hand/0002.chords/0003.chord-changes from=$chords to=$chords $shifts
drill 0003.fret-hand/0003.fingering/0001.half-scales $es mode=maj,min
drill 0003.fret-hand/0003.fingering/0002.trills $es interval=1,2 $frets
drill 0003.fret-hand/0003.fingering/0003.hammer-ons $es interval=1,2 $frets fingers=2,3,4
drill 0003.fret-hand/0003.fingering/0004.flick-offs $es interval=1,2 $frets fingers=2,3,4
drill 0004.hands-together/0001.scales $modes $scale_vars $picking
drill 0004.hands-together/0002.arpeggios mode=maj,min $scale_vars $picking
drill 0004.hands-together/0003.chord-progressions $tonics $modes $rhythms $progressions $scale_vars $picking
drill 0004.hands-together/0004.arpeggiated-progressions $tonics $modes $rhythms $progressions $scale_vars $picking strings=2,3,4,5,6
drill 0005.phrases
drill 0006.pieces


# bridge hand
#   strumming=thumb,thumbnail,finger,fingernail,fake-pick,thumb-then-finger
#       picking
#         finger picking
#         fingerstyle
#         finger tapping
#       6/8 strumming
#       crescendo/decrescendo strumming
#       pinch harmonics
#
# pitch hand
#       fingering
#         hammer-ons {12,23,34,13,24,14,123,234,134,124,1234} {es} (justin 20061204)
#         flick-offs {12,23,34,13,24,14,123,234,134,124,1234} {es} (justin 20061204)
#         spider diagonals with alternate picking (justin 20061204)
#
#       chords
#         one minute chordchanges
#
#       harmonics
#         classical harmonics (opposite of open harmonics)
#         tapped harmonics
#
# both hands
#       scales
#         position 1: second finger on root, no shifts
#         position 2: second finger on root, 4th string, shift up on 2nd string and 5th string
#         legato scales with three finger scales
#         cycling (only pick when changing strings)
#
#       scale variations
#         random direction changes
#         random scale degrees 
#         climbs in thirds
#         four in a row
#
#  riffs
#    peter gunn theme
