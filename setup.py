# This class sets up the game.
import psycopg2
from psycopg2 import extensions
class Setup():
	
	# Make setup inherit Authenticate
	def __init__(self, username, password):
		self.setting_up()
		self.acc_u_name = username
		self.acc_p_word = password
	
	def setting_up(self, username, password):
		# This packages all functions into one function

		self.create_db()
		self.create_table()
		self.create_trigger()
		self.create_function()


	def create_db(self):
		# Creates database
			auto_commit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
			self.conn = psycopg2.connect(dbname='postgres', user='postgres', 
										password=f'12', host='127.0.0.1' )
			self.conn.set_isolation_level(auto_commit)
			self.cur = self.conn.cursor()
			self.cur.execute(f'ALTER ROLE {self.acc_u_name} CREATEDB')
			self.cur.execute(f'CREATE DATABASE {self.acc_u_name}_game')
			self.cur.execute('ALTER DATABASE {}_game OWNER TO {}'.format(self.acc_u_name, self.acc_u_name))
			self.cur.close()
			self.conn.close()

	def create_table(self, statements):
		# Creates table
		self.conn.commit()

		self.cur.close()

		self.conn.close()

		print("Database Made!")

# Questionable existance we'll see later.
	def input_val(self, statements):
		# Inputs all values
		self.conn = psycopg2.connect(dbname=f'{self.acc_u_name}_game', user=f'{self.acc_u_name}', 
									 password=f'{self.acc_p_word}', host='127.0.0.1' )

		self.cur = self.conn.cursor()
		# This is where various values are added on to the code.
	  
		for key, val in statements.items():
		   for num in range(0,len(val)-1):
			   if len(val) > 1:
				   self.cur.execute("INSERT INTO {}({}) {}".format(key, val[0], val[num+1]))

			   else:
				   self.cur.execute("INSERT INTO {}({}) {}".format(key, val[0], val[1]))

		self.conn.commit()
		self.cur.close()
		self.conn.close()

	def create_trigger(self):
		 pass

	def create_function(self, statement):
		# Creatse the function
		self.conn = psycopg2.connect(dbname=f'{self.acc_u_name}_game', user=f'{self.acc_u_name}', 
									 password=f'{self.acc_p_word}', host='127.0.0.1' )
		self.cur = self.conn.cursor()
		for key, val in statement.items():
			self.cur.execute(
						   "CREATE OR REPLACE FUNCTION {} {}".format(key, val)
						   )
			self.conn.commit()
						   
		self.cur.close()
		self.conn.close()
