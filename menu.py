#  Menu class where controls for the start menu and instructions will be passed
# Start, where the player can exit, start, or see the intructions.
import sys
import time
import read_lines
class Menu:

    def __init__(self):
        self.start_game = False
    def start_menu(self):
        """
            This will act as the start menu of the program
            There will be 3 choices to start, exit and read the instructions.
        """
        
        print(
            "Welcome! This is Escape Forest\n\n", 
            "Here are the list of choices\n",
            "[1] Start Game.\n", "[2]Help!\n", 
            "[3]Exit\n"
            )

        self.choose()

    def choose(self):

        """ 
		    Starts different function depending on the choice
		    of the player. 
        """
        chosen = input("Choose: ")

        if chosen == '1':
            self.start_game = True
            
        elif chosen == '2':
            read_lines.read_lines('instructions.txt')

        elif chosen == '3':
            sys.exit
 
        else:
            print("Invalid Command! ")
