venv:
	poetry shell

install:
	poetry install

env:
	cp .env.sample .env

requirements:
	poetry export -f requirements.txt --output requirements.txt

notes:
	jupyter-notebook