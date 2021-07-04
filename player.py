from create import Pull
from get_values import Get_Values
class Player:

	def __init__(self, username, password):
		# Define player_stats
		self.name = username
		self.health = 0
		self.damage = 0
		self.gold = 0 
		self.mana = 0
		self.stamina = 0
		self.get = Get_Values(username, password)
		self.pull = Pull(username, password)
		

# All of the values below will be put in player_actions	
	def got_hit(self, res):
		if res == 'Miss':
			print("It missed!")

		else:
			print("You got hit! -{} health points".format(res))
			self.pull.update_values(
				"player SET health = {} - {}".format(
				self.get.get_health(), res) 
				)

	def loses_stamina(self):
		self.pull.update_values(
			"player SET stamina = {} - 5".format(self.get.get_stamina())
		 )

	def player_stats(self):
		print(
			"Health:{}\nStamina:{}\nDamage:{}\nGold:{}\nMana:{}\n"
			.format(
				self.get.get_health, self.get.get_stamina(), self.get.get_damage()
				, self.get.get_gold(), self.get.get_mana()
				)
			)