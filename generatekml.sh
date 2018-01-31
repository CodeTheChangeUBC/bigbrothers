#!/bin/bash

if [[ -n "$1" ]]; then
    DIR="$1"
else
    DIR='/srv/bigbrothers'
fi

function cleanup {
    rm -rf $DIR/bins.csv
    kill -9 "$XVFB_PID"
}

trap cleanup EXIT

Xvfb :10 -ac &
XVFB_PID="$!"

export DISPLAY=:10
cd $DIR
source .env/bin/activate
./scraper.py

