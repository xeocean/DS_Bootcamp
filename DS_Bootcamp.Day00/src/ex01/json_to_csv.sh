#!/bin/sh

INPUT="../ex00/hh.json"
OUTPUT="hh.csv"
FILTER="filter.jq"

echo "\"id\",\"created_at\",\"name\",\"has_test\",\"alternate_url\"" > $OUTPUT

if jq -r -f $FILTER $INPUT >> $OUTPUT; then
  echo "Save in hh.csv"
else
  echo "Error :("
  exit 1
fi