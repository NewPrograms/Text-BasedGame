from create import Pull
from numpy.random import choice
from get_values import Get_Values
class Monster:

	def __init__(self, monster, username, password):
		self.monster = monster
		self.pull = Pull(username, password)
		self.get = Get_Values(username, password)	

	def attack(self, poss):
		print(self.monster)
		if self.monster == 'zombies':
			return choice(['Miss',16, 17, 18, 19, 20], p=poss)
			
		
		if self.monster == 'skeletons':
			return choice(['Miss', 6, 7, 8, 9, 10], p=poss)
			

	def loses_stamina(self):
			self.pull.update_values(
            "monsters SET stamina = {} - 5 WHERE monster_name = '{}'"
            .format(self.get.get_mon_stamina(self.monster), self.monster)
            )

	def mon_dodge(self, poss):
		return choice(['Hit, Miss'], p=[poss, 1-poss] )