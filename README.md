# SVG Viewer

A simple SVG viewer application built with Python and PyWebView.

## Features

- View SVG files in a native window
- Simple command-line interface
- Cross-platform support

## Installation

1. Make sure you have Python 3.9 or higher installed
2. Install Poetry (if you haven't already):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```
3. Clone this repository and navigate to the project directory
4. Install dependencies:
   ```bash
   poetry install
   ```

## Usage

To view an SVG file:

```bash
# Using Poetry
poetry run svg-viewer path/to/your/file.svg

# Or after installing globally
poetry install
svg-viewer img.svg
python viewer.py img.svg
```

## Development

### Setting up the development environment

1. Install development dependencies:
   ```bash
   poetry install --with dev
   ```

### Running tests

```bash
poetry run pytest
```

### Code formatting and linting

```bash
# Format code with Black
poetry run black .

# Sort imports with isort
poetry run isort .

# Check for type errors
poetry run mypy .

# Lint the code
poetry run flake8
```

## License

MIT