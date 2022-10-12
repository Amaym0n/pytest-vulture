"""The conftest"""
from pathlib import Path
from shutil import copytree
from test import TEST_BASE_DIR

import pytest


@pytest.fixture
def examples_path(tmp_path):
    """Get copies of the example"""
    mock_dir = Path(TEST_BASE_DIR + "/test/examples")
    copytree(
        mock_dir,
        tmp_path / "examples"
    )
    return tmp_path / "examples"
