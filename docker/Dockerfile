FROM inewsland/python:3-alpine

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

RUN apk add build-base

RUN apk add --no-cache git make musl-dev go

RUN pip install scrapy
RUN pip install scrapyd
RUN pip install git+https://github.com/scrapy/scrapyd-client.git

ENV GOROOT /usr/lib/go
ENV GOPATH /go
ENV PATH /go/bin:$PATH

RUN mkdir -p ${GOPATH}/src ${GOPATH}/bin

RUN go get github.com/cespare/reflex

EXPOSE 5000
