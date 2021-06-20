
from operator import itemgetter
from create import Pull

class Calculate:

    def __init__(self, username, password):
        self.pull = Pull(username, password)
        self.total = []

    def calc_success(self):
        # Pull values from the player table and calculate them

        self.statement =  'SELECT health, stamina FROM player'

        # if have time optimize these 2 lines of code.
        self.health, self.stamina = itemgetter(0,1)(self.pull.pull_val(self.statement))
        return (self.health/100 + self.stamina/100)/3

    def calc_fail(self):
        return abs(1 - self.calc_success())


    def undeadmon_att_succ(self):
        # This is for zombie and skeleton who are undead!
        
        self.statement = "SELECT health, speed FROM monsters WHERE monster_name = 'zombies'"   
        self.health, self.speed = itemgetter(0,1)(self.pull.pull_val(self.statement))
        self.ans = (self.health/100+self.speed/100)/5
        self.total.append((self.health/100+self.speed/100)/5)
        self.division(5, self.ans)
        return self.get_final_val()

    def division(self, n, val):

        if n <= 1:
            return val
        else:
            self.ans = val/5 + self.division(n-1, val)
            self.total.append(self.ans)
            return self.ans

    def get_final_val(self):
        self.total.append(1-sum(self.total))
        return self.total.sort(reverse=True)