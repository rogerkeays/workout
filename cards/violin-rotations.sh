#!/usr/bin/env bash
#
# creates a drill hierarchy, where each level of the hierarchy
# can be rotated by incrementing the leading zeros
#

# create a directory for each drill and one file defining each drill variable
function drill { 
  mkdir -p $1; 
  i=0
  for var in ${@:2}; do
    i=$((i+1))
    touch $1/$i.$var
  done
}

# shorthand
EF="finger=p,r,m,i"
ES="string=1,2,3,4"
ESDS="string=1,2,3,4,12,23,34"
MFT="bowpos=middle,frog,top"
MFTZ="$MFT,travelling"
XING_VARS="$ES reptop=off,on npb=0,1,2,3 $MFTZ"
SCALE_VARS="mode=maj,nmin,mmin,hmin pat=ud,climb,ud-rand,rand,four-row tempo=30,60,90,120,240 npb=1,2,3,4,5,6,7 octaves=1,2,3 pos=1,3,5,7,9,Z"

# build the drill hierarchy
drill 01.ear/01.pitch-singing 
drill 01.ear/02.interval-singing
drill 01.ear/03.interval-recognition
drill 02.bow-arm/01.finger-flexibility/01.jellyfish
drill 02.bow-arm/01.finger-flexibility/02.finger-wiggles straight,curled
drill 02.bow-arm/01.finger-flexibility/03.fingertip-kisses
drill 02.bow-arm/01.finger-flexibility/04.finger-position-jankin
drill 02.bow-arm/01.finger-flexibility/05.finger-position-curls
drill 02.bow-arm/01.finger-flexibility/06.finger-hammers
drill 02.bow-arm/02.bow-hold/01.itsy-bitsy-spider
drill 02.bow-arm/02.bow-hold/02.windscreen-wiper
drill 02.bow-arm/02.bow-hold/03.bow-hand-resets
drill 02.bow-arm/02.bow-hold/04.horizontal-bow-raises
drill 02.bow-arm/02.bow-hold/05.vertical-bow-raises
drill 02.bow-arm/02.bow-hold/06.air-colle
drill 02.bow-arm/03.bow-placement/01.square $MFT $ESDS
drill 02.bow-arm/03.bow-placement/02.swivel-and-stop $MFT $ES
drill 02.bow-arm/03.bow-placement/03.hops $MFTZ
drill 02.bow-arm/03.bow-placement/04.circles dir=u,d $MFTZ
drill 02.bow-arm/03.bow-placement/05.pizzicato
drill 02.bow-arm/04.bow-pressure/01.bow-benders $ESDS
drill 02.bow-arm/04.bow-pressure/02.one-minute-bows $ESDS
drill 02.bow-arm/04.bow-pressure/03.even-bowing $ESDS spb=2,4,8,15
drill 02.bow-arm/04.bow-pressure/04.frog-reversed $ESDS spb=2,4,8,15
drill 02.bow-arm/04.bow-pressure/05.finger-lifting $ESDS spb=2,4,8,15
drill 02.bow-arm/04.bow-pressure/06.pinky-and-index $ESDS spb=2,4,8,15
drill 02.bow-arm/04.bow-pressure/07.air-bowing spb=4,8,15 bow=normal,reversed
drill 02.bow-arm/04.bow-pressure/08.parlando $ESDS xpb=1,2,4 first=light,heavy
drill 02.bow-arm/04.bow-pressure/09.ramp $ESDS crescendo,decrescendo
drill 02.bow-arm/05.bow-changes/01.stationary $ESDS $MFT
drill 02.bow-arm/05.bow-changes/02.detache $ESDS $MFTZ rhythms
drill 02.bow-arm/05.bow-changes/03.legato $ESDS $MFTZ rhythms
drill 02.bow-arm/05.bow-changes/04.martele $ESDS $MFTZ
drill 02.bow-arm/05.bow-changes/05.stacatto $ESDS $MFTZ
drill 02.bow-arm/05.bow-changes/06.spicatto $ESDS $MFTZ
drill 02.bow-arm/05.bow-changes/07.colle $ESDS
drill 02.bow-arm/06.bow-acceleration/01.fast-bowing $ESDS rest=1,0 bps=1,2
drill 02.bow-arm/06.bow-acceleration/02.speed-changes $ESDS xpb=1,2,3 first=slow,fast
drill 02.bow-arm/07.bow-direction/01.overbowing
drill 02.bow-arm/07.bow-direction/02.snaking xpb=1,2,3
drill 02.bow-arm/07.bow-direction/03.lane-changes lanes=121,232,123,321
drill 02.bow-arm/07.bow-direction/04.tilt-flat-tilt $ES
drill 02.bow-arm/08.string-crossings/01.single $XING_VARS num=2,3,4
drill 02.bow-arm/08.string-crossings/02.double $XING_VARS
drill 02.bow-arm/08.string-crossings/03.triple $XING_VARS
drill 02.bow-arm/08.string-crossings/04.chords $XING_VARS pat=1-23,12-3,12-23,12-24
drill 03.pitch-arm/01.violin-hold/01.no-hand-swivels
drill 03.pitch-arm/01.violin-hold/02.pinky-reaches
drill 03.pitch-arm/02.finger-dropping/01.trills fingers=01,12,23,34,13,24,14 $ES pos=1,3,5,7,9,Z
drill 03.pitch-arm/02.finger-dropping/02.half-scales shape=westside,chicken,gun,porcupine $ES
drill 03.pitch-arm/02.finger-dropping/03.fifth-hops $EF $ES
drill 03.pitch-arm/02.finger-dropping/04.double-stop-trills $ES thirds
drill 03.pitch-arm/02.finger-dropping/05.drop-and-lift-to-harmonic $EF $ES
drill 03.pitch-arm/03.intonation/01.pitch-matching after,together,before
drill 03.pitch-arm/03.intonation/02.interval-matching after,together,before
drill 03.pitch-arm/03.intonation/03.chromatic-scales together,before pos=1,3,5,7,9,Z
drill 03.pitch-arm/03.intonation/04.predictive-scales
drill 03.pitch-arm/04.vibrato/01.knocking fulcrum=wrist,arm loc=air,in-situ
drill 03.pitch-arm/04.vibrato/02.slides fulcrum=wrist,arm $ES
drill 03.pitch-arm/04.vibrato/03.on-the-body fulcrum=wrist,arm $EF
drill 03.pitch-arm/04.vibrato/04.on-the-string fulcrum=wrist,arm silent,voiced $EF $ES pos=1,3,5,7,9,Z
drill 03.pitch-arm/05.shifts/01.one-finger-scales chromatic,major,minor
drill 03.pitch-arm/05.shifts/02.shifts $EF int=1,2,3,4,5,6,7,8,9,X,Y,Z pos=1,3,5,7,9,Z
drill 04.both-arms/01.scales/00 $SCALE_VARS
drill 04.both-arms/01.scales/01 $SCALE_VARS
drill 04.both-arms/01.scales/02 $SCALE_VARS
drill 04.both-arms/01.scales/03 $SCALE_VARS
drill 04.both-arms/01.scales/04 $SCALE_VARS
drill 04.both-arms/01.scales/05 $SCALE_VARS
drill 04.both-arms/01.scales/06 $SCALE_VARS
drill 04.both-arms/01.scales/07 $SCALE_VARS
drill 04.both-arms/01.scales/08 $SCALE_VARS
drill 04.both-arms/01.scales/09 $SCALE_VARS
drill 04.both-arms/01.scales/0X $SCALE_VARS
drill 04.both-arms/01.scales/0Y $SCALE_VARS
drill 04.both-arms/02.arpeggios/00 $SCALE_VARS
drill 04.both-arms/02.arpeggios/01 $SCALE_VARS
drill 04.both-arms/02.arpeggios/02 $SCALE_VARS
drill 04.both-arms/02.arpeggios/03 $SCALE_VARS
drill 04.both-arms/02.arpeggios/04 $SCALE_VARS
drill 04.both-arms/02.arpeggios/05 $SCALE_VARS
drill 04.both-arms/02.arpeggios/06 $SCALE_VARS
drill 04.both-arms/02.arpeggios/07 $SCALE_VARS
drill 04.both-arms/02.arpeggios/08 $SCALE_VARS
drill 04.both-arms/02.arpeggios/09 $SCALE_VARS
drill 04.both-arms/02.arpeggios/0X $SCALE_VARS
drill 04.both-arms/02.arpeggios/0Y $SCALE_VARS

#chord patterns {300} {es} {3-strings/12, 3-strings/22} {ud} {fmt}
#right hand pizzicato

