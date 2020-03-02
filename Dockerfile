FROM inewsland/python:3-alpine

RUN pip install scrapy
RUN pip install scrapyd
RUN pip install git+https://github.com/scrapy/scrapyd-client.git

COPY app /app
WORKDIR /app

RUN pip install -r requirements.txt

COPY script /script

CMD [ "/script/start.sh" ]
