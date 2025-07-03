#!/bin/bash

# Exit on error
set -e

echo "=== SVG Viewer Environment Setup ==="

# Check if running as root
if [ "$EUID" -ne 0 ]; then
    echo "This script needs root privileges to install system packages."
    echo "Please run with sudo or as root."
    exit 1
fi

# Detect Linux distribution
if [ -f /etc/fedora-release ]; then
    echo "Detected Fedora Linux"

    # Update package lists
    echo "Updating package lists..."
    dnf update -y

    # Install system dependencies for GTK
    echo "Installing system dependencies for GTK..."
    dnf install -y python3-gobject gtk3 webkit2gtk3

    # Install system dependencies for Qt (alternative backend)
    echo "Installing system dependencies for Qt..."
    dnf install -y python3-qt5 qt5-qtwebengine

elif [ -f /etc/debian_version ]; then
    echo "Detected Debian/Ubuntu Linux"

    # Update package lists
    echo "Updating package lists..."
    apt-get update

    # Install system dependencies for GTK
    echo "Installing system dependencies for GTK..."
    apt-get install -y python3-gi python3-gi-cairo gir1.2-gtk-3.0

    # Install system dependencies for Qt (alternative backend)
    echo "Installing system dependencies for Qt..."
    apt-get install -y python3-pyqt5 python3-pyqt5.qtwebengine
else
    echo "Unsupported Linux distribution. Please install the following packages manually:"
    echo "- Python GTK3 bindings (python3-gobject, gtk3, webkit2gtk3)"
    echo "- PyQt5 (python3-qt5, qt5-qtwebengine)"
    exit 1
fi

# Create a virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install Python dependencies
echo "Installing Python dependencies..."
pip install poetry
poetry install

echo -e "\n=== Setup Complete ==="
echo "To run the SVG viewer, use:"
echo "  source venv/bin/activate"
echo "  python viewer.py path/to/your/image.svg"
echo ""
echo "For development, you can also use:"
echo "  make test    # Run tests"
echo "  make lint    # Run linters"
echo "  make format  # Format code"

# Make the script executable
chmod +x setup_env.sh
