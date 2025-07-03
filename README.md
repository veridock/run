# SVG Viewer with Python Integration

A powerful SVG viewer application built with Python and PyWebView that supports embedded Python execution within SVG files.

## Features

- View SVG files in a native window
- Execute embedded Python code within SVG files
- Interactive SVG elements with Python backend
- Simple command-line interface
- Cross-platform support (Linux, Windows, macOS)
- Support for both GTK and Qt backends
- Example interactive SVG included (`preview.svg`)

## Installation

### Prerequisites

- Python 3.9 or higher
- System dependencies (GTK or Qt)

### Automated Setup (Recommended)

1. Clone this repository and navigate to the project directory
2. Run the setup script (requires sudo for system packages):
   ```bash
   chmod +x setup_env.sh
   sudo ./setup_env.sh
   ```
3. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

### Manual Setup

1. Install system dependencies:

   **For Fedora:**
   ```bash
   sudo dnf install python3-gobject gtk3 webkit2gtk3 python3-qt5 qt5-qtwebengine
   ```

   **For Debian/Ubuntu:**
   ```bash
   sudo apt-get install python3-gi python3-gi-cairo gir1.2-gtk-3.0 python3-pyqt5 python3-pyqt5.qtwebengine
   ```

2. Set up Python environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install poetry
   poetry install
   ```

## Interactive SVG Features

This viewer supports SVG files with embedded Python code. Here's how to create interactive SVGs:

1. **Embed Python Code**:
   ```xml
   <script type="application/python" id="pyCode">
   # Your Python code here
   radius = 30
   result = {"radius": radius, "area": 3.14 * radius**2}
   </script>
   ```

2. **JavaScript Integration**:
   ```javascript
   function executePython() {
     var code = document.getElementById('pyCode').textContent;
     window.pywebview.api.execute_script(code).then(function(response) {
       // Handle Python response
       var result = JSON.parse(response);
       // Update SVG elements
     });
   }
   ```

3. **Example Interactive Elements**:
   - Buttons that trigger Python code
   - Dynamic updates to SVG elements
   - Two-way communication between SVG and Python

## Usage

### Basic Usage

```bash
# View an SVG file
python viewer.py img.svg

# Using Poetry
poetry run run img.svg
```

### Interactive Example

Try the included example:

```bash
python viewer.py preview.svg
```

This will show an interactive SVG with a button that executes Python code and updates the SVG dynamically.

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
