import pytest
from unittest.mock import patch, MagicMock
from calc_app.plugins.add import addCommand

# Mock class to simulate the Command base class if needed
class MockCommand:
    def get_env_variable(self, var):
        if var == "DECIMAL_PLACES":
            return "2"
        elif var == "SAVE_HISTORY":
            return "True"
    
    def record_history(self, operation, a, b, result):
        pass

class TestAddCommand(MockCommand, addCommand):
    pass

@pytest.fixture
def add_command():
    return TestAddCommand()

def test_execute_success(add_command):
    with patch('builtins.input', side_effect=["3", "4"]), \
         patch.object(add_command, 'get_env_variable', side_effect=["2", "True"]), \
         patch.object(add_command, 'record_history') as mock_record_history:

        add_command.execute()
        
        mock_record_history.assert_called_once_with("Add", "3", "4", 7.0)

def test_execute_invalid_input(add_command, capsys):
    with patch('builtins.input', side_effect=["three", "4"]), \
         patch.object(add_command, 'get_env_variable', side_effect=["2", "True"]):

        add_command.execute()
        
        captured = capsys.readouterr()
        assert "Invalid input. Please enter numeric values." in captured.out

def test_execute_no_history(add_command):
    with patch('builtins.input', side_effect=["5", "6"]), \
         patch.object(add_command, 'get_env_variable', side_effect=["2", "False"]), \
         patch.object(add_command, 'record_history') as mock_record_history:

        add_command.execute()
        
        mock_record_history.assert_not_called()

def test_execute_invalid_decimal_places(add_command, capsys):
    with patch('builtins.input', side_effect=["5", "6"]), \
         patch.object(add_command, 'get_env_variable', side_effect=["invalid", "True"]):

        add_command.execute()
        
        captured = capsys.readouterr()
        assert "Invalid input. Please enter numeric values." in captured.out