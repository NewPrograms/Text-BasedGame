from create import Pull
class Get_Values:
	def __init__(self,username, password):
		self.pull = Pull(username, password)
	def get_playerstats(self):
		return [val for val in self.pull.pull_table("SELECT * FROM player;")]

	def get_monster_stats(self, monster):
		return [val for val in self.pull.pull_table(
			"SELECT * FROM monsters WHERE monster_name = '{}';".format(monster)
		)]
		
	def get_storage(self):
		return [list(val) for val in self.pull.pull_table("SELECT * FROM merchant_storage;")]
