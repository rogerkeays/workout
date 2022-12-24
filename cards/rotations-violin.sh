#!/usr/bin/env bash
#
# creates a drill hierarchy, where each level of the hierarchy
# can be rotated by incrementing the leading zeros
#

source rotations-base.sh

# shorthand
EF="finger=p,r,m,i"
ES="string=1,2,3,4"
ESDS="string=1,2,3,4,12,23,34"
MFT="bowpos=middle,frog,top"
MFTZ="$MFT,travelling"
XING_VARS="$ES reptop=off,on npb=0,1,2,3 $MFTZ" # shoulder/elbow/wrist
MODES="mode=maj,nmin,mmin,hmin"
SCALE_VARS="timing=together,predictive tempo=30,60,90,120,240 npb=1,2,3,4,5,6,7 octaves=1,2,3 pos=1,3,5,7,9,Z"

# build the drill hierarchy
mkdir violin; cd violin
drill 001.ear/001.pitch-singing 
drill 001.ear/002.pitch-matching timing=after,together,before
drill 001.ear/003.interval-singing
drill 001.ear/004.interval-matching timing=after,together,before
drill 001.ear/005.interval-recognition
drill 001.ear/006.double-stop-matching
drill 001.ear/007.retuning
drill 002.frogs/001.fingertip-kisses
drill 002.frogs/002.pinky-reaches
drill 002.frogs/003.pinky-vibrato $ES
drill 003.bow-arm/002.bow-hold/001.jellyfish
drill 003.bow-arm/002.bow-hold/002.itsy-bitsy-spider
drill 003.bow-arm/002.bow-hold/003.windscreen-wiper
drill 003.bow-arm/002.bow-hold/004.bow-hand-resets
drill 003.bow-arm/002.bow-hold/005.horizontal-bow-raises
drill 003.bow-arm/002.bow-hold/006.vertical-bow-raises
drill 003.bow-arm/003.bow-placement/001.square $MFT $ESDS
drill 003.bow-arm/003.bow-placement/002.swivel-and-stop $MFT $ES
drill 003.bow-arm/003.bow-placement/003.hops $MFTZ
drill 003.bow-arm/003.bow-placement/004.circles dir=u,d $MFTZ
drill 003.bow-arm/003.bow-placement/005.pizzicato
drill 003.bow-arm/004.bow-pressure/001.bow-benders $ESDS
drill 003.bow-arm/004.bow-pressure/002.one-minute-bows $ESDS
drill 003.bow-arm/004.bow-pressure/003.even-bowing $ESDS spb=2,4,8,15
drill 003.bow-arm/004.bow-pressure/004.frog-reversed $ESDS spb=2,4,8,15
drill 003.bow-arm/004.bow-pressure/005.finger-lifting $ESDS spb=2,4,8,15
drill 003.bow-arm/004.bow-pressure/006.pinky-and-index $ESDS spb=2,4,8,15
drill 003.bow-arm/004.bow-pressure/007.air-bowing spb=4,8,15 bow=normal,reversed
drill 003.bow-arm/004.bow-pressure/008.parlando $ESDS xpb=1,2,4 first=light,heavy
drill 003.bow-arm/004.bow-pressure/009.dynamics $ESDS crescendo,decrescendo,pianissimo
drill 003.bow-arm/005.bow-changes/001.stationary $ESDS $MFT
drill 003.bow-arm/005.bow-changes/002.detache $ESDS $MFTZ rhythms
drill 003.bow-arm/005.bow-changes/003.legato $ESDS $MFTZ rhythms
drill 003.bow-arm/005.bow-changes/004.martele $ESDS $MFTZ
drill 003.bow-arm/005.bow-changes/005.stacatto $ESDS $MFTZ
drill 003.bow-arm/005.bow-changes/006.spicatto $ESDS $MFTZ
drill 003.bow-arm/005.bow-changes/007.colle $ESDS
drill 003.bow-arm/006.bow-acceleration/001.fast-bowing $ESDS rest=1,00 bps=1,2
drill 003.bow-arm/006.bow-acceleration/002.speed-changes $ESDS xpb=1,2,3 first=slow,fast
drill 003.bow-arm/007.bow-direction/001.overbowing
drill 003.bow-arm/007.bow-direction/002.snaking xpb=1,2,3
drill 003.bow-arm/007.bow-direction/003.lane-changes lanes=121,232,123,321
drill 003.bow-arm/007.bow-direction/004.tilt-flat-tilt $ES
drill 003.bow-arm/008.string-crossings/001.single $XING_VARS num=2,3,4
drill 003.bow-arm/008.string-crossings/002.double $XING_VARS
drill 003.bow-arm/008.string-crossings/003.triple $XING_VARS
drill 003.bow-arm/008.string-crossings/004.chords $XING_VARS pat=1-23,12-3,12-23,12-24
drill 004.pitch-arm/001.violin-hold/001.no-hand-swivels
drill 004.pitch-arm/001.violin-hold/002.pinky-reaches
drill 004.pitch-arm/002.finger-independence/001.finger-wiggles straight,curled
drill 004.pitch-arm/002.finger-independence/002.fingertip-kisses
drill 004.pitch-arm/002.finger-independence/003.finger-position-jankin
drill 004.pitch-arm/002.finger-independence/004.finger-position-curls
drill 004.pitch-arm/002.finger-independence/005.finger-hammers
drill 004.pitch-arm/003.finger-dropping/001.trills fingers=001,12,23,34,13,24,14 $ES pos=1,3,5,7,9,Z
drill 004.pitch-arm/003.finger-dropping/002.half-scales shape=westside,chicken,gun,porcupine $ES
drill 004.pitch-arm/003.finger-dropping/003.fifth-hops $EF $ES
drill 004.pitch-arm/003.finger-dropping/004.double-stop-trills $ES thirds
drill 004.pitch-arm/003.finger-dropping/005.drop-and-lift-to-harmonic $EF $ES
drill 004.pitch-arm/005.vibrato/001.knocking fulcrum=wrist,arm loc=air,in-situ
drill 004.pitch-arm/005.vibrato/002.slides fulcrum=wrist,arm $ES
drill 004.pitch-arm/005.vibrato/003.on-the-body fulcrum=wrist,arm $EF
drill 004.pitch-arm/005.vibrato/004.on-the-string fulcrum=wrist,arm silent,voiced $EF $ES pos=1,3,5,7,9,Z
drill 004.pitch-arm/006.shifts/001.one-finger-scales chromatic,major,minor
drill 004.pitch-arm/006.shifts/002.same-finger-shifts $EF int=1,2,3,4,5,6,7,8,9,X,Y,Z pos=1,3,5,7,9,Z
drill 004.pitch-arm/006.shifts/003.different-finger-shifts $EF int=1,2,3,4,5,6,7,8,9,X,Y,Z pos=1,3,5,7,9,Z
drill 005.both-arms/001.chromatic-scale $SCALE_VARS
scale 005.both-arms/002.scales 001.ud $MODES
scale 005.both-arms/002.scales 002.climbs $MODES
scale 005.both-arms/002.scales 003.four-in-a-row $MODES
scale 005.both-arms/002.scales 004.random-conj $MODES
scale 005.both-arms/002.scales 005.random-disj $MODES
scale 005.both-arms/003.arpeggios 001.ud mode=maj,min
scale 005.both-arms/003.arpeggios 002.climbs mode=maj,min
scale 005.both-arms/003.arpeggios 003.random-conj mode=maj,min
scale 005.both-arms/003.arpeggios 004.random-disj mode=maj,min

#chord patterns {300} {es} {3-strings/12, 3-strings/22} {ud} {fmt}
#right hand pizzicato

