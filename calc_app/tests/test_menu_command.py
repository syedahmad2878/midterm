import pytest
from unittest.mock import MagicMock
from calc_app.commands import Command
from calc_app.plugins.menu import menuCommand

class MockAppInstance:
    def get_commands_list(self):
        return ["command1", "command2", "command3"]

class TestMenuCommand(menuCommand):
    pass

@pytest.fixture
def menu_command():
    app_instance = MockAppInstance()
    return TestMenuCommand(app_instance)

def test_execute_menu_command(menu_command, capsys):
    menu_command.execute()
    
    captured = capsys.readouterr()
    output = captured.out.strip().split("\n")
    
    assert "Available commands:" in output
    assert "command1" in output
    assert "command2" in output
    assert "command3" in output
