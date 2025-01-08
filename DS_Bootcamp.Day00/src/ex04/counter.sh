#!/bin/sh

INPUT="../ex03/hh_positions.csv"
OUTPUT="hh_uniq_positions.csv"

echo "\"name\",\"count\"" > $OUTPUT

tail -n +2 $INPUT | cut -d ',' -f3 | sort | uniq -c \
| sort -nr | awk '{print $2 "," $1 }' >> $OUTPUT