# Contributing to SVG Viewer

Thank you for your interest in contributing to SVG Viewer! We welcome contributions from everyone.

## Getting Started

1. **Fork** the repository on GitHub
2. **Clone** your fork locally
   ```bash
   git clone https://github.com/veridock/svg-viewer.git
   cd svg-viewer
   ```
3. **Set up** the development environment:
   ```bash
   # Install system dependencies (requires sudo)
   sudo ./setup_env.sh

   # Set up Python environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -e .[dev]
   ```
4. **Install pre-commit hooks**
   ```bash
   pre-commit install
   ```

## Development Workflow

1. **Create a new branch** for your feature or bugfix
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. **Make your changes** following the coding standards
3. **Run tests** to ensure everything works
   ```bash
   make test
   ```
4. **Commit your changes** with a descriptive message
   ```bash
   git commit -m "Add your commit message here"
   ```
5. **Push** to your fork
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Create a Pull Request** against the main branch

## Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code
- Use [Google Style Docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
- Keep lines under 88 characters (Black formatter will handle this)
- Type hints are encouraged for better code maintainability

## Testing

- Write tests for new features and bug fixes
- Run tests with: `make test`
- Aim for good test coverage (currently: [![Coverage](https://img.shields.io/badge/coverage-XX%25-yellow)]())

## Reporting Issues

When reporting issues, please include:
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Environment details (OS, Python version, etc.)
- Any relevant error messages or logs

## Code of Conduct

This project adheres to the Contributor Covenant [code of conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

## License

By contributing, you agree that your contributions will be licensed under the project's [MIT License](LICENSE).

## Getting Help

If you have any questions, feel free to open an issue or reach out to the maintainers.
