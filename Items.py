# This the items class where items are made deleted etc.

class Items:
	
	def __init__(self, item_name, damage, durability, sell_price, purchasing_price):
		# This is class is for items 
		pass

	
	def item_info(self):
		return [list(val) for val in self.pull.pull_table("SELECT * FROM items;")]


	def losing_durability(self):
		# Call self.pull.updates('UPDATE storage SET durability = {} - {}
		# WHERE item_name = {}'.format(Call item_durability, and Value of durability lost))
		pass