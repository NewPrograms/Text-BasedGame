from create import Pull

class Merchant:

	def __init__(self,username, password):
		self.pull = Pull(username, password)
		self.items = []
	def get_items(self):
		for val in self.pull.pull_val("SELECT * from merchant_storage"):
			self.i
	def show_items(self):
		pass

	def give_items(self):
		pass
