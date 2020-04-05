#!/bin/bash

export SRC="noto-emoji/svg/emoji_u""$1".svg

if [ ! -e "$SRC" ]
then
  export SRC="box-drawing/svg/0x""$1".svg
fi

export DEST="$2""$1".png

cp fallback.png "$DEST"
convert -thumbnail 64x64 -gravity center -background none -extent 64x64 \
        -colorspace Gray -evaluate add 25% -posterize 3 -evaluate add 10% \
        "$SRC" PNG32:"$DEST"

