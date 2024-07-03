import pytest
from unittest.mock import patch
from calc_app.plugins.exit import exitCommand
import sys

# Mock class to simulate the Command base class if needed
class MockCommand:
    pass

class TestExitCommand(MockCommand, exitCommand):
    pass

@pytest.fixture
def exit_command():
    return TestExitCommand()

def test_execute_exit(exit_command, capsys):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        exit_command.execute()
    
    captured = capsys.readouterr()
    assert "Goodbye\n" in captured.out
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0