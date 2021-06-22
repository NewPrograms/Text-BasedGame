from get_values import Get_Values
from operator import itemgetter
from create import Pull

class Calculate:

    def __init__(self, username, password):
        self.pull = Pull(username, password)
        self.get = Get_Values(username, password)
        self.total = []
        self.hitting_chance = []

    def calc_success(self):
        # Pull values from the player table and calculate the
        return (self.get.get_health()/100 + self.get.get_stamina()/100)/3

    def calc_fail(self):
        return abs(1 - self.calc_success())

    def calc_poss_damage(self, damage):
        self.possible_damage = []
        if len(self.possible_damage) == 4:
            self.possible_damage.append(damage)
            self.possible_damage.sort()

        else:
            self.possible_damage.append(damage + self.calc_poss_damage(damage + 1))
            
        print(self.possible_damage)
        return self.possible_damage
    
    def hitting_chances(self, n, val):
        if n <= 1:
            return val
        else:
            self.ans = val/5 + self.division(n-1, val)
            self.hitting_chance.append(self.ans)
        
        return self.hitting_chance
    def undeadmon_att_succ(self, monster):
        # This is for zombie and skeleton who are undead!
        if len(self.total) >= 6:
            for i in range(0, len(self.total)-1):
                self.total.remove(self.total[i])
                print(self.total)
        else:
            self.ans = (
                        (
                        self.get.get_mon_stamina(monster)/100
                         + self.get.get_mon_speed(monster)/100
                         + self.get.get_mon_health(monster)/100)/7
                         )
            self.total.append(self.ans)
            self.division(5, self.ans)
            self.get_final_val()
            print(self.total)
            return self.total
    
    def division(self, n, val):

        if n <= 1:
            return val
        else:
            self.ans = val/5 + self.division(n-1, val)
            self.total.append(self.ans)
            return self.ans

    def get_final_val(self):
        self.total.append(1-sum(self.total))
    

    def mon_calc_dodge(self):
        return (self.get.get_mon_speed/100 + self.get.get_mon_stamina/100)/3