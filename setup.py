from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="run",
    version="0.1.0",
    description="A simple SVG viewer with Python scripting support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Tom Sapletta",
    author_email="info@softreck.dev",
    packages=find_packages(),
    install_requires=[
        "pywebview>=4.0.0",
        "PyQt5>=5.15.0",
        "PyQtWebEngine>=5.15.0",
        "qtpy>=2.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=3.0.0",
            "pytest-mock>=3.10.0",
            "black>=22.0.0",
            "isort>=5.0.0",
            "flake8>=4.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "run=viewer:main",
        ],
    },
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Graphics :: Viewers",
    ],
)
