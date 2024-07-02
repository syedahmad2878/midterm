import pytest
from calc_app.plugins.add import addCommand
from unittest.mock import patch
from io import StringIO

def test_add_command_valid_input(monkeypatch, capsys):
    # Mock input to return '2' and '3'
    inputs = iter(['2', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create an instance of addCommand and execute
    cmd = addCommand()
    cmd.execute()

    # Capture the output and check
    captured = capsys.readouterr()
    assert "The result is: 5.0" in captured.out

def test_add_command_invalid_input(monkeypatch, capsys):
    # Mock input to return 'a' and '3'
    inputs = iter(['a', '3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Create an instance of addCommand and execute
    cmd = addCommand()
    cmd.execute()

    # Capture the output and check
    captured = capsys.readouterr()
    assert "Invalid input. Please enter numeric values." in captured.out