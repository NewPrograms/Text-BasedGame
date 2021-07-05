to_create = {
			"player":
				'player_name varchar(50) PRIMARY KEY NOT NULL,'+
				'health int NOT NULL, stamina int NOT NULL,'+ 
				'damage int NOT NULL, gold int NOT NULL, mana int NOT NULL'
			,

			"items":
				'item_name varchar(100) PRIMARY KEY NOT NULL,' +
				'damage int NOT NULL, durability int NOT NULL,' +
				'selling_price int NOT NULL, purchasing_price int NOT NULL'
			,

			"monsters": 
				'monster_name varchar(50) PRIMARY KEY NOT NULL,' +
				'health int NOT NULL, stamina int NOT NULL, damage int NOT NULL, mana int NOT NULL,' +
				'speed int NOT NULL, gold_drop int NOT NULL' 
			,

			"merchant":
				'merchant_id varchar(100) PRIMARY KEY NOT NULL, merchant_name varchar(50) NOT NULL,' +
				'merchant_location varchar(150) NOT NULL'
			,

			"merchant_storage":  
				'merchant_id varchar(50) NOT NULL references merchant(merchant_id),' +
				'item_name varchar(100) NOT NULL references items(item_name), quantity int NOT NULL'
			,

			"storage":
				'item_name varchar(100) NOT NULL references items(item_name), damage int NOT NULL,'+
				'quantity int NOT NULL, durability int NOT NULL, selling_price int NOT NULL '
		}

to_input = {
			'stats':[
				'player_name, health, stamina, damage, gold, mana', 
				'VALUES ({}, {}, {}, {}, {}, {})'.format(50, 60, 70, 80, 0)
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


trigger_functions = {
				"transaction(quant int, name_of_item varchar(100))":
				"RETURNS text AS $$\nDECLARE\ntotal_price int;\nprice_used int;\nplayer_gold int;\n"+
				"dam int;\nquant_of_prod int;\nname varchar(100);\ndur int;\nprice int;\nsell int;"+
				"BEGIN\nSELECT quantity into quant_of_prod FROM merchant_storage; " +
				"SELECT gold into player_gold FROM player;\n"+
				"SELECT * into name, dam, dur, sell, price FROM items WHERE item_name = name_of_item;\n" +
				"total_price := quant * price;\nprice_used := player_gold - total_price;\n "
				"IF quant < 0 THEN\nRAISE EXCEPTION USING MESSAGE = \"NEGATIVE VALUES ARE NOT ALLOWED\";"
				"ELSIF quant_of_prod IS NULL THEN\nRAISE EXCEPTION USING MESSAGE = \"MISPELLED NAME OR DOESN'T EXIST!\";\n"
				"ELSIF price_used <0 THEN\nRETURN 'FAIL LACKS GOLD!';\nELSE\nUPDATE player SET gold = price_used;\n"+
				"UPDATE merchant_storage SET quantity = quant_of_prod - quant WHERE item_name = name_of_item;\n" +
				"INSERT INTO storage(item_name, quantity, damage, durability, selling_price)"+
				"VALUES(name, quant, dam, dur, sell);\nRETURN 'SUCCESSFUL!';\nEND IF;\nEND;\n$$ LANGUAGE \'plpgsql\';",

				"only_one()":
				"RETURNS TRIGGER AS $$\nBEGIN\nIF NEW.QUANTITY > 1 THEN\n"+
				"RAISE EXCEPTION USING MESSAGE = 'ONLY ONE QUANTITY OF WEAPONRY IS ALLOWED!';\n"+
				"END IF;\nRETURN NEW;\nEND;\n$$ LANGUAGE 'plpgsql';\n",

				"removing_item()":
				"RETURNS TRIGGER AS $$\nDECLARE\nprev_damage int;\ni record;\nBEGIN\nSELECT damage into prev_damage FROM player;\n"+
				"UPDATE player SET damage = prev_damage - OLD.damage;\n"
				"RETURN OLD;\nEND;\n$$ LANGUAGE 'plpgsql';\n",

				"get_total_damage()":
				"RETURNS TRIGGER AS $$\nDECLARE \ntotal_damage int;\n"+
				"BEGIN\nSELECT damage into total_damage FROM player;\n"+                                                                                                                                                                                                                                                                                                                                                                                                                                
				"UPDATE player SET damage = total_damage + NEW.DAMAGE;\n"+
				"RETURN NEW;\nEND;\n$$ LANGUAGE 'plpgsql';"
}