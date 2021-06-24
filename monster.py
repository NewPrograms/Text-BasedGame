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
			

	def loses_stamina(self, to_lose):
			self.pull.update_values(
			"monsters SET stamina = {} - {} WHERE monster_name = '{}'"
			.format(self.get.get_mon_stamina(self.monster), to_lose, self.monster)
			)

	def dodge(self, poss):
		return choice(['Hit', 'Miss'], p=[poss, 1-poss] )

	def monster_damaged(self, damage):
		print("The monster has been damaged {}".format(damage))
		self.pull.update_values(
			"monsters SET health = {} - {} WHERE monster_name = '{}'"
			.format(self.get.get_mon_health(self.monster), damage, self.monster)
		)

	def counter_attack(self, poss):
		print("The monster will now counter attack!")
		return choice([True, False], p=[1-poss, poss]) 

	def is_dead(self):
		if self.get.get_mon_health(self.monster) <= 0:
			print("The monster has died!")
			return True

		else:
			print(
				"The health of the monster is at {}"
				.format(self.get.get_mon_health(self.monster))
				)
			return False
