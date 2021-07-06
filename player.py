# Import player and get_values
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
				p=[abs(self.calculate_poss.calc_success(self.health)), abs(self.calculate_poss.calc_fail())]
				)

	def hide(self):
		   return choice(
						['Successful', 'The creature saw you!', 'The creature saw you and pounced at you!'], 
						p=[0.2, 0.5, 0.3]
						)

	def attack(self):
		# This is to get the damage and possibilities for damage.
		return choice(
					self.calculate_poss.get_possibilities(self.damage),
					p=self.calculate_poss.get_final_val() # WTF WHAT DOES THIS SHIT MEAN!
					)

	# DEFINE DEFEND
	def defend(self):
		# This is a function that allows the player to defend
		if self.is_defended is True:
			print('Defended!')
			
			# Call losing_durability
		# ElSE
			# PRINT('He hit you!')
			# Call functin losing health, stamina, and monster_stamina

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
				"player SET health = {} - {}".format(
				self.health, res) 
				)

	def loses_stamina(self):
		self.pull.update_values(
			"player SET stamina = {} - 5".format(self.stamina())
		 )
	
