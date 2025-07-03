.PHONY: help install install-dev test lint format type-check build publish clean

# Variables
PYTHON = poetry run python
PACKAGE_NAME = svg-viewer

# Help
help:
	@echo "SVG Viewer - Makefile"
	@echo "======================"
	@echo "Available targets:"
	@echo "  install      Install production dependencies"
	@echo "  install-dev  Install development dependencies"
	@echo "  test        Run tests"
	@echo "  lint        Run code linters (flake8)"
	@echo "  format      Format code (black, isort)"
	@echo "  type-check  Run type checking (mypy)"
	@echo "  check       Run all checks (lint, format, type-check, test)"
	@echo "  build       Build the package"
	@echo "  publish     Publish to PyPI"
	@echo "  clean       Clean build artifacts"

# Installation
install:
	@echo "Installing production dependencies..."
	poetry install --no-dev

install-dev:
	@echo "Installing development dependencies..."
	poetry install

# Testing
test:
	@echo "Running tests..."
	poetry run pytest -v --cov=$(PACKAGE_NAME) --cov-report=term-missing

# Linting
lint:
	@echo "Running flake8..."
	poetry run flake8 $(PACKAGE_NAME) tests

# Formatting
format:
	@echo "Running black..."
	poetry run black $(PACKAGE_NAME) tests
	@echo "Running isort..."
	poetry run isort $(PACKAGE_NAME) tests

# Type checking
type-check:
	@echo "Running mypy..."
	poetry run mypy $(PACKAGE_NAME) tests

# Run all checks
check: lint format type-check test

# Build and publish
build:
	@echo "Building package..."
	rm -rf dist/*
	poetry build

publish: build
	@echo "Publishing to PyPI..."
	poetry publish

# Cleanup
clean:
	@echo "Cleaning up..."
	rm -rf build/
	rm -rf dist/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf .coverage
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type d -name "*.egg-info" -exec rm -r {} +

# Default target
.DEFAULT_GOAL := help
