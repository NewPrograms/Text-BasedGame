import psycopg2
from create import Create, Pull
class User():
	# This is the user class
	def __init__(self, username = "postgres", password = "1"):
		self.username = username
		self.password = password

		self.active = True
# Remove because the User will be inherited by Create, Pull, Del
# As part of the priveleges.


# Remove and put to items, merchant_storage, player, monster, and merchant.
		self.to_input = {
			'player':[
				'player_name, health, stamina, damage, gold, mana', 
				'VALUES ({}, {}, {}, {}, {}, {})'.format(f"'{self.username}'", 50, 60, 70, 80, 0)
			],
			'monsters': [
				'monster_name, health, stamina, speed, damage, gold_drop, mana',
				'VALUES({}, {}, {}, {}, {}, {}, {})'.format("'zombies'", 50, 40, 10, 20, 30, 0),
				'VALUES({}, {}, {}, {}, {}, {}, {})'.format("'skeletons'", 20, 70, 40, 5, 50, 0),
				'VALUES({}, {}, {}, {}, {}, {}, {})'.format("'wolves'", 55, 30, 50, 25, 80, 0),
				],
			'merchant': [
					'merchant_id, merchant_name, merchant_location',
					'VALUES({}, {}, {})'.format("'MER001'", "'Ben'", "'Temple'")
				],
			'items': [
				'item_name, damage, durability, selling_price, purchasing_price',
				'VALUES({}, {}, {}, {}, {})'.format("'normal_sword'", 20, 50, 10, 30),   
				'VALUES({}, {}, {}, {}, {})'.format("'shield'", 0, 100, 20, 40),   
				'VALUES({}, {}, {}, {}, {})'.format("'dagger'", 10, 60, 5, 20)   
				],
			'merchant_storage': [
				'merchant_id, item_name, quantity',
				'VALUES({}, {}, {})'.format("'MER001'", "'normal_sword'", 6),
				'VALUES({}, {}, {})'.format("'MER001'", "'shield'", 3),
				'VALUES({}, {}, {})'.format("'MER001'", "'dagger'",  10)                     
			],
			}

# Also remove this.
 
