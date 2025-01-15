# Makefile to manage common tasks

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	pytest -v

format:
	black .

lint:
	pylint --disable=R,C,W0611,E0401 app/

all: install lint test