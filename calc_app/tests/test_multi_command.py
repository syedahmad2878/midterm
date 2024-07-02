import pytest
from unittest.mock import patch, MagicMock
from calc_app.commands import Command
from calc_app.plugins.multiply import multiCommand

def test_multi_command_valid_inputs():
    # Mock the input function to return specific values
    with patch('builtins.input', side_effect=['3', '4']), patch('builtins.print') as mock_print:
        cmd = multiCommand()
        cmd.execute()
        mock_print.assert_called_with("The result is: 12.0")

def test_multi_command_invalid_inputs():
    # Mock the input function to return invalid values
    with patch('builtins.input', side_effect=['a', 'b']), patch('builtins.print') as mock_print:
        cmd = multiCommand()
        cmd.execute()
        mock_print.assert_called_with("Invalid input. Please enter numeric values.")

def test_multi_command_mixed_invalid_valid_inputs():
    # Mock the input function to return mixed values
    with patch('builtins.input', side_effect=['5', 'b']), patch('builtins.print') as mock_print:
        cmd = multiCommand()
        cmd.execute()
        mock_print.assert_called_with("Invalid input. Please enter numeric values.")

def test_multi_command_zero_input():
    # Mock the input function to return zero and another number
    with patch('builtins.input', side_effect=['0', '5']), patch('builtins.print') as mock_print:
        cmd = multiCommand()
        cmd.execute()
        mock_print.assert_called_with("The result is: 0.0")
