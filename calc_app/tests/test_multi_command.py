import pytest
from unittest.mock import patch, MagicMock
from calc_app.commands import Command
from calc_app.plugins.multiply import multiCommand

# Mock class to simulate the Command base class if needed
class MockCommand:
    def get_env_variable(self, var):
        if var == "DECIMAL_PLACES":
            return "2"
        elif var == "SAVE_HISTORY":
            return "True"
    
    def record_history(self, operation, a, b, result):
        pass

class TestMultiCommand(MockCommand, multiCommand):
    pass

@pytest.fixture
def multi_command():
    return TestMultiCommand()

def test_execute_success(multi_command):
    with patch('builtins.input', side_effect=["3", "4"]), \
         patch.object(multi_command, 'get_env_variable', side_effect=["2", "True"]), \
         patch.object(multi_command, 'record_history') as mock_record_history:

        with patch('builtins.print') as mock_print:
            multi_command.execute()
            
            mock_print.assert_any_call("The result is: 12.00")
            mock_record_history.assert_called_once_with("Multiply", "3", "4", 12.0)

def test_execute_invalid_input(multi_command, capsys):
    with patch('builtins.input', side_effect=["three", "4"]), \
         patch.object(multi_command, 'get_env_variable', side_effect=["2", "True"]):

        multi_command.execute()
        
        captured = capsys.readouterr()
        assert "Invalid input. Please enter numeric values." in captured.out

def test_execute_no_history(multi_command):
    with patch('builtins.input', side_effect=["5", "6"]), \
         patch.object(multi_command, 'get_env_variable', side_effect=["2", "False"]), \
         patch.object(multi_command, 'record_history') as mock_record_history:

        with patch('builtins.print') as mock_print:
            multi_command.execute()
            
            mock_print.assert_any_call("The result is: 30.00")
            mock_record_history.assert_not_called()

def test_execute_invalid_decimal_places(multi_command, capsys):
    with patch('builtins.input', side_effect=["5", "6"]), \
         patch.object(multi_command, 'get_env_variable', side_effect=["invalid", "True"]):

        multi_command.execute()
        
        captured = capsys.readouterr()
        assert "Invalid input. Please enter numeric values." in captured.out
