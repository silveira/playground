#!/bin/sh

# convert the video frames to jpeg
mplayer $1 -nosound -vo jpeg

for i in *.jpg
do
	echo $i
done



