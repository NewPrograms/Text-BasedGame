import time
import sys
from operator import itemgetter
from create import Pull
from numpy.random import choice
class Combat:

    def __init__(self):
        self.pull = Pull()
        
    
    def options(self):

        print(
            "[1] Attack!\n",
            "[2] Run!\n",
            "[3] Defend!\n",
            "[4] Hide!\n"
                )

    def results(self):

        chosen = input("Choose: ")

        self.count = self.countdown(5)

        if chosen == "1":

            pass

        elif chosen == "2":

            self.result = self.run()

            return self.result
        elif chosen == "3":

            pass

        elif chosen == "4":

            self.result = self.hide()
            return self.hide
        
        else:
            print("Invalid Choice!")
            sys.exit()
        
        if self.count == 'stop':
            self.random_choice()
        
        else:
            time.sleep(5-self.count)


    def run(self):
        
        # Get the value from calc_success
        # and calculate it to get the weights of choices

        self.succ_chance = self.calc_success

        choices = ['Successful', 'You got hit!']

        return choice(choices, p=[self.succ_chance, abs(1-self.succ_chance)])

    def hide(self):
           choices = ['Successful', 'The creature saw you!', 'The creature saw you and pounced at you!']
           return choice(choices,  p=[0.2, 0.5, 0.3])

    def attack(self):
        pass
    def calc_success(self):
        # Pull values from the player table and calculate them

        self.statement =  'SELECT health, stamina FROM player'

        # if have time optimize these 2 lines of code.
        self.health, self.stamina = itemgetter(0,1)(self.pull.pull_val(self.statement))

        return (self.health/100 + self.stamina/100)/3


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
