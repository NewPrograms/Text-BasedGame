from numpy.random import choice
from calc_poss import Calculate
class Monster:

	def __init__(self, monster):
		self.monster = monster
	def attack(self, poss):
		print(self.monster)
		if self.monster == 'zombies':
			choices = ['Miss',16, 17, 18, 19, 20]
			ans = choice(choices, p=poss)
			return ans
		
		if self.monster == 'skeletons':
			choices = ['Miss', 6, 7, 8, 9, 10]
			ans = choice(choices, p=poss)
			return ans