#!/bin/sh

while ! nc -z localhost 6800; do
  sleep 3
  scrapyd&
done
if nc -z localhost 6800; then
    scrapyd-deploy news
fi
reflex -c /reflex.conf
