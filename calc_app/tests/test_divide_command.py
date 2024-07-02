import pytest
from calc_app.plugins.divide import divideCommand
from io import StringIO
import sys

class MockInput:
    def __init__(self, inputs):
        self.inputs = inputs
        self.index = 0

    def __call__(self, _):
        input_value = self.inputs[self.index]
        self.index += 1
        return input_value

def test_divide_command_valid_input(monkeypatch):
    # Arrange
    inputs = ['10', '2']
    monkeypatch.setattr('builtins.input', MockInput(inputs))
    command = divideCommand()
    captured_output = StringIO()
    sys.stdout = captured_output

    # Act
    command.execute()

    # Assert
    sys.stdout = sys.__stdout__
    assert "The result is: 5.0" in captured_output.getvalue()

def test_divide_command_invalid_input(monkeypatch):
    # Arrange
    inputs = ['10', 'abc']
    monkeypatch.setattr('builtins.input', MockInput(inputs))
    command = divideCommand()
    captured_output = StringIO()
    sys.stdout = captured_output

    # Act
    command.execute()

    # Assert
    sys.stdout = sys.__stdout__
    assert "Invalid input. Please enter numeric values." in captured_output.getvalue()

def test_divide_command_division_by_zero(monkeypatch):
    # Arrange
    inputs = ['10', '0']
    monkeypatch.setattr('builtins.input', MockInput(inputs))
    command = divideCommand()
    captured_output = StringIO()
    sys.stdout = captured_output

    # Act
    command.execute()

    # Assert
    sys.stdout = sys.__stdout__
    assert "Error: Division by zero is not allowed." in captured_output.getvalue()
