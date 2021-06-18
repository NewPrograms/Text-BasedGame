# Main file of the program where different parts of the app will be ran
import sys
import psycopg2
from menu import Menu


class Main:

    def __init__(self):
        # Initialize the variables
        self.menu = Menu()

    def __run__(self):
        # Functions will ran here
        self.menu.start_menu()

        if self.menu.start_game is not False:
            while True:
                pass
                

if __name__ == '__main__':
    main = Main()
    main.__run__()
    