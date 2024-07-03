from calc_app.commands import Command



class menuCommand(Command):  # Assuming Command is defined elsewhere
    def __init__(self, app_instance):
        self.app_instance = app_instance

    def execute(self):
        print("Available commands:")
        for command in self.app_instance.get_commands_list():
            print(command)
