dev:
	docker-compose -f docker/docker-compose.yml up
rebuild:
	docker-compose -f docker/docker-compose.yml down --rmi all && \
	docker-compose -f docker/docker-compose.yml up
remove:
	docker-compose -f docker/docker-compose.yml down --rmi all
install:
	rm -rf $(PWD)/app/dependencies && \
	docker run --rm -v $(PWD)/app:/app \
	-e "PYTHONPATH=/usr/local/lib/python3.8:/app/dependencies" \
	inewsland/python:3-alpine pip install -r /app/requirements.txt -t /app/dependencies
freeze:
	pip freeze > app/requirements.txt
