from pull import Pull
class PlayerStorage():
	
	# This is for the player's storage
	def __init__(self, username, password):
		self.pull = Pull(username, password)
	# Showing the items in the class
	def show_items(self):
		print("Player Storage: ")
		for i in range(0, len(self.get_items())):
			print(
				"""
				\nItem: {}\nQuantity: {}\nDurability: {}\nSelling Price: {}\nDamage: {}
				""" 
				.format(
					self.get_items()[i][0], 
					self.get_items()[i][1],
					self.get_items()[i][2],
					self.get_items()[i][3], 
					self.get_items()[i][4], 
					)
				)


	def get_items(self):
		return [list(val) for val in self.pull.pull_table("SELECT * FROM storage")]



class MerchantStorage():

	# This class is for the storage of the merchants
	def __init__(self, username, password):
		self.pull = Pull(username, password)

	# define merchant_storage_items
	# Useful for showing the available items and it's quantity
	def show_items(self):
		print("Hey kid these are the items:")
		for i in range(0, len(self.get_items())):
			print(
				"\nMerchant_name: {}\nItem: {}\nQuantity: {}" 
				.format(
					self.get_items()[i][0], 
					self.get_items()[i][1],
					self.get_items()[i][2]
					)
				)

	def get_items(self):
		return [list(val) for val in self.pull.pull_table("SELECT * FROM merchant_storage;")]

