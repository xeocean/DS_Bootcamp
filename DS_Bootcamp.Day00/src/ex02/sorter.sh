#!/bin/sh

INPUT="../ex01/hh.csv"
OUTPUT="hh_sorted.csv"

head -n 1 $INPUT > $OUTPUT

if tail -n 20 $INPUT | sort -t',' -k2 -k1 >> $OUTPUT; then
  echo "Save in hh_sorted.csv"
else
  echo "Error :("
  exit 1
fi