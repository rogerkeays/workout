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
drill 0001.A4
drill 0002.ear/0000.frogs
drill 0002.ear/0001.pitch-singing 
drill 0002.ear/0002.pitch-matching timing=after,together,before
drill 0002.ear/0003.interval-singing
drill 0002.ear/0004.interval-matching timing=after,together,before
drill 0002.ear/0005.interval-recognition
drill 0002.ear/0006.double-stop-matching
drill 0002.ear/0007.retuning
drill 0003.bow-arm/0000.frogs
drill 0003.bow-arm/0001.bow-hold/0001.jellyfish
drill 0003.bow-arm/0001.bow-hold/0002.itsy-bitsy-spider
drill 0003.bow-arm/0001.bow-hold/0003.windscreen-wiper
drill 0003.bow-arm/0001.bow-hold/0004.bow-hand-resets
drill 0003.bow-arm/0001.bow-hold/0005.horizontal-bow-raises
drill 0003.bow-arm/0001.bow-hold/0006.vertical-bow-raises
drill 0003.bow-arm/0002.bow-placement/0001.square $MFT $ESDS
drill 0003.bow-arm/0002.bow-placement/0002.swivel-and-stop $MFT $ES
drill 0003.bow-arm/0002.bow-placement/0003.hops $MFTZ
drill 0003.bow-arm/0002.bow-placement/0004.circles dir=u,d $MFTZ
drill 0003.bow-arm/0002.bow-placement/0005.pizzicato
drill 0003.bow-arm/0003.bow-pressure/0001.bow-benders $ESDS
drill 0003.bow-arm/0003.bow-pressure/0002.one-minute-bows $ESDS
drill 0003.bow-arm/0003.bow-pressure/0003.even-bowing $ESDS spb=2,4,8,15
drill 0003.bow-arm/0003.bow-pressure/0004.frog-reversed $ESDS spb=2,4,8,15
drill 0003.bow-arm/0003.bow-pressure/0005.finger-lifting $ESDS spb=2,4,8,15
drill 0003.bow-arm/0003.bow-pressure/0006.pinky-and-index $ESDS spb=2,4,8,15
drill 0003.bow-arm/0003.bow-pressure/0007.air-bowing spb=4,8,15 bow=normal,reversed
drill 0003.bow-arm/0003.bow-pressure/0008.parlando $ESDS xpb=1,2,4 first=light,heavy
drill 0003.bow-arm/0003.bow-pressure/0009.dynamics $ESDS crescendo,decrescendo,pianissimo
drill 0003.bow-arm/0004.bow-changes/0001.stationary $ESDS $MFT
drill 0003.bow-arm/0004.bow-changes/0002.detache $ESDS $MFTZ rhythms
drill 0003.bow-arm/0004.bow-changes/0003.legato $ESDS $MFTZ rhythms
drill 0003.bow-arm/0004.bow-changes/0004.martele $ESDS $MFTZ
drill 0003.bow-arm/0004.bow-changes/0005.stacatto $ESDS $MFTZ
drill 0003.bow-arm/0004.bow-changes/0006.spicatto $ESDS $MFTZ
drill 0003.bow-arm/0004.bow-changes/0007.colle $ESDS
drill 0003.bow-arm/0005.bow-acceleration/0001.fast-bowing $ESDS rest=1,0 bps=1,2
drill 0003.bow-arm/0005.bow-acceleration/0002.speed-changes $ESDS xpb=1,2,3 first=slow,fast
drill 0003.bow-arm/0006.bow-direction/0001.overbowing
drill 0003.bow-arm/0006.bow-direction/0002.snaking xpb=1,2,3
drill 0003.bow-arm/0006.bow-direction/0003.lane-changes lanes=121,232,123,321
drill 0003.bow-arm/0006.bow-direction/0004.tilt-flat-tilt $ES
drill 0003.bow-arm/0007.string-crossings/0001.single $XING_VARS num=2,3,4
drill 0003.bow-arm/0007.string-crossings/0002.double $XING_VARS
drill 0003.bow-arm/0007.string-crossings/0003.triple $XING_VARS
drill 0003.bow-arm/0007.string-crossings/0004.chords $XING_VARS pat=1-23,12-3,12-23,12-24
drill 0004.pitch-arm/0000.frogs
drill 0004.pitch-arm/0001.violin-hold/0001.no-hand-swivels
drill 0004.pitch-arm/0001.violin-hold/0002.pinky-reaches
drill 0004.pitch-arm/0002.finger-independence/0001.finger-wiggles straight,curled
drill 0004.pitch-arm/0002.finger-independence/0002.fingertip-kisses
drill 0004.pitch-arm/0002.finger-independence/0003.finger-position-jankin
drill 0004.pitch-arm/0002.finger-independence/0004.finger-position-curls
drill 0004.pitch-arm/0002.finger-independence/0005.finger-hammers
drill 0004.pitch-arm/0003.finger-dropping/0001.trills fingers=01,12,23,34,13,24,14 $ES pos=1,3,5,7,9,Z
drill 0004.pitch-arm/0003.finger-dropping/0002.half-scales shape=westside,chicken,gun,porcupine $ES
drill 0004.pitch-arm/0003.finger-dropping/0003.fifth-hops $EF $ES
drill 0004.pitch-arm/0003.finger-dropping/0004.double-stop-trills $ES thirds
drill 0004.pitch-arm/0003.finger-dropping/0005.drop-and-lift-to-harmonic $EF $ES
drill 0004.pitch-arm/0005.vibrato/0001.knocking fulcrum=wrist,arm loc=air,in-situ
drill 0004.pitch-arm/0005.vibrato/0002.slides fulcrum=wrist,arm $ES
drill 0004.pitch-arm/0005.vibrato/0003.on-the-body fulcrum=wrist,arm $EF
drill 0004.pitch-arm/0005.vibrato/0004.on-the-string fulcrum=wrist,arm silent,voiced $EF $ES pos=1,3,5,7,9,Z
drill 0004.pitch-arm/0006.shifts/0001.one-finger-scales chromatic,major,minor
drill 0004.pitch-arm/0006.shifts/0002.same-finger-shifts $EF int=1,2,3,4,5,6,7,8,9,X,Y,Z pos=1,3,5,7,9,Z
drill 0004.pitch-arm/0006.shifts/0003.different-finger-shifts $EF int=1,2,3,4,5,6,7,8,9,X,Y,Z pos=1,3,5,7,9,Z
drill 0005.both-arms/0000.frogs
drill 0005.both-arms/0001.chromatic-scale $SCALE_VARS
scale 0005.both-arms/0002.scales 0001.ud $MODES $SCALE_VARS
scale 0005.both-arms/0002.scales 0002.climbs $MODES $SCALE_VARS
scale 0005.both-arms/0002.scales 0003.four-in-a-row $MODES $SCALE_VARS
scale 0005.both-arms/0002.scales 0004.random-conj $MODES $SCALE_VARS
scale 0005.both-arms/0002.scales 0005.random-disj $MODES $SCALE_VARS
scale 0005.both-arms/0003.arpeggios 0001.ud mode=maj,min $SCALE_VARS
scale 0005.both-arms/0003.arpeggios 0002.climbs mode=maj,min $SCALE_VARS
scale 0005.both-arms/0003.arpeggios 0003.random-conj mode=maj,min $SCALE_VARS
scale 0005.both-arms/0003.arpeggios 0004.random-disj mode=maj,min $SCALE_VARS
drill 0006.phrases
drill 0007.pieces

#chord patterns {301} {es} {3-strings/12, 3-strings/22} {ud} {fmt}
#right hand pizzicato

