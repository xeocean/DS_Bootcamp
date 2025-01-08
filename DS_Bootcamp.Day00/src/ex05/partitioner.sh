#!/bin/sh

INPUT="../ex03/hh_positions.csv"

HEADER=$(head -n 1 $INPUT)

tail -n +2 $INPUT | while IFS=, read -r id created_at name has_test alternate_url;
do
  DATE=$(echo "$created_at" | cut -d 'T' -f 1 | cut -d '"' -f 2)
  OUTPUT="$DATE".csv

  if [ ! -f "$OUTPUT" ]; then
    echo "$HEADER" > "$OUTPUT"
  fi

  echo "$id,$created_at,$name,$has_test,$alternate_url" >> "$OUTPUT"
done