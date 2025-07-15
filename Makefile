.PHONY: help install install-dev test test-cov format lint type-check clean build upload docs

help:
	@echo "Available commands:"
	@echo "  make install      - Install the package"
	@echo "  make install-dev  - Install the package with development dependencies"
	@echo "  make test         - Run tests"
	@echo "  make test-cov     - Run tests with coverage"
	@echo "  make format       - Format code with black"
	@echo "  make lint         - Run linting with flake8"
	@echo "  make type-check   - Run type checking with mypy"
	@echo "  make clean        - Clean build artifacts"
	@echo "  make build        - Build distribution packages"
	@echo "  make upload       - Upload to PyPI (requires credentials)"
	@echo "  make docs         - Build documentation"

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"

test:
	pytest tests/

test-cov:
	pytest tests/ --cov=yaologit --cov-report=html --cov-report=term

format:
	black yaologit tests examples

lint:
	flake8 yaologit tests examples

type-check:
	mypy yaologit

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .mypy_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete

build: clean
	python -m build

upload: build
	python -m twine upload dist/*

docs:
	cd docs && sphinx-build -b html . _build/html