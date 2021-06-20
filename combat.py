import time
import sys
from monster import Monster
from create import Create, Pull
from numpy.random import choice
from calc_poss import Calculate
class Combat:

    def __init__(self, username, password):
        self.pull = Pull() 
        self.calculate_poss = Calculate(username, password)        
        self.monster = Monster()
    def options(self):

        print(
            "[1] Attack!\n",
            "[2] Run!\n",
            "[3] Defend!\n",
            "[4] Hide!\n"
                )
        return self.results()

    def results(self):

        chosen = input("Choose: ")


        if chosen == "1":

            pass

        elif chosen == "2":

            if self.run() == "Successful":
                return True

            else:
                self.res = self.monster.attack(self.calculate_poss.undeadmon_att_succ())

                if self.res == 'Miss':
                    print("It missed!")
                    statement = "player, monsters SET player.stamina = -5," +
                                 " monsters.stamina = -5, WHERE monsters.monster_name = zombies"
                    self.pull.update_values(statement)

                else:
                    print("You got hit! -{} health points")
                    statement = "player, monsters SET player.health = {} monster.stamina = -5, WHERE monsters.monster_name = zombies".format()
                return False
        elif chosen == "3":

            pass

        elif chosen == "4":

            self.result = self.hide()
            return self.hide
        
        else:
            print("Invalid Choice!")
            sys.exit()
        


    def run(self):
        
        # Get the value from calc_success
        # and calculate it to get the weights of choices


        choices = ['Successful', 'You got hit!']

        return choice(choices, p=[self.calculate_poss.calc_success(), self.calculate_poss.calc_fail() ])

    def hide(self):
           choices = ['Successful', 'The creature saw you!', 'The creature saw you and pounced at you!']
           return choice(choices,  p=[0.2, 0.5, 0.3])

    def attack(self):
        pass

    def countdown(time_sec):
        while time_sec:

            mins, secs = divmod(time_sec, 60)

            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            
            print(timeformat, end='\r')
            
            time.sleep(1)

            time_sec -= 1

        return "stop"

    def random_choice(self):
        choices = [self.attack(), self.hide(), self.run(), self.defend()]
        
        return choice(choices)
