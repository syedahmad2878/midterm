# calc_app/tests/test_add_command.py
from calc_app.plugins.subtract.sub_command import subCommand
import pytest

@pytest.fixture
def command():
    return subCommand()

def test_execute_addition(monkeypatch, command):
    inputs = iter(['3', '2'])

    def mock_input(prompt):
        return next(inputs)

    results = []

    def mock_print(x):
        results.append(x)

    monkeypatch.setattr('builtins.input', mock_input)
    monkeypatch.setattr('builtins.print', mock_print)  # Capture print output during test

    command.execute()

    assert results == ['The result is: 1.0']  # Adjust expected output to match actual output