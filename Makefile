start:
	docker-compose -f docker/docker-compose.yml up -d
stop:
	docker-compose -f docker/docker-compose.yml down
restart:
	docker-compose -f docker/docker-compose.yml down --remove-orphans && \
	docker-compose -f docker/docker-compose.yml up --build
remove:
	docker-compose -f docker/docker-compose.yml down --rmi all
install:
	rm -rf $(PWD)/app/dependencies && \
	docker run --rm -v $(PWD)/app:/app \
	-e "PYTHONPATH=/usr/local/lib/python3.8:/app/dependencies" \
	inewsland/python:3-alpine pip install -r /app/requirements.txt -t /app/dependencies
freeze:
	pip freeze > app/requirements.txt
sync:
	pip install -r app/requirements.txt
build:
	docker build -t scrapers:latest .
scrapy:
	docker container exec -it scraper_app bash -c scrapy
crawl:
	docker container exec -it scraper_app bash -c "scrapy crawl ${spider}"
check:
	docker container exec -it scraper_app bash -c "scrapy check ${spider}"
shell:
	docker container exec -it scraper_app bash -c "scrapy shell"
genspider:
	docker container exec -it scraper_app bash -c "scrapy genspider ${spider}"
list:
	docker container exec -it scraper_app bash -c "scrapy list"
