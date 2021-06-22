import time
import sys
from monster import Monster
from get_values import Get_Values
from create import Create, Pull
from numpy.random import choice
from calc_poss import Calculate
class Combat:

    def __init__(self, username, password, monster):
        self.monster = Monster(monster, username, password)
        self.calculate_poss = Calculate(username, password)
        self.get = Get_Values(username, password)
        self.pull = Pull(username, password) 
        
        self.monster_name = monster
    
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


            if self.get.get_mon_stamina(self.monster) <= 10:
                print("The monster is tired!")

            else:
                if self.mon.dodge(self.calculate_poss.mon_calc_dodg()) == 'Miss':
                    self.player_losestamina()
                    self.monster.loses_stamina()
                    return False
                else:
                    self.attack()
                

            
        elif chosen == "2":

            if self.run() == "Successful":
                print(" You have ran away!")
                self.player_losestamina()
                self.monster.loses_stamina()
                return True

            else:
                self.res = self.monster.attack(self.calculate_poss.undeadmon_att_succ(self.monster_name))
                if self.res == 'Miss':
                    print("It missed!")
                    self.player_losestamina()
                    self.monster.loses_stamina()
                    return False
                else:
                    self.player_hit(self.res)
                    self.monster.loses_stamina()
                    return False
                    
        elif chosen == "3":

            pass

        elif chosen == "4":
            print("Nice Nice")
            self.result = self.hide()
            
            if self.result == 'Successful':
                self.player_losestamina()
                print("You hid succesfully!")
                return True
            
            elif self.result == 'The creature saw you!':
                print("The creature saw you and is now preparing for battle")
                return False
            
            else:
                print("the monster saw you and has now hit you!.")
                self.player_hit(self.monster.attack(self.calculate_poss.undeadmon_att_succ(self.monster_name))) 
                self.monster.loses_stamina()
                return False

        
        else:
            print("Invalid Choice!")
            sys.exit()
        


    def run(self):
        
        # Get the value from calc_success
        # and calculate it to get the weights of choices
        print(self.calculate_poss.calc_success(), abs(self.calculate_poss.calc_fail()))
        return choice(
                ['Successful', 'You got hit!'], 
                p=[abs(self.calculate_poss.calc_success()), abs(self.calculate_poss.calc_fail())]
                )

    def hide(self):
           return choice(
                        ['Successful', 'The creature saw you!', 'The creature saw you and pounced at you!'], 
                        p=[0.2, 0.5, 0.3]
                        )

    def attack(self):
        return choice(
                    self.calculate_poss.calc_poss_damage(), 
                    p=self.calculate_poss.hitting_chances(5, self.calculate_poss.calc_success)
        )

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


    def player_hit(self, res):
        print("You got hit! -{} health points".format(res))
        self.pull.update_values(
            "player SET health = {} - {}".format(
            self.get.get_health(),
            res) 
            )

    def player_losestamina(self):
        self.pull.update_values(
            "player SET stamina = {} - 5".format(self.get.get_stamina())
         )

                                            