#!/bin/sh

OUTPUT="hh_positions.csv"

echo '"id","created_at","name","has_test","alternate_url"' > $OUTPUT

for file in ./*.csv; do
  if [ "$file" = ./$OUTPUT ]; then
     continue
  fi
  tail -n +2 "$file" >> $OUTPUT
done