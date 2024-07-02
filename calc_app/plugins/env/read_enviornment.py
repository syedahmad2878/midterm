from calc_app.commands import Command
from dotenv import load_dotenv, dotenv_values
import logging
import os

class readEnviornment(Command):
    def __init__(self):
        self.env_file_path = os.path.join(os.path.dirname(__file__), "..", ".env")
        print (self.env_file_path)

    def execute(self):
        
        current_dir = os.path.dirname(__file__)
        plugin_dir = os.path.dirname(current_dir)
        parent_dir = os.path.dirname(plugin_dir)
        
        self.env_file_path = os.path.join(parent_dir, ".env")
        load_dotenv(self.env_file_path)
        settings = dotenv_values(self.env_file_path)
        # logging.info("Environment variables loaded.")
        key = input("Enter the Key: ").strip()
        value = settings.get(key)
        if value is not None:
            print(value)
        else:
            print(f"Key '{key}' not found.")