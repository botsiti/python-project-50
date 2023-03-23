install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl

package-remove:
	python3 -m pip uninstall hexlet-code


lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml


selfcheck:
	poetry check

check: selfcheck test lint

build: check
	poetry build

.PHONY: install test lint selfcheck check build
