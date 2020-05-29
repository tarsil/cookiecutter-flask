requirements:
	pip install -r requirements-dev.txt

docker:
	docker-compose up

docker-no-logs:
	docker-compose up -d

docker-stop:
	docker-compose stop

run-local:
	python -m src.serve

run-special:
	FLASK_SETTINGS_FILENAME=$(FLASK_SETTINGS_FILENAME) python -m src.serve

run-tests:
	python -m src.tests