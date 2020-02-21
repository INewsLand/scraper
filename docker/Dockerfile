FROM inewsland/python:3-alpine

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

RUN apk add build-base

RUN pip install scrapy

EXPOSE 5000
