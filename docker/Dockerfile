FROM inewsland/python:3-alpine

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh

RUN apk add build-base

RUN apk add --no-cache git make musl-dev go

ENV GOROOT /usr/lib/go
ENV GOPATH /go
ENV PATH /go/bin:$PATH

RUN mkdir -p ${GOPATH}/src ${GOPATH}/bin

RUN go get github.com/cespare/reflex
