from create import Pull
class Get_Values:
	def __init__(self,username, password):
		self.pull = Pull(username, password)
	def get_health(self):
	    for val in self.pull.pull_val("SELECT health FROM player"):
                        return val
    
	def get_stamina(self):
	        for val in self.pull.pull_val("SELECT stamina FROM player"):
	            return val
	
	def get_damage(self):
			for val in self.pull.pull_val("SELECT damage FROM player"):
				return val

	def get_gold(self):
			for val in self.pull.pull_val("SELECT gold FROM player"):
				return val
				
	def get_mana(self):
			for val in self.pull.pull_val("SELECT mana FROM player"):
				return val

	def get_mon_stamina(self, monster_name):
	    for val in self.pull.pull_val("SELECT stamina FROM monsters " + 
                                    "WHERE monster_name = '{}'".format(monster_name)):
	        return val

	def get_mon_speed(self, monster_name):
		for val in self.pull.pull_val("select speed FROM monsters " + 
										"WHERE monster_name = '{}'".format(monster_name)):
				return val
	def get_mon_health(self, monster_name):
		for val in self.pull.pull_val("SELECT health FROM monsters " +
										"WHERE monster_name = '{}'".format(monster_name)):
				print(val)
				return val
		