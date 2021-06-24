import time
import sys
from create import Pull
from player import Player
from monster import Monster
from numpy.random import choice
from calc_poss import Calculate
from get_values import Get_Values
class Combat:

    def __init__(self, username, password, monster):
        self.pull = Pull(username, password)
        self.player = Player(username, password) 
        self.get = Get_Values(username, password)
        self.monster = Monster(monster, username, password)
        self.calculate_poss = Calculate(username, password)
        
        self.monster_name = monster
    
    def options(self):

        print(
            "[1] Attack!\n",
            "[2] Run!\n",
            "[3] Defend!\n",
            "[4] Hide!\n",
            "[5] Check Stats\n"
                )
        return self.results()

    def results(self):

        chosen = input("Choose: ")


        if chosen == "1":
            if self.get.get_mon_stamina(self.monster_name) <= 10:
                print("The monster is tired!")
                self.monster.monster_damaged(self.attack())
                return True if self.monster.is_dead() else False


            else:
                if self.monster.dodge(self.calculate_poss.mon_calc_dodge(self.monster_name)) == 'Miss':
                    print("The monster dodged successfully and you missed!")
                    if self.monster.counter_attack(
                        self.calculate_poss.mon_counterattack_chance(self.monster_name)
                        ) == True:
                       self.player.got_hit(
                                    self.monster.attack(
                                        self.calculate_poss.undeadmon_att_succ(self.monster_name)
                                        )
                       )
                       self.player.loses_stamina()
                       self.monster.loses_stamina()
                       return False
                        
                    else:
                        self.player.loses_stamina()
                        self.monster.loses_stamina()
                        return False
                else:
                    print("It hit!")
                    self.monster.monster_damaged(self.attack())
                    self.player.loses_stamina()
                    self.monster.loses_stamina()
                    return True if self.monster.is_dead() else False

            
        elif chosen == "2":

            if self.run() == "Successful":
                print(" You have ran away!")
                self.player.loses_stamina()
                self.monster.loses_stamina()
                return True

            else:
                    self.player.got_hit(
                                        self.monster.attack(
                                        self.calculate_poss.undeadmon_att_succ(self.monster_name)
                                        ))
                    self.players.loses_stamina()
                    self.monster.loses_stamina()
                    return False
                    
        elif chosen == "3":

            pass

        elif chosen == "4":
            self.result = self.hide()
            
            if self.result == 'Successful':
                self.player.loses_stamina()
                print("You hid succesfully!")
                return True
            
            elif self.result == 'The creature saw you!':
                print("The creature saw you and is now preparing for battle")
                return False
            
            else:
                print("the monster saw you and has now hit you!.")
                self.player.got_hit(self.monster.attack(self.calculate_poss.undeadmon_att_succ(self.monster_name))) 
                self.monster.loses_stamina()
                return False
        
        elif chosen == "5":
            self.player.player_stats()

        
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
                    self.calculate_poss.get_possibilities(),
                    p=self.calculate_poss.get_final_val()
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


                
