from numpy.random import choice
from calc_poss import Calculate
class Monster:

	def __init__(self):
		self.calculate_poss = Calculate

	def attack(self, poss):
		possibilites = ['miss',6, 7, 8, 9, 10]
		return choice(possibilites, p=poss)

