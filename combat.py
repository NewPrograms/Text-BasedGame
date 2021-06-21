import time
import sys
from monster import Monster
from create import Create, Pull
from numpy.random import choice
from calc_poss import Calculate
class Combat:

    def __init__(self, username, password, monster):
        self.monster_name = monster
    
        self.monster = Monster(monster)
        self.pull = Pull(username, password) 
        self.calculate_poss = Calculate(username, password)        
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
                self.pull.update_values(
                    "player SET stamina = {} - 5".format(self.get_stamina())
                    )
                self.pull.update_values(
                    "monsters SET stamina = {} -5 WHERE monster_name = '{}'"
                    .format(self.get_mon_stamina(), self.monster_name)
                    )
                return True

            else:
                self.res = self.monster.attack(self.calculate_poss.undeadmon_att_succ(self.monster_name))
                print(self.res)
                if self.res == 'Miss':
                    print("It missed!")
                    self.pull.update_values(
                        "player SET stamina = {} - 5" 
                        .format(self.get_stamina())
                    )
                    self.pull.update_values(" monsters.stamina = {} - 5, WHERE monsters.monster_name = {}"
                                            .format(self.get_mon_stamina(), self.monster_name))
                else:
                    print("You got hit! -{} health points".format(self.res))
                    self.pull.update_values(
                            "player SET health = {} - {}".format(
                            self.get_health(),
                            self.res) 
                            )
                                            
                    self.pull.update_values(
                        "monsters SET stamina = {} - 5 WHERE monster_name = '{}'"
                        .format(self.get_mon_stamina(), self.monster))
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

        return choice(
                ['Successful', 'You got hit!'], 
                p=[self.calculate_poss.calc_success(), self.calculate_poss.calc_fail()]
                )

    def hide(self):
           return choice(
                        ['Successful', 'The creature saw you!', 'The creature saw you and pounced at you!'], 
                        p=[0.2, 0.5, 0.3]
                        )

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
        return choice([self.attack(), self.hide(), self.run(), self.defend()])

    def get_health(self):
        for val in self.pull.pull_val("SELECT health FROM player"):
                        return val
    
    def get_stamina(self):
        for val in self.pull.pull_val("SELECT stamina FROM player"):
            return val

    def get_mon_stamina(self):
        for val in self.pull.pull_val("SELECT stamina FROM monsters " + 
                                    "WHERE monster_name = '{}'".format(self.monster_name)):
            return val