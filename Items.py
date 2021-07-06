# This the items class where items are made deleted etc.
from pull import Pull

class Items:
	
	def __init__(self, username, password):
		# This is class is for items 
		self.pull = Pull(username, password)
	# Printing the info of the item
	def item_info(self):
		return [list(val) for val in self.pull.pull_table("SELECT * FROM items;")]

	# effects the item's durability
	def losing_durability(self):
		# Call self.pull.updates('UPDATE storage SET durability = {} - {}
		# WHERE item_name = {}'.format(Call item_durability, and Value of durability lost))
		pass

	def more_info(self):
		ask  = input("More info?(y/n): ")

		if ask.lower() == 'y':
			for i in range(0, len(self.get.item_info())):
				print(
					"\nItem_name: {}\nDamage: {}\nDurability: {}\n" 
					.format(
						self.get.item_info()[i][0], 
						self.get.item_info()[i][1],
						self.get.item_info()[i][2],
					) +
					"Selling Price: {}\nPurchasing Price: {}" 
					.format(
						self.get.item_info()[i][3],
						self.get.item_info()[i][4]
						)
					)
				if	self.get.item_info()[i][0] == 'normal_sword':
					print(
						"This is a normal sword that is poorly manufactured" +
						"In order to ensure efficiency."
						)	
				
				elif self.get.item_info()[i][0] == 'shield':
					print(
						"This is a shield which you can use to defend various attacks from your enemy"
					)

				else:
					print("This is a dagger which you can use to quickly stab opponents.")

		elif ask.lower() == 'n':
			pass

			

		else: 
			print("You typed the wrong letter!")