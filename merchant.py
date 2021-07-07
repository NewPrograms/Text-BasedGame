from sys import excepthook
import psycopg2
from pull import Pull
from Items import Items
from storage import MerchantStorage
class Merchant:

	def __init__(self,username, password):
		self.pull = Pull(username, password)
		self.items = Items(username, password)
		self.merchant_storage = MerchantStorage(username, password)
	

	def menu(self):
		ask = input("Do you want to buy items?(y/n)")

		if ask.lower() == 'y':
			self.merchant_storage.show_items()
			self.items.more_info()
			self.buy_item()
			return True
		else: 
			making_sure = input("Are you sure if so you may go...(y/n): ")
			if making_sure.lower() == 'y':
				return True
		
			else:
				self.menu()

	def buy_item(self):
		try:
			self.pull.pull_table("SELECT transaction({}, '{}')".format(
								 int(input("How many? ")), input("What item do you want to buy? ")
 								))
			return True

		except psycopg2.errors.RaiseException:
			print("Sold out!!!!!!!!!!!!")
			self.menu()
		



