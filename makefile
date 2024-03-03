venv:
	poetry shell

install:
	poetry install

requirements:
	poetry export -f requirements.txt --output requirements.txt