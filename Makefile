.PHONY: run/dev black isort db/upgrade test test/db

run/dev:
	poetry run uvicorn main:app --reload

black:
	poetry run black .

isort:
	poetry run isort .

format: black isort


db/upgrade:
	alembic upgrade head

test/db:
	docker-compose up -d --no-recreate db

test: test/db
	poetry run pytest -v tests