# Import player and get_values
import sys
from numpy.random import choice, random
from calc_poss import Calculate
class Player:

	def __init__(self, values):
		# Define player_stats
		self.health = values[0]
		self.stamina = values[1]
		self.damage = values[2]
		self.gold = values[3]
		self.mana = values[4]





	def player_stats(self):
		print(
			"Health:{}\nStamina:{}\nDamage:{}\nGold:{}\nMana:{}\n"
			.format(
				self.health, self.stamina, self.damage
				, self.gold, self.mana
				)
			)


				

	
class PlayerActions(Player):
	def __init__(self, values):
			super().__init__(values)
			self.calculate_poss = Calculate()
	def run(self):
		# Get the value from calc_success
		# and calculate it to get the weights of choices
		return choice(
				['Successful', 'You got hit!'], 
				p=[
					abs(self.calculate_poss.calc_success(self.health, self.stamina)),
				 	abs(self.calculate_poss.calc_fail(self.health, self.stamina))]
				)

	def hide(self):
		   return choice(
						['Successful', 'The creature saw you!', 'The creature saw you and pounced at you!'], 
						p=[0.2, 0.5, 0.3]
						)

	def attack(self):
		print(self.calculate_poss.get_possibilities(5, self.damage))
		# This is to get the damage and possibilities for damage.
		return choice(
					self.calculate_poss.get_possibilities(5, self.damage),
					p=self.calculate_poss.get_final_val() # WTF WHAT DOES THIS SHIT MEAN!
					)


	def defend(self):
        # This is for the chances of defending an attack
		total =  self.calculate_poss.calc_success() +  0.1 
		return choice([True, False], p=[total, abs(1-total)])

from pull import Pull
class PlayerEffects(Player):

	def __init__(self, values, username, password):
		super().__init__(values)
		self.username = username
		self.password = password
		self.pull = Pull(username, password)

# All of the values below will be put in player_actions	
	def got_hit(self, res):
		if res == 'Miss':
			print("It missed!")

		else:
			print("You got hit! -{} health points".format(res))
			self.pull.update_values(
				"stats SET health = {} - {}".format(
				self.health, res) 
				)

	def loses_stamina(self, stamina_lost):
		self.pull.update_values(
			"stats SET stamina = {} - {}".format(self.stamina, stamina_lost)
		 )
	
	def is_dead(self, res):
		if res == 'Miss':
			print("Whew! Still alive!")
		else:
			if self.health - int(res) <= 0:
				print("Player is dead!")
				self.pull.restart()
				sys.exit()

	def is_tired(self):
		if self.stamina <= 0:
			print("Player is tired! and the monster has killed him!")
			self.pull.restart()
			sys.exit()

