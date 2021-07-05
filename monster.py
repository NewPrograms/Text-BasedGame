from numpy.random import choice
from get_values import Get_Values
class Monster:

	def __init__(self, monster,health, stamina, damage, mana, speed, gold_drop):
		self.monster = monster
		self.health = health
		self.stamina = stamina
		self.damage =  damage
		self.mana = mana
		self.speed = speed
		self.gold_drop = gold_drop

	def print_monster_stats(self):
		print(
			"Monster:{}\nHealth:{}\nStamina:{}\nDamage\nMana:{}\n"
			.format(
				self.health, self.stamina, self.damage
				,self.mana
				)
			)
	def is_dead(self):
		if self.health <= 0:
			print("The monster has died!")
			return True

		else:
			print(
				"The health of the monster is at {}"
				.format(self.get.get_mon_health(self.monster))
				)
			return False

	def loses_stamina(self, to_lose):
			self.pull.update_values(
			"monsters SET stamina = {} - {} WHERE monster_name = '{}'"
			.format(self.health, to_lose, self.monster))

class MonsterActions(Monster):
	def __init__(self, monster, health, damage, mana, speed, gold_drop):
		super.__init__(monster, health, damage, mana, speed, gold_drop)

	def attack(self, poss):
		print(self.monster)
		if self.monster == 'zombies':
			return choice(['Miss',16, 17, 18, 19, 20], p=poss)
			
		
		if self.monster == 'skeletons':
			return choice(['Miss', 6, 7, 8, 9, 10], p=poss)
			


	def dodge(self, poss):
		return choice(['Hit', 'Miss'], p=[poss, 1-poss] )

	def monster_damaged(self, damage):
		print("The monster has been damaged {}".format(damage))
		self.pull.update_values(
			"monsters SET health = {} - {} WHERE monster_name = '{}'"
			.format(self.health, damage, self.monster)
		)

	def counter_attack(self, poss):
		print("The monster will now counter attack!")
		return choice([True, False], p=[1-poss, poss]) 

