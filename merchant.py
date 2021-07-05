from sys import excepthook
from get_values import Get_Values
from get_values import Get_Values
import psycopg2
class Merchant:

	def __init__(self,username, password):
		self.create = Create(username, password)
		self.pull = Pull(username, password)
		self.get = Get_Values(username, password)
		self.items = []

	def show_items(self):
		print("Hey kid these are the items:")
		for i in range(0, len(self.get.get_storage())):
			print(
				"\nMerchant_name: {}\nItem: {}\nQuantity: {}" 
				.format(
					self.get.get_storage()[i][0], 
					self.get.get_storage()[i][1],
					self.get.get_storage()[i][2]
					)
				)
	
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

	def menu(self):
		ask = input("Do you want to buy items?(y/n)")

		if ask.lower() == 'y':
			self.show_items()
			self.more_info()
			self.buy_item()
			return True
		else: 
			making_sure = input("Are you sure if so you may go...(y/n): ")
			if making_sure.lower() == 'y':
				return True
		
			else:
				self.menu()
	def choose_what_to_buy(self):
		self.to_buy  = input("Choose what you want to buy(Type letter): ")

		if self.to_buy.lower().strip("_") == 'normal sword':
			return self.get.item_info()[0][0].strip('_')
		
		elif self.to_buy.lower() == 'shield':
			return self.get.item_info()[1][0]
		
		elif self.to_buy.lower() == 'dagger':
			return self.get.item_info()[2][0]
		
		else:
			return "Error! There is a mistake in what you typed"

	def buy_item(self):
		try:
			chosen_item =  self.choose_what_to_buy()
			self.pull.pull_table("SELECT transaction({}, '{}')".format(
								 int(input("How many? ")), chosen_item
 								))
			return True

		except psycopg2.errors.RaiseException:
			print("Sold out!!!!!!!!!!!!")
			self.menu()
		



