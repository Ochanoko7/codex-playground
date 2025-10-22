from pathlib import Path
import sys

# Ensure the project root is available on the import path when pytest collects the test
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from hello import hello


def test_hello_prints_greeting(capsys):
    """hello() should print the expected greeting."""
    hello()
    captured = capsys.readouterr()
    assert captured.out == "Hello World!\n"
