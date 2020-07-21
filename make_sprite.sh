#!/bin/bash

export DEST="$2""$1".png
cp fallback.png "$DEST"

export SRC="noto-emoji/svg/emoji_u""$1".svg

if [ ! -e "$SRC" ]
then
  export SRC="box-drawing/svg/0x""$1".svg
fi

if [ -e "$SRC" ]
then
  convert -thumbnail 64x64 -gravity center -background none -extent 64x64 \
         -posterize 4 \
        "$SRC" PNG32:"$DEST"
  #        -colorspace Gray -evaluate add 25%

fi
