"""Shared pytest fixtures and configuration."""
import os
import tempfile
from pathlib import Path
from typing import Generator
from unittest.mock import Mock

import pytest


@pytest.fixture
def temp_dir() -> Generator[Path, None, None]:
    """Create a temporary directory for test files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def mock_requests_get(mocker):
    """Mock requests.get for testing HTTP calls."""
    mock = mocker.patch('requests.get')
    return mock


@pytest.fixture
def sample_domain_list():
    """Provide a sample domain list for testing."""
    return """
    # Sample domain list
    example.com
    test.example.org
    subdomain.test.com
    # Comment line
    another-domain.net
    """


@pytest.fixture
def sample_whitelist_content():
    """Provide sample whitelist content for testing."""
    return """
    [{
        "name": "white",
        "urlPattern": "*.example.com/*",
        "profileName": "direct",
        "id": "1"
    }]
    """


@pytest.fixture
def mock_config():
    """Provide a mock configuration object."""
    return {
        'domain_lists': [
            'https://example.com/domains.txt',
            'https://test.com/list.txt'
        ],
        'output_file': 'white-list.sorl',
        'mini_file': 'white-mini.sorl',
        'update_interval': 3600
    }


@pytest.fixture
def mock_file_operations(mocker):
    """Mock file read/write operations."""
    mock_open = mocker.mock_open()
    mocker.patch('builtins.open', mock_open)
    return mock_open


@pytest.fixture(autouse=True)
def reset_environment():
    """Reset environment variables before each test."""
    original_env = os.environ.copy()
    yield
    os.environ.clear()
    os.environ.update(original_env)


@pytest.fixture
def captured_logs(caplog):
    """Capture log messages during tests."""
    with caplog.at_level('DEBUG'):
        yield caplog