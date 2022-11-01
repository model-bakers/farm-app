.PHONY=help
SHELL := /bin/bash

help:  ## This help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

clean: ## Remove cache files
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf

### install dependencies

dependencies: 
	pip install -r requirements.txt

### envirements
setup:
	cp .env-example.txt .env

###
# Lint section
###
_flake8:
	@flake8 --show-source

_isort:
	@isort --check-only .

_black:
	@black --diff --check .

_isort-fix:
	@isort .

_black_fix:
	@black .

detect_missing_migrations:  ## Detect missing model migration
	@python manage.py makemigrations --dry-run | grep -q "No changes detect"

lint: _flake8 _isort _black detect_missing_migrations ## Check code lint
format-code: _isort-fix _black_fix  ## Format code

test: clean ## Run tests
	@pytest

###
# Shell section
###
shell:  ## Run repl with development settings
	@python manage.py shell

###
# Run section
###
run:  ## Run server with default settings
	@python manage.py migrate --no-input
	@python manage.py runserver