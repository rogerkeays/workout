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
drill 1.quiz
drill 2.tuning
drill 3.intonation/LL.01.retuning
drill 3.intonation/LL.02.pitch-singing 
drill 3.intonation/LL.03.pitch-matching timing=after,together,before
drill 3.intonation/LL.04.pitch-hitting
drill 3.intonation/LL.05.interval-singing
drill 3.intonation/LL.06.interval-matching timing=after,together,before
drill 3.intonation/LL.07.interval-recognition
drill 3.intonation/LL.08.interval-hitting
drill 3.intonation/LL.09.double-stop-matching

# bow hold
drill 4.bow-arm/LL.11.jellyfish
drill 4.bow-arm/LL.12.itsy-bitsy-spider
drill 4.bow-arm/LL.13.windscreen-wiper
drill 4.bow-arm/LL.14.bow-hand-resets
drill 4.bow-arm/LL.15.horizontal-bow-raises
drill 4.bow-arm/LL.16.vertical-bow-raises

# bow placement
drill 4.bow-arm/LL.21.square $MFT $ESDS
drill 4.bow-arm/LL.22.swivel-and-stop $MFT $ES
drill 4.bow-arm/LL.23.hops $MFTZ
drill 4.bow-arm/LL.24.retakes dir=u,d $MFTZ
drill 4.bow-arm/LL.25.pizzicato

# bow pressure
drill 4.bow-arm/LL.31.bow-benders $ESDS
drill 4.bow-arm/LL.32.one-minute-bows $ESDS
drill 4.bow-arm/LL.33.even-bowing $ESDS spb=2,4,8,15
drill 4.bow-arm/LL.34.frog-reversed $ESDS spb=2,4,8,15
drill 4.bow-arm/LL.35.finger-lifting $ESDS spb=2,4,8,15
drill 4.bow-arm/LL.36.pinky-and-index $ESDS spb=2,4,8,15
drill 4.bow-arm/LL.37.air-bowing spb=4,8,15 bow=normal,reversed
drill 4.bow-arm/LL.38.parlando $ESDS xpb=1,2,4 first=light,heavy
drill 4.bow-arm/LL.39.dynamics $ESDS crescendo,decrescendo,pianissimo

# bow changes
drill 4.bow-arm/LL.41.stationary $ESDS $MFT
drill 4.bow-arm/LL.42.detache $ESDS $MFTZ rhythms
drill 4.bow-arm/LL.43.legato $ESDS $MFTZ rhythms
drill 4.bow-arm/LL.44.martele $ESDS $MFTZ
drill 4.bow-arm/LL.45.stacatto $ESDS $MFTZ
drill 4.bow-arm/LL.46.brushing $ESDS $MFTZ
drill 4.bow-arm/LL.47.spicatto $ESDS $MFTZ
drill 4.bow-arm/LL.48.colle $ESDS

# bow acceleration
drill 4.bow-arm/LL.51.fast-bowing $ESDS rest=1,0 bps=1,2
drill 4.bow-arm/LL.52.speed-changes $ESDS xpb=1,2,3 first=slow,fast

# bow direction
drill 4.bow-arm/LL.61.overbowing
drill 4.bow-arm/LL.62.snaking xpb=1,2,3
drill 4.bow-arm/LL.63.lane-changes lanes=121,232,123,321
drill 4.bow-arm/LL.64.tilt-flat-tilt $ES

# string crossings
drill 4.bow-arm/LL.71.single $XING_VARS num=2,3,4
drill 4.bow-arm/LL.72.double $XING_VARS
drill 4.bow-arm/LL.73.triple $XING_VARS
drill 4.bow-arm/LL.74.chords $XING_VARS pat=1-23,12-3,12-23,12-24

# violin hold
drill 5.pitch-arm/LL.11.no-hand-swivels
drill 5.pitch-arm/LL.12.pinky-reaches

# finger independence
drill 5.pitch-arm/LL.21.finger-wiggles straight,curled
drill 5.pitch-arm/LL.22.fingertip-kisses
drill 5.pitch-arm/LL.23.finger-position-jankin
drill 5.pitch-arm/LL.24.finger-position-curls
drill 5.pitch-arm/LL.25.finger-hammers

# finger dropping
drill 5.pitch-arm/LL.31.trills fingers=01,12,23,34,13,24,14 $ES pos=1,3,5,7,9,Z
drill 5.pitch-arm/LL.32.half-scales shape=westside,chicken,gun,porcupine $ES drone=off,on
drill 5.pitch-arm/LL.33.fifth-hops $EF $ES
drill 5.pitch-arm/LL.34.double-stop-trills $ES thirds
drill 5.pitch-arm/LL.35.drop-and-lift-to-harmonic $EF $ES

# vibrato
drill 5.pitch-arm/LL.51.vibrato-knocking fulcrum=wrist,arm loc=air,in-situ silent,voiced
drill 5.pitch-arm/LL.53.on-the-body-vibrato fulcrum=wrist,arm $EF
drill 5.pitch-arm/LL.52.vibrato-slides fulcrum=wrist,arm $ES silent,voiced
drill 5.pitch-arm/LL.54.on-the-string fulcrum=wrist,arm silent,voiced $EF $ES pos=1,3,5,7,9,Z

# shifts
drill 5.pitch-arm/LL.61.one-finger-scales chromatic,major,minor
drill 5.pitch-arm/LL.62.same-finger-shifts $EF int=1,2,3,4,5,6,7,8,9,X,Y,Z pos=1,3,5,7,9,Z
drill 5.pitch-arm/LL.63.different-finger-shifts $EF int=1,2,3,4,5,6,7,8,9,X,Y,Z pos=1,3,5,7,9,Z

drill 6.both-arms/LL.01.chromatic-scale $SCALE_VARS
scale 6.both-arms/LL.02.scales LL.01.ud $MODES $SCALE_VARS
scale 6.both-arms/LL.02.scales LL.02.climbs $MODES $SCALE_VARS
scale 6.both-arms/LL.02.scales LL.03.four-in-a-row $MODES $SCALE_VARS
scale 6.both-arms/LL.02.scales LL.04.random-conj $MODES $SCALE_VARS
scale 6.both-arms/LL.02.scales LL.05.random-disj $MODES $SCALE_VARS
scale 6.both-arms/LL.03.arpeggios LL.01.ud mode=maj,min $SCALE_VARS
scale 6.both-arms/LL.03.arpeggios LL.02.climbs mode=maj,min $SCALE_VARS
scale 6.both-arms/LL.03.arpeggios LL.03.random-conj mode=maj,min $SCALE_VARS
scale 6.both-arms/LL.03.arpeggios LL.04.random-disj mode=maj,min $SCALE_VARS
drill 7.phrases
drill 8.pieces

#chord patterns {301} {es} {3-strings/12, 3-strings/22} {ud} {fmt}
#right hand pizzicato

