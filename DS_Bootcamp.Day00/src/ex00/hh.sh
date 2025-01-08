#!/bin/sh

if [ $# -eq 0 ]
then
  echo "Use: $0 <search vacancy>"
  exit 1
fi

SEARCH="$*"
ENCODE=$(echo "$SEARCH" | sed 's/ /%20/g')

if curl -s "https://api.hh.ru/vacancies?text=${ENCODE}&per_page=20" | jq . > hh.json
then
  echo "Save in hh.json"
else
  echo "Request error"
  exit 1
fi