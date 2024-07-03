import pytest
from unittest.mock import patch, MagicMock
from calc_app.commands import Command
from calc_app.plugins.history import historyCommand

# Mock class to simulate the Command base class if needed
class MockCommand:
    def show_history(self):
        pass

    def delete_history(self):
        pass

    def save_history(self, save):
        pass

class TestHistoryCommand(MockCommand, historyCommand):
    pass

@pytest.fixture
def history_command():
    return TestHistoryCommand()

def test_show_history(history_command):
    with patch('builtins.input', side_effect=["1", "0"]), \
         patch.object(history_command, 'show_history') as mock_show_history:

        history_command.execute()
        
        mock_show_history.assert_called_once()

def test_delete_history(history_command):
    with patch('builtins.input', side_effect=["2", "0"]), \
         patch.object(history_command, 'delete_history') as mock_delete_history:

        history_command.execute()
        
        mock_delete_history.assert_called_once()

def test_save_history_yes(history_command):
    with patch('builtins.input', side_effect=["3", "y", "0"]), \
         patch.object(history_command, 'save_history') as mock_save_history:

        history_command.execute()
        
        mock_save_history.assert_called_once_with(save="True")

def test_save_history_no(history_command):
    with patch('builtins.input', side_effect=["3", "n", "0"]), \
         patch.object(history_command, 'save_history') as mock_save_history:

        history_command.execute()
        
        mock_save_history.assert_called_once_with(save="False")

def test_exit(history_command):
    with patch('builtins.input', side_effect=["0"]), \
         patch.object(history_command, 'show_history') as mock_show_history, \
         patch.object(history_command, 'delete_history') as mock_delete_history, \
         patch.object(history_command, 'save_history') as mock_save_history:

        history_command.execute()
        
        mock_show_history.assert_not_called()
        mock_delete_history.assert_not_called()
        mock_save_history.assert_not_called()
