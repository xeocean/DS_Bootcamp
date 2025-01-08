#!/bin/sh

INPUT="../ex02/hh_sorted.csv"
OUTPUT="hh_positions.csv"

head -n 1 $INPUT > $OUTPUT
tail -n +2 $INPUT | awk -F '",' '{

  position = "-"

  if ($3 ~ /[Jj]unior/) position = "Junior"
  if ($3 ~ /[Mm]iddle/) position = (position == "-" ? "Middle" : position "/Middle")
  if ($3 ~ /[Ss]enior/) position = (position == "-" ? "Senior" : position "/Senior")

  $3 = "\"" position "\""
  print $1 "\"," $2 "\"," $3 "," $4
}' >> $OUTPUT
