from get_values import Get_Values
from operator import itemgetter
from create import Pull

class Calculate:

    def __init__(self, username, password):
        self.pull = Pull(username, password)
        self.get = Get_Values(username, password)
        self.total = []
        self.possible_damage = []
        self.hitting_chances = []

    def calc_success(self):
        # Pull values from the player table and calculate the
        return (self.get.get_health()/100 + self.get.get_stamina()/100)/3

    def calc_fail(self):
        return abs(1 - self.calc_success())

    def calc_poss_damage(self, n, damage):
        if n == damage:
            self.possible_damage.append(damage)
            return damage
        else:
            self.res =self.get.get_damage() - 4 + self.calc_poss_damage(n-1, damage)
            self.possible_damage.append(self.res)
            return self.res  

    def get_possibilities(self):
        self.calc_poss_damage(self.get.get_damage(), self.get.get_damage()-4)
        return self.possible_damage

    def calc_hitting_chance(self, n, val):
        if n <= 1:
            return val
        else:
            self.ans = val/5 + self.calc_hitting_chance(n-1, val)
            self.hitting_chances.append(self.ans)
            return self.ans

    def get_final_chance(self):
        if len(self.hitting_chances) >= 6:
            for i in range(0, len(self.hitting_chances)-1):
                self.hitting_chances.remove(self.hitting_chances[i])
        else:
            self.calc_hitting_chance(5, self.calc_success())
            self.hitting_chances.append(1-sum(self.hitting_chances))
            return self.hitting_chances.sort(reverse=True)
    def undeadmon_att_succ(self, monster):
        # This is for zombie and skeleton who are undead!
        if len(self.total) >= 6:
            for i in range(0, len(self.total)-1):
                self.total.remove(self.total[i])
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

            return self.total
    
    def division(self, n, val):

        if n <= 1:
            return val
        else:
            self.ans = val/5 + self.division(n-1, val)
            self.total.append(self.ans)
            return self.ans

    def get_final_val(self):
        if sum(self.total) >= 1:
            self.total.append(1-sum(self.total))
        
        else: 
            self.total = [abs(x - 0.1) for x in self.total]
            self.total.append(1-sum(self.total))
        
    def calculate_stamina_consumed(self):
        return ((100/self.get.get_stamina())*0.9)+3


    def mon_calc_dodge(self, monster):
        return (self.get.get_mon_speed(monster)/100 + self.get.get_mon_stamina(monster)/100)/3

    def mon_counterattack_chance(self, monster):
        return (self.get.get_mon_speed(monster)/100 + self.get.get_mon_stamina(monster)/100)/7