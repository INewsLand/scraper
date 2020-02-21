#!/bin/sh

while ! nc -z localhost 6800; do
  sleep 3
  scrapyd &
  echo "Waiting to Scrapyd"
done
echo "Deploying Project"
scrapyd-deploy news
python main.py
