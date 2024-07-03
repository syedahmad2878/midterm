from calc_app.commands import Command

class historyCommand(Command):
    def execute(self):
        
        while True:
            print("1   for show history")
            print("2   for delete history")
            print("3   for Save History")
            print("0   for Exit")
            a = input(">>>>>> ")
            if a == "1":
                self.show_history()
            if a == "2":
                self.delete_history()
            if a == "3":
                userInput = input("Do you want to Save History. y/n: ")
                if userInput == 'y':
                    self.save_history(save="True")
                if userInput == 'n':
                    self.save_history(save="False")                    
            if a == "0":
                break