#!/bin/sh

scrapyd&
scrapyd-deploy news
reflex -c /reflex.conf
