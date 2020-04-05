#!/bin/bash

# Makes a 256-sprite atlas out of an emoji block.
# example: to make the atlas 1f300..1f3ff:
# make_sprite_atlas.sh 1f3

mkdir work || exit 1

seq 0x"$1"0 0x"$1"f | xargs printf '%03x\n' | while read HEX
do
  seq 0x"$HEX"0 0x"$HEX"f | xargs printf '%04x\n' | while read NUM
  do
    ./make_sprite.sh "$NUM" work/
  done
  convert work/"$HEX"*.png +append work/h"$HEX".png
done
convert work/h*.png -append "$1".png

rm -fr work


