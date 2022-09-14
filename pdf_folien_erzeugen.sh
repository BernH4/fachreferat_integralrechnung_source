#!/bin/sh
set -e
rm -r tmp/ || echo "kein dir"
mkdir "tmp"
convert fachreferat_integralrechnung/thumb*.jpg  -channel RGB -negate tmp/negated.jpg
convert `ls -v tmp/*.jpg` folien_ausdruck_gesamt.pdf

