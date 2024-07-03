from calc_app.commands import Command
from dotenv import load_dotenv
import os
class envCommand(Command):
    def execute(self):
        load_dotenv()
        try:

            while True:
                print("1   for Save History.")
                print("2   for Set Decimal Place")
                print("0   for Exit")
                userInput = input("<<<<<< ")
                if userInput == "1":
                    a = input("Do you want to Save History. y/n: ")
                    if a == 'y':
                        os.environ["SAVE_HISTORY"] = "True"
                    if a == 'n':
                        os.environ["SAVE_HISTORY"] = "False"
                    else:
                        print("Wrong input")
                if userInput == "2":
                    c = int(input("Enter the desire decimal place: "))
                    
                    
                    if not isinstance(c, int):
                        raise ValueError("decimal_places must be an integer")
                    os.environ["DECIMAL_PLACES"] = str(c)
                    print("Decimal Places is set to " + str(c))
                if userInput == "0":
                    break
        except ValueError:
            print("Invalid input. Please enter numeric values.")