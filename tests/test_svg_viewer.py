import os
import shutil
import sys
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

# Add the parent directory to the Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Import the viewer module
from viewer import Api
from viewer import main as viewer_main

# Test data
SIMPLE_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg width="100" height="100" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
  <circle cx="50" cy="50" r="40" fill="red" />
</svg>"""

INTERACTIVE_SVG = """<?xml version="1.0" encoding="UTF-8"?>
<svg width="200" height="200" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <circle id="testCircle" cx="100" cy="100" r="40" fill="blue" />
  <script type="text/python">
    result = "Script executed"
  </script>
</svg>"""


class TestApi:
    def test_execute_script_success(self):
        """Test that execute_script runs Python code correctly."""
        api = Api()
        result = api.execute_script("x = 5 + 3")
        assert result == "Script executed successfully"

    def test_execute_script_with_result(self):
        """Test that execute_script captures the result variable."""
        api = Api()
        result = api.execute_script("result = 'test result'")
        assert result == "test result"

    def test_execute_script_error(self):
        """Test that execute_script handles errors properly."""
        api = Api()
        result = api.execute_script("1 / 0")
        assert "Error" in result
        assert "ZeroDivisionError" in result


class TestSvgViewer:
    @pytest.fixture
    def temp_svg_file(self):
        """Create a temporary SVG file for testing."""
        with tempfile.NamedTemporaryFile(suffix=".svg", delete=False) as f:
            f.write(SIMPLE_SVG.encode("utf-8"))
            f.flush()
            yield f.name
        # Cleanup
        if os.path.exists(f.name):
            os.unlink(f.name)

    @pytest.fixture
    def temp_interactive_svg_file(self):
        """Create a temporary interactive SVG file for testing."""
        with tempfile.NamedTemporaryFile(suffix=".svg", delete=False) as f:
            f.write(INTERACTIVE_SVG.encode("utf-8"))
            f.flush()
            yield f.name
        # Cleanup
        if os.path.exists(f.name):
            os.unlink(f.name)

    @patch("viewer.webview")
    def test_main_with_valid_file(self, mock_webview, temp_svg_file):
        """Test that main function works with a valid SVG file."""
        # Mock the webview module functions
        mock_webview.create_window.return_value = "mock_window"

        # Call the main function with our test file
        with patch("sys.argv", ["viewer.py", temp_svg_file]):
            viewer_main()

        # Verify webview.create_window was called with the correct arguments
        mock_webview.create_window.assert_called_once()
        args, kwargs = mock_webview.create_window.call_args
        assert "SVG Viewer" in args
        assert "file://" in kwargs["url"]
        assert temp_svg_file in kwargs["url"]

        # Verify webview.start was called
        mock_webview.start.assert_called_once()

    @patch("viewer.sys.exit")
    @patch("builtins.print")
    def test_main_with_missing_file(self, mock_print, mock_exit):
        """Test that main function handles missing files correctly."""
        with patch("sys.argv", ["viewer.py", "nonexistent.svg"]):
            viewer_main()

        # Verify an error message was printed
        mock_print.assert_called()
        assert any("not found" in str(call) for call in mock_print.call_args_list)
        # Verify the program exited with error code 1
        mock_exit.assert_called_once_with(1)

    @patch("viewer.sys.exit")
    @patch("builtins.print")
    def test_main_without_arguments(self, mock_print, mock_exit):
        """Test that main function handles missing arguments correctly."""
        with patch("sys.argv", ["viewer.py"]):
            viewer_main()

        # Verify usage message was printed
        mock_print.assert_called_with("Usage: python viewer.py <svg_file>")
        # Verify the program exited with error code 1
        mock_exit.assert_called_once_with(1)

    @patch("viewer.QApplication")
    @patch("viewer.QWebEngineView")
    def test_simple_viewer(self, mock_web_view, mock_app, temp_svg_file):
        """Test the simple viewer implementation."""
        # Mock the QApplication instance
        mock_app_instance = MagicMock()
        mock_app.return_value = mock_app_instance

        # Mock the QWebEngineView instance
        mock_web_instance = MagicMock()
        mock_web_view.return_value = mock_web_instance

        # Import and test the simple viewer
        from viewer import simple_viewer_main

        with patch("sys.argv", ["viewer.py", temp_svg_file]):
            with patch("sys.exit") as mock_sys_exit:
                simple_viewer_main()

        # Verify QApplication was created
        mock_app.assert_called_once()

        # Verify QWebEngineView was created and configured
        mock_web_view.assert_called_once()
        mock_web_instance.setWindowTitle.assert_called_with("SVG Viewer")
        mock_web_instance.load.assert_called_once()
        mock_web_instance.show.assert_called_once()

        # Verify the application event loop was started
        mock_app_instance.exec_.assert_called_once()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
