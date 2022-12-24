#!/usr/bin/env bash
#
# creates a drill hierarchy, where each level of the hierarchy
# can be rotated by incrementing the leading zeros
#

source rotations-base.sh

# shorthand
es=string=1,2,3,4,5,6
picking=picking=finger,flat,alternate,economic
base-chord=chord=A,Am,B,C,D,Dm,E,E,F,Fm,G

# build the drill hierarchy
mkdir guitar; cd guitar
drill 0001.bridge-hand/0001.strumming rhythms=auio,auo,uo
drill 0001.bridge-hand/0002.palm-muting direction=up,down
drill 0001.bridge-hand/0003.string-walking strings=1,2,3,4,5,6 $picking
drill 0001.bridge-hand/0004.string-skipping strings=1,2,3,4 string=random $picking
drill 0002.fret-hand/0001.flexibility/0001.finger-stretches
drill 0002.fret-hand/0002.chord-shapes/0001.shapes
