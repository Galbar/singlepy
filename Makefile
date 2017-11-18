all: clean flake tests

clean:
	find . -regex ".*\.pyc" -delete
	find . -name "__pycache__" -delete
	rm -rf .coverage .cache

flake:
	python -m flake8 .

tests:
	PYTHONPATH=. pytest tests/ --cov=singlepy --cov-report=term-missing

.PHONY: clean flake tests
