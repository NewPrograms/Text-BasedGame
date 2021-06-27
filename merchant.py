from get_values import Get_Values
from create import Pull, Create
from get_values import Get_Values
class Merchant:

	def __init__(self,username, password):
		self.create = Create(username, password)
		self.pull = Pull(username, password)
		self.get = Get_Values(username, password)
		self.items = []
	def get_storage(self):
		return [list(val) for val in self.pull.pull_table("SELECT * FROM merchant_storage;")]

	def item_info(self):
		return [list(val) for val in self.pull.pull_table("SELECT * FROM items;")]

	def show_items(self):
		print("Hey kid these are the items:")
		for i in range(0, len(self.get_storage())):
			print(
				"\nMerchant_name: {}\nItem: {}\nQuantity: {}" 
				.format(
					self.get_storage()[i][0], 
					self.get_storage()[i][1],
					self.get_storage()[i][2]
					)
				)
		self.more_info()
	
	def more_info(self):
		ask  = input("More info?(y/n): ")

		if ask.lower() == 'y':
			for i in range(0, len(self.item_info())):
				print(
					"\nItem_name: {}\nDamage: {}\nDurability: {}\n" 
					.format(
						self.item_info()[i][0], 
						self.item_info()[i][1],
						self.item_info()[i][2],
					) +
					"Selling Price: {}\nPurchasing Price: {}" 
					.format(
						self.item_info()[i][3],
						self.item_info()[i][4]
						)
					)
				if	self.item_info()[i][0] == 'normal_sword':
					print(
						"This is a normal sword that is poorly manufactured" +
						"In order to ensure efficiency."
						)	
				
				elif self.item_info()[i][0] == 'shield':
					print(
						"This is a shield which you can use to defend various attacks from your enemy"
					)

				else:
					print("This is a dagger which you can use to quickly stab opponents.")

		elif ask.lower() == 'n':
			pass

		else: 
			print("You typed the wrong letter!")

	def buy_items(self):
		ask = input("Do you want to buy items?(y/n)")

		if ask.lower() == 'y':
			self.show_items()
			self.item, self.purchase_price = self.choose_what_to_buy()
			self. res = self.calculate_howmuch(self.purchase_price, 
											  self.how_many() )
			question = input("Are you sure?(y/n)")
			if question.lower() == 'y':
				if self.decrease_money(self.res) == True:
					self.give_items(self.item, self.purchase_price)
				else:
					print("Try again!")
					self.buy_items()	
			else:
				pass
		else: 
			pass

	def choose_what_to_buy(self):
		self.to_buy  = input("Choose what you want to buy(Type letter): ")

		if self.to_buy.lower().strip("_") == 'normal sword':
			return self.item_info()[0][0].strip('_'), self.item_info()[0][4]
		
		elif self.to_buy.lower() == 'shield':
			return self.item_info()[1][0], self.item_info[1][4]
		
		elif self.to_buy.lower() == 'dagger':
			return self.item_info()[2][0], self.item_info[2][4]
		
		else:
			return "Error! There is a mistake in what you typed"

	def decrease_money(self, gold_used):
		if self.get.get_gold() - gold_used < 0:
			print("Money is not enough!")
			return False
		
		else:
			self.pull.update_values(
				"player SET gold = {} - {} "
				.format(self.get.get_gold(), gold_used)
				)
			return True

	def how_many(self):
		return int(input("How many do you want to buy?"))
	
		

	def calculate_howmuch(self, purchasing_price, quantity):
		
		print("The price will be {} gold".format(purchasing_price * quantity))
		return purchasing_price * quantity

	def give_items(self, item_ordered, quantity):
		
			self.create.input_val({
					'storage': [
					"item_name,quantity, damage, durability, selling_price",
					" SELECT item_name, {}, damage, durability, selling_price".format(quantity) +
					" FROM items WHERE item_name = '{}'".format(item_ordered)
					]
			}   
			)
