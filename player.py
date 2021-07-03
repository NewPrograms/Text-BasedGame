from create import Pull
from get_values import Get_Values
class Player:

	def __init__(self, username, password):
		self.get = Get_Values(username, password)
		self.pull = Pull(username, password)
		

	
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