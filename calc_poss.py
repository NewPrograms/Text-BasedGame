from operator import itemgetter

class Calculate:

    def __init__(self):
        self.total = []
        self.possible_damage = []
        self.hitting_chances = []

    def calc_success(self, health, stamina):
        # Pull values from the player table and calculate the
        # Get the health and stamina of the player
        return (health/100 + stamina/100)/3

    def calc_fail(self):
        return abs(1 - self.calc_success())

    def calc_poss_damage(self, n, damage):
        # Get the damage of the player
        # Using Recursion subtract the stats if the player by 4
        # which is then appended to possible_damage
        if n == damage:
            self.possible_damage.append(damage)
            return damage
        else:
            self.res = damage - 4 + self.calc_poss_damage(n-1, damage)
            self.possible_damage.append(self.res)
            return self.res  

    def get_possibilities(self, damage):
        # This function is to get the damage range
        # This works by adding the original damage in the first argument
        # of calc_poss_damage then putting subratracting damage in the left side to
        # add the range up until it will return the original damage.
        self.calc_poss_damage(damage, damage-4)
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
    def undeadmon_att_succ(self, mon_health, mon_speed, mon_stamina):
        # This is for zombie and skeleton who are undead!
        if len(self.total) >= 6:
            for i in range(0, len(self.total)-1):
                self.total.remove(self.total[i])
        else:
            self.ans = (
                        (mon_health/100 + mon_stamina/100 + mon_speed/100)/7
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
        # If the sum of the self.total < 1
        # the sum of is the appended to total.
        if sum(self.total) >= 1:
            self.total.append(1-sum(self.total))
        
        # If it is greater than the absolute value
        # will then be subtracted by 0.1 
        # Up until  it becomes lesser than 1.
        else: 
            self.total = [abs(x - 0.1) for x in self.total]
            self.total.append(1-sum(self.total))
        
    def calculate_stamina_consumed(self, stamina):
        return (100/stamina*0.9)+3


    def mon_calc_dodge(self, mon_speed, mon_stamina):
        return (mon_speed/100 + mon_stamina/100)/3

    def mon_counterattack_chance(self, mon_stamina, mon_speed):
        return (mon_stamina/100 + mon_speed/100)/7