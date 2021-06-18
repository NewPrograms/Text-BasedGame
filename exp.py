to_input = {
                'player':[
                        'player_name, health, stamina, damage, gold, mana', 
                        'VALUES ({}, {}, {}, {}, {}, {})'.format(self.acc_u_name, 50, 60, 70, 80, 0)
                ],
                'monsters`': [
                          'monster_name, health, stamina, speed, damage, gold_drop, mana',
                          'VALUES({}, {}, {}, {}, {}, {}, {})'.format('zombies', 50, 40, 10, 20, 30, 0),
                          'VALUES({}, {}, {}, {}, {}, {}, {})'.format('skeletons', 20, 70, 40, 10, 50, 0),
                          'VALUES({}, {}, {}, {}, {}, {}, {})'.format('wolves', 55, 80, 50, 30, 80, 0),
                          ],
                'merchants': [
                            'merchant_name, merchant_name, merchant_location',
                            'VALUES({}, {}, {})'.format('MER001', 'Ben', 'Temple')
                        ],
                'items': [
                        'item_name, damage, durability, sell_price, purchasing_price',
                        'VALUES({}, {}, {}, {}, {})'.format('normal_sword', 20, 50, 10, 30),   
                        'VALUES({}, {}, {}, {}, {})'.format('shield', 0, 100, 20, 40),   
                        'VALUES({}, {}, {}, {}, {})'.format('dagger', 10, 60, 5, 20)   
                       ],
                'merchant_storage': [
                        'merchant_id','item_name, quantity'
                        'VALUES({}, {}, {})'.format('MER001', 'normal_sword', 6),
                        'VALUES({}, {}, {})'.format('MER001', 'shield', 3),
                        'VALUES({}, {}, {})'.format('MER001', 'dagger',  10)                     
                ],
            }
for key, val in statements.items():
    if len(val) > 1:
       

        else:
            for it_val in val:
            print(it_val)