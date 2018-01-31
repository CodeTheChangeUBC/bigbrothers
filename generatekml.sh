#!/bin/bash

function cleanup {
    rm -rf /srv/bigbrothers/bins.csv
    kill -9 "$XVFB_PID"
}

trap cleanup EXIT

xvfb :10 -ac &
XVFB_PID="$!"

export DISPLAY=:10
cd /srv/bigbrothers
source .env/bin/activate
./scraper.py

