# Main file of the program where different parts of the app will be ran
from re import A
import sys
import psycopg2
from menu import Menu
from  user import User
from scenarios import Scenes
class Main:

    def __init__(self):
        # Initialize the variables
        self.menu = Menu()
        self.u_name = input("Add username: ")
        self.p_word = input("Add a password: ")
        self.scenarios = Scenes(self.u_name, self.p_word)
        self.user = User(self.u_name, self.p_word)
        # Other values

        self.has_logged_in = False
    def __run__(self):
        # Functions will ran here
        self.has_logged_in = self.user.auth()
        
        if self.has_logged_in == True:
            self.menu.start_menu()

            if self.menu.start_game is not False:
                    self.act()
            
            else:
                self.menu.start_menu()
        
        
    def act(self):
        self.scenarios.starting_scene()
        
if __name__ == '__main__':
    main = Main()
    main.__run__()
 