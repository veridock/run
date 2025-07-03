"""SVG Viewer - A simple SVG viewer with Python scripting support.

This module provides a simple way to view SVG files with support for
embedded Python scripts within the SVG files.
"""

__version__ = "0.1.0"

import os
import platform
import sys

# Configure environment variables before any other imports
os.environ["PYWEBVIEW_GUI"] = "qt"  # Force Qt backend
os.environ["PYTHONWARNINGS"] = "ignore"  # Suppress some warnings

# Import webview after setting environment variables
import webview  # noqa: E402


class Api:
    """API class exposed to the webview for executing Python code.

    This class provides methods that can be called from JavaScript within the SVG.
    """

    def execute_script(self, code):
        try:
            local_vars = {}
            exec(code, globals(), local_vars)
            result = local_vars.get("result", "Script executed successfully")
            print(f"Script executed. Result: {result}")
            return result
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            print(error_msg, file=sys.stderr)
            import traceback

            traceback.print_exc()
            return error_msg


def main():
    """Run the SVG viewer with the file specified in command line arguments.

    Usage:
        python -m svg_viewer path/to/file.svg
    """
    if len(sys.argv) != 2:
        print("Usage: python viewer.py <svg_file>")
        sys.exit(1)

    svg_path = os.path.abspath(sys.argv[1])

    if not os.path.exists(svg_path):
        print(f"File {svg_path} not found", file=sys.stderr)
        sys.exit(1)

    print("\n=== SVG Viewer Starting ===")
    print(f"Python: {platform.python_version()}")
    print(f"File: {svg_path}")

    try:
        from PyQt5.QtCore import QT_VERSION_STR

        print(f"PyQt5 version: {QT_VERSION_STR}")
    except ImportError as e:
        print("PyQt5 not available:", str(e))
        sys.exit(1)

    print("\nCreating webview window...")
    try:
        api = Api()
        window = webview.create_window(
            "SVG Viewer",
            f"file://{svg_path}",
            js_api=api,
            width=1024,
            height=768,
            min_size=(800, 600),
            text_select=True,
        )
        print("Starting webview...")
        webview.start(debug=True)
    except Exception as e:
        print(f"\n=== ERROR ===")
        print(f"Failed to start the application: {str(e)}")
        print("\nTroubleshooting steps:")
        print(
            "1. Make sure all dependencies are installed: pip install pywebview PyQt5 PyQtWebEngine qtpy"
        )
        print("2. If using conda, try: conda install -c conda-forge pyqt pyqtwebengine")
        print(
            "3. Check if Qt is working with: python -c 'from PyQt5.QtWidgets import QApplication; print(\"Qt is working!\")'"
        )
        import traceback

        traceback.print_exc()
        sys.exit(1)

    print("\nSVG Viewer closed")


def _simple_viewer_main():
    """Internal function to run a simple SVG viewer using PyQt5 directly.

    This is used as a fallback when the main webview fails to initialize.
    """
    """A simple SVG viewer implementation using PyQt5 directly.

    This function is used for testing and as a fallback when pywebview is not available.
    """
    import sys

    from PyQt5.QtCore import QUrl
    from PyQt5.QtWebEngineWidgets import QWebEngineView
    from PyQt5.QtWidgets import QApplication

    if len(sys.argv) != 2:
        print("Usage: python viewer.py <svg_file>")
        sys.exit(1)

    svg_path = os.path.abspath(sys.argv[1])

    if not os.path.exists(svg_path):
        print(f"File {svg_path} not found")
        sys.exit(1)

    app = QApplication(sys.argv)
    web = QWebEngineView()
    web.setWindowTitle("SVG Viewer")
    web.load(QUrl.fromLocalFile(svg_path))
    web.show()
    sys.exit(app.exec_())


# Public API
__all__ = ["Api", "main", "__version__"]

if __name__ == "__main__":
    # Try to run the main webview-based viewer first
    try:
        main()
    except Exception as e:
        print(f"Error with webview: {e}", file=sys.stderr)
        print("Falling back to simple viewer...")
        _simple_viewer_main()
