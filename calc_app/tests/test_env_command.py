import pytest
from unittest.mock import patch, MagicMock
import os
from calc_app.commands import Command
from calc_app.plugins.env import envCommand

# Mock class to simulate the Command base class if needed
class MockCommand:
    pass

class TestEnvCommand(MockCommand, envCommand):
    pass

@pytest.fixture
def env_command():
    return TestEnvCommand()

def test_save_history_yes(env_command):
    with patch('builtins.input', side_effect=["1", "y", "0"]), \
         patch('os.environ', {}):

        with patch('builtins.print') as mock_print:
            env_command.execute()
            
            assert os.environ["SAVE_HISTORY"] == "True"
            mock_print.assert_any_call("1   for Save History.")
            mock_print.assert_any_call("2   for Set Decimal Place")
            mock_print.assert_any_call("0   for Exit")

def test_save_history_no(env_command):
    with patch('builtins.input', side_effect=["1", "n", "0"]), \
         patch('os.environ', {}):

        with patch('builtins.print') as mock_print:
            env_command.execute()
            
            assert os.environ["SAVE_HISTORY"] == "False"
            mock_print.assert_any_call("1   for Save History.")
            mock_print.assert_any_call("2   for Set Decimal Place")
            mock_print.assert_any_call("0   for Exit")

def test_set_decimal_place(env_command):
    with patch('builtins.input', side_effect=["2", "3", "0"]), \
         patch('os.environ', {}):

        with patch('builtins.print') as mock_print:
            env_command.execute()
            
            assert os.environ["DECIMAL_PLACES"] == "3"
            mock_print.assert_any_call("Decimal Places is set to 3")
            mock_print.assert_any_call("1   for Save History.")
            mock_print.assert_any_call("2   for Set Decimal Place")
            mock_print.assert_any_call("0   for Exit")

def test_invalid_input(env_command, capsys):
    with patch('builtins.input', side_effect=["2", "invalid", "0"]), \
         patch('os.environ', {}):

        env_command.execute()
        
        captured = capsys.readouterr()
        assert "Invalid input. Please enter numeric values." in captured.out

def test_wrong_input(env_command, capsys):
    with patch('builtins.input', side_effect=["1", "maybe", "0"]), \
         patch('os.environ', {}):

        env_command.execute()
        
        captured = capsys.readouterr()
        assert "Wrong input" in captured.out
