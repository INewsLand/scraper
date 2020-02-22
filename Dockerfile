FROM inewsland/python:3-alpine

EXPOSE 5000

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

RUN apk add build-base

RUN pip install scrapy
RUN pip install scrapyd
RUN pip install git+https://github.com/scrapy/scrapyd-client.git

COPY app /app
WORKDIR /app

RUN pip install -r requirements.txt

RUN scrapyd-deploy news
