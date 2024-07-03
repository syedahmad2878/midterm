import pytest
from unittest.mock import patch, MagicMock
from calc_app.plugins.divide import divideCommand

# Mock class to simulate the Command base class if needed
class MockCommand:
    def get_env_variable(self, var):
        if var == "DECIMAL_PLACES":
            return "2"
        elif var == "SAVE_HISTORY":
            return "True"
    
    def record_history(self, operation, a, b, result):
        pass

class TestDivideCommand(MockCommand, divideCommand):
    pass

@pytest.fixture
def divide_command():
    return TestDivideCommand()

def test_execute_success(divide_command):
    with patch('builtins.input', side_effect=["10", "2"]), \
         patch.object(divide_command, 'get_env_variable', side_effect=["2", "True"]), \
         patch.object(divide_command, 'record_history') as mock_record_history:

        divide_command.execute()
        
        mock_record_history.assert_called_once_with("divide", "10", "2", 5.0)

def test_execute_invalid_input(divide_command, capsys):
    with patch('builtins.input', side_effect=["ten", "2"]), \
         patch.object(divide_command, 'get_env_variable', side_effect=["2", "True"]):

        divide_command.execute()
        
        captured = capsys.readouterr()
        assert "Invalid input. Please enter numeric values." in captured.out

def test_execute_no_history(divide_command):
    with patch('builtins.input', side_effect=["10", "2"]), \
         patch.object(divide_command, 'get_env_variable', side_effect=["2", "False"]), \
         patch.object(divide_command, 'record_history') as mock_record_history:

        divide_command.execute()
        
        mock_record_history.assert_not_called()

def test_execute_invalid_decimal_places(divide_command, capsys):
    with patch('builtins.input', side_effect=["8", "2"]), \
         patch.object(divide_command, 'get_env_variable', side_effect=["invalid", "True"]):

        divide_command.execute()
        
        captured = capsys.readouterr()
        assert "Invalid input. Please enter numeric values." in captured.out

def test_execute_zero_division(divide_command, capsys):
    with patch('builtins.input', side_effect=["8", "0"]), \
         patch.object(divide_command, 'get_env_variable', side_effect=["2", "True"]):

        divide_command.execute()
        
        captured = capsys.readouterr()
        assert "Error: Division by zero is not allowed." in captured.out
