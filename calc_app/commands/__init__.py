# Example content of commands/__init__.py
#from .command_handler import CommandHandler

from abc import ABC, abstractmethod
from pandas import DataFrame
import pandas as pd
from dotenv import load_dotenv
import os, datetime

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    def record_history(self, operation, operand1, operand2, result):
        # Create a DataFrame with operation, operands, and result
        history_data = {'Operation': operation, 'Operand1': operand1,
                        'Operand2': operand2, 'Result': result, 'Date': datetime.datetime.now()}
        history_df = DataFrame(history_data, index=[0])

        # Append to the history.csv file
        history_df.to_csv('history.csv', mode='a', header=False, index=False)

    def show_history(self):
        try:
            data = pd.read_csv("history.csv")
            if data.empty:
                print("History is already empty")
            else:
                print(data.to_string())
        except FileNotFoundError:
            print("History file 'history.csv' not found. No history to display.")
        except pd.errors.EmptyDataError:
            print("History is empty. No data to show.")
    
    def delete_history(self):
        try:    
            empty_df = pd.DataFrame(columns=[])    
            empty_df.to_csv("history.csv", index=False)
            print("Deleted all data from the CSV file.")
        except FileNotFoundError:
            print(f"Error: File 'history.csv' not found.")
    
    def save_history(self, save="True"):
        load_dotenv()
        os.environ["SAVE_HISTORY"] = save
    def get_env_variable(self,  envVar):
        load_dotenv()
        return os.getenv(envVar)

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command
        

    def execute_command(self, command_name: str):
        """ Look before you leap (LBYL) - Use when its less likely to work
        if command_name in self.commands:
            self.commands[command_name].execute()
        else:
            print(f"No such command: {command_name}")
        """
        """Easier to ask for forgiveness than permission (EAFP) - Use when its going to most likely work"""
        try:
            self.commands[command_name].execute()
        except KeyError:
            print(f"No such command: {command_name}")
