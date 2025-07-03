"""Configuration and fixtures for pytest."""
import os
import sys
from pathlib import Path

import pytest

# Add the project root to the Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Set environment variables for testing
os.environ["PYTEST_RUNNING"] = "1"

# Disable GUI windows during tests
os.environ["PYTEST_DISABLE_GUI"] = "1"

# Configuration for pytest
pytest_plugins = [
    # Add any pytest plugins here
]

# Common test data directory
TEST_DATA_DIR = Path(__file__).parent / "test_data"


def pytest_configure(config):
    """Configure pytest with custom settings."""
    # Create test data directory if it doesn't exist
    TEST_DATA_DIR.mkdir(exist_ok=True)


@pytest.fixture(scope="session")
def test_data_dir():
    """Return the path to the test data directory."""
    return TEST_DATA_DIR


@pytest.fixture(scope="session")
def simple_svg():
    """Return a simple SVG string for testing."""
    return """<?xml version="1.0" encoding="UTF-8"?>
    <svg width="100" height="100" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
      <circle cx="50" cy="50" r="40" fill="red" />
    </svg>"""


@pytest.fixture(scope="session")
def interactive_svg():
    """Return an interactive SVG string for testing."""
    return """<?xml version="1.0" encoding="UTF-8"?>
    <svg width="200" height="200" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
      <circle id="testCircle" cx="100" cy="100" r="40" fill="blue" />
      <script type="text/python">
        result = "Script executed"
      </script>
    </svg>"""


@pytest.fixture
def temp_svg_file(tmp_path, simple_svg):
    """Create a temporary SVG file for testing."""
    svg_file = tmp_path / "test.svg"
    svg_file.write_text(simple_svg)
    return str(svg_file)


@pytest.fixture
def temp_interactive_svg_file(tmp_path, interactive_svg):
    """Create a temporary interactive SVG file for testing."""
    svg_file = tmp_path / "interactive.svg"
    svg_file.write_text(interactive_svg)
    return str(svg_file)
