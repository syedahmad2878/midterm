
#from calc_app.commands.command_handler import CommandHandler
#from calc_app.commands.add import addCommand
#from calc_app import commands, Command, CommandHandler, addCommand, subCommand, multiCommand, divideCommand, exitCommand, greetCommand, goodbyeCommand, menuCommand, readEnviornment
from calc_app.commands import Command, CommandHandler
from dotenv import load_dotenv, dotenv_values
import os
import logging
import logging.config
import pkgutil
import importlib
import sys

#def main():
#    handler = CommandHandler()
#    command = addCommand()
#    command.execute()

#if __name__ == "__main__":
 #   main()
class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        self.configure_logging()
        #self.settings = self.load_environment_variables()
       # print(self.settings['ENVIRONMENT'])
        self.start()
        
    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename="app.log")
        
        logging.info("Logging configured.")
    
   
    def load_plugins(self):
        plugins_package = 'calc_app.plugins'
        plugins_path = plugins_package.replace('.', '/')
        
        if not os.path.exists(plugins_path):
            logging.warning(f"Plugins directory '{plugins_path}' not found.")
            return
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
            if is_pkg:
                try:
                    comp_plugin_package = f'{plugins_package}.{plugin_name}'
                    
                    plugin_module = importlib.import_module(comp_plugin_package,)
                    
                    self.register_plugin_commands(plugin_module, plugin_name)
                    
                except ImportError as e:
                    logging.error(f"Error importing plugin {plugin_name}: {e}")
                    

    def register_plugin_commands(self, plugin_module, plugin_name):
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                # Command names are now explicitly set to the plugin's folder name
                self.command_handler.register_command(plugin_name, item())
                
                logging.info(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")


    def start(self):
       
        self.load_plugins()
        logging.info("Application started. Type 'exit' to exit.")
        try:
            while True:
                cmd_input = input(">>> ").strip()
                if cmd_input.lower() == 'exit':
                    logging.info("Application exit.")
                    sys.exit(0)  # Use sys.exit(0) for a clean exit, indicating success.
                try:
                    self.command_handler.execute_command(cmd_input)
                except KeyError:  # Assuming execute_command raises KeyError for unknown commands
                    logging.error(f"Unknown command: {cmd_input}")
                    sys.exit(1)  # Use a non-zero exit code to indicate failure or incorrect command.
        except KeyboardInterrupt:
            logging.info("Application interrupted and exiting gracefully.")
            sys.exit(0)  # Assuming a KeyboardInterrupt should also result in a clean exit.
        finally:
            logging.info("Application shutdown.")

if __name__ == "__main__":
    App()