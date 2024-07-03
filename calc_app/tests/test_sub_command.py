import pytest
from unittest.mock import patch, MagicMock
from calc_app.plugins.subtract import subCommand

# Mock class to simulate the Command base class if needed
class MockCommand:
    def get_env_variable(self, var):
        if var == "DECIMAL_PLACES":
            return "2"
        elif var == "SAVE_HISTORY":
            return "True"
    
    def record_history(self, operation, a, b, result):
        pass

class TestSubCommand(MockCommand, subCommand):
    pass

@pytest.fixture
def sub_command():
    return TestSubCommand()

def test_execute_success(sub_command):
    with patch('builtins.input', side_effect=["10", "4"]), \
         patch.object(sub_command, 'get_env_variable', side_effect=["2", "True"]), \
         patch.object(sub_command, 'record_history') as mock_record_history:

        sub_command.execute()
        
        mock_record_history.assert_called_once_with("Subtract", "10", "4", 6.0)

def test_execute_invalid_input(sub_command, capsys):
    with patch('builtins.input', side_effect=["ten", "4"]), \
         patch.object(sub_command, 'get_env_variable', side_effect=["2", "True"]):

        sub_command.execute()
        
        captured = capsys.readouterr()
        assert "Invalid input. Please enter numeric values." in captured.out

def test_execute_no_history(sub_command):
    with patch('builtins.input', side_effect=["5", "3"]), \
         patch.object(sub_command, 'get_env_variable', side_effect=["2", "False"]), \
         patch.object(sub_command, 'record_history') as mock_record_history:

        sub_command.execute()
        
        mock_record_history.assert_not_called()

def test_execute_invalid_decimal_places(sub_command, capsys):
    with patch('builtins.input', side_effect=["8", "3"]), \
         patch.object(sub_command, 'get_env_variable', side_effect=["invalid", "True"]):

        sub_command.execute()
        
        captured = capsys.readouterr()
        assert "Invalid input. Please enter numeric values." in captured.out
