from calc_app.commands import Command

class subCommand(Command):
    def execute(self):
        a = input("Enter the first number: ")
        b = input("Enter the second number: ")
        try:
            c = float(a) - float(b)
            decimal_places = int(self.get_env_variable("DECIMAL_PLACES"))
            if not isinstance(decimal_places, int):
                raise ValueError("decimal_places must be an integer")
            formatted = "{:.{}f}".format(c, decimal_places)
            print(f"The result is: {formatted}")
            if self.get_env_variable("SAVE_HISTORY") == "True":
                self.record_history("Subtract", a, b, c)
        except ValueError:
            print("Invalid input. Please enter numeric values.")
