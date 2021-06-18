#  Menu class where controls for the start menu and instructions will be passed
# Start, where the player can exit, start, or see the intructions.
import sys
import time
from  user import User
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
            self.u_name = self.make_u_name()
            self.p_word = self.make_p_word()
            self.user = User(self.u_name, self.p_word)
            self.user.auth()
        elif chosen == '2':
            self.instructions()
        elif chosen == '3':
            sys.exit
        else:
            print("Invalid Command! ")
		
    def make_u_name(self):
        # This is to enter the user_name of the code
        self.username = input("Enter user_name: ")
        return self.username
        
    def make_p_word(self):
        # This is to enter the p_word of the code
        self.p_word = input("Enter p_word: ")
        return self.p_word
	
    def instructions(self):
        filename = "instructions.txt"

        with open(filename, 'r') as f:
            content = f.readlines()
            
        for line in content:
            time.sleep(2)
            print(line)

        f.close()