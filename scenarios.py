# This is the part where all scenarios are typed our or played out.
from pull import Pull
from combat import Combat
from merchant import Merchant
class Scenes:


    def __init__(self, u_name, password):
        self.u_name = u_name
        self.password = password
        self.merchant = Merchant(self.u_name, self.password)
        self.pull = Pull(self.u_name, self.password)
    def starting_scene(self):
        print(
            "Huff! Huff! Those zombies are everywhere! I don't know if I can escape\nn",
            "This damned forest! How did this happen!(Flashback)\n",
            "Drafted by that damned king I was forced into the frontlines of the forest of Acacia\n",
            "This dreaded forest consisted of ghastly trees, vicious monsters, and a thick fog",
            "Sensing danger and death our commander ordered for someone to get out of the forest and ",
            "ask for reinforcements. Being close to him I was picked. Unfortunately, zombies noticed me moving",
            " and have been hunting me ever since.", "Damn it! How can I escape this! "
            )
        self.enter_combat_zombies()

    def enter_combat_zombies(self):
        self.monster = 'zombies'
        if self.conditions(self.monster)is True:
            self.diverging_of_path()

        else:
            self.enter_combat_zombies()

    def diverging_of_path(self):
        print("Gasp... Gasp... Luckily I made it out there! Now where should I go...")
        print(
            "[1] A simple looking path to the left.\n",
            "[2] The weird looking temple at the center.\n",
            "[3] The twisted trees at the right.")
        self.choose = input("Choose: ")
        if self.choose == '1':
            self.wolves()

        elif self.choose == '2':
            self.entering_temple()

        elif self.choose == '3':
            self.twisted_trees()

    def twisted_trees(self):
        print(
            "(Sounds of crickets and howls) Are there wolves here?",
            "Hopefully there isn't or I'm toast.... Damnnnn ittttt.",
            "Why did I choose this path.(Hears clanking noises)",
            "Damn it! Better get ready."
 )
        self.enter_skeletons()

    def enter_skeletons(self):       
        self.monster = 'skeletons'
        if self.conditions(self.monster) is True:
            self.zombies_again()

        else:
            self.enter_skeletons()
    def zombies_again(self):
        print(
            "Sighhhh.... Luckily I survived...(Walks away)\n",
            "Looks like I'm now at the end of this damn trees.",
            "(Looks around) Damnnnnn Where am I?(Grrrrrr.....)",
            "Oh crap looks like I have to do this all over again."
            )
        self.enter_zombies() 
    def enter_zombies(self):
        self.monster = 'zombies'
        if self.conditions(self.monster) is True:
            self.end()

        else:
            self.enter_zombies()
        
    def wolves(self):
        print(
            "This path looks easy as I thought it would be!\n",
            "Looks like this would be a breeze!(Hears howls)",
            "Wha-!(Wolves Enter) Mother-"
            )
        self.enter_wolves()

    def enter_wolves(self):
        self.monster = 'wolves'
        if self.conditions(self.monster) is True:
            self.end()

        else:
            self.enter_wolves() 
    def entering_temple(self):
        print(
            "This temple is sure looking old! Hmmm... better be ",
            "Better be on the look out..."
            "(Hears voice) Wha---\n\n (Merchant): Hey kid! You want some items?"
            "Sure...."
            )
        
        if self.merchant.menu() is True:
            self.end()
        
        else:
            self.merchant.menu()

    def conditions(self, monsters):
        self.combat = Combat(self.u_name, self.password, monsters)
        if  self.combat.options() is True:
            return True
        
        else:
           return False 




       


    def end(self):
        # This is the end of the game.
        print("I made it out! Damn what should I do next....")
        self.pull.restart()