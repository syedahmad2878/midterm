from calc_app.commands import Command

class divideCommand(Command):
    def execute(self):
        a = input("Enter the first number: ")
        b = input("Enter the second number: ")
        try:
            c = float(a) / float(b)
            print(f"The result is: {c}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")