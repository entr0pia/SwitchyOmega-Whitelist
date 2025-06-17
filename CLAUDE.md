# Project Context

This is a Python project that generates whitelist rules for SwitchyOmega browser extension.

## Testing Infrastructure
- Package manager: Poetry (configured in pyproject.toml)
- Testing framework: pytest with coverage
- Test structure: tests/ directory with unit and integration subdirectories
- Test dependencies: pytest, pytest-cov, pytest-mock

## Running Tests
- Run all tests: `poetry run pytest`
- Run with verbose output: `poetry run pytest -v`
- Run specific test file: `poetry run pytest tests/test_file.py`
- Run tests by marker: `poetry run pytest -m unit`

## Test Commands
- `poetry run test` - Run all tests with coverage
- `poetry run tests` - Alternative command (both work)

## Code Quality Commands
The project doesn't currently have linting or type checking set up. If you add them, update this section.