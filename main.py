# Main file of the program where different parts of the app will be ran
from re import A
import sys
import psycopg2
from auth import Auth
from menu import Menu
from scenarios import Scenes
class Main:

    def __init__(self):
        # Initialize the variables
        self.username = input("Add a username: ")
        self.password = input("Add a password: ")
        self.auth = Auth(self.username, self.password)
        self.menu = Menu(self.username, self.password)
        self.scenes = Scenes(self.username, self.password)
        # Other values

        self.has_logged_in = False

    # Make a function that puts the username and password
    # Make a function asking if the player want to log_in or register

    def __run__(self):
        # Functions will ran here
        if self.auth.auth() == True:
            self.menu.start_menu()
            if self.menu.choose() is True:
                    self.act()
            
            else:
                self.menu.choose()
        
        
    def act(self):
        self.scenes.starting_scene()
    
    def add_u_name(self):
        return [input("Add a username: ")]

    def add_a_password(self):
        return (input("Add a password: "))
if __name__ == '__main__':
    main = Main()
    main.__run__()
 