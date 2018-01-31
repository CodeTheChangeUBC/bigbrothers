#!/bin/bash

function cleanup {
    rm -rf /srv/bigbrothers/bins.csv
}

trap cleanup EXIT
cd /srv/bigbrothers
source .env/bin/activate
./scraper.py

