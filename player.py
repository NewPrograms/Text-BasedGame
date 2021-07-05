# Import player and get_values
from get_values import Get_Values
from numpy.random import choice, random

class Player:

	def __init__(self, username,health, damage, gold, mana, stamina):
		# Define player_stats
		self.name = username
		self.health = health
		self.damage = damage
		self.gold = gold
		self.mana = mana
		self.stamina = stamina



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
				self.health, self.stamina, self.damage
				, self.gold, self.mana
				)
			)
class PlayerActions(Player):
    def __init__(health, stamina, damage, mana, gold):
            super().__init__(health, stamina, damage, mana, gold)

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