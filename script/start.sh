#!/bin/sh

set -e
set -x

curl http://159.89.224.233:6800/delproject.json -d project=news
scrapyd-deploy news
