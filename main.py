# Main file of the program where different parts of the app will be ran
import sys
import psycopg2
from menu import Menu
from scenarios import Scenes
class Main:

    def __init__(self):
        # Initialize the variables
        self.menu = Menu()
        self.scenarios = Scenes()

    def __run__(self):
        # Functions will ran here

        if self.menu.start_game is not False:
            while True:
                self.act()
        
        else:
             self.menu.start_menu()
    
        
    def act(self):
        self.scenarios.starting_scene()
        self.scenarios.second_act()

if __name__ == '__main__':
    main = Main()
    main.__run__()
    