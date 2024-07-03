from calc_app.commands import Command
import sys
class exitCommand(Command):
    def execute(self):
        print("Goodbye")
        sys.exit(0)
    