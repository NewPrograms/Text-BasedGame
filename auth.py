import psycopg2
from user import User
from setup import Setup

class Auth(User):
	def __init__(self, username, password):
		super().__init__(username, password)
		
	def auth(self):
		# This is to autheticate the user
		try:
			self.log_in()
		except:
			self.sign_in()
			Setup(self.username, self.password)

	def log_in(self):
		# This is a function that let's the user log_in
		# This is a function that log's the user in
		self.conn = psycopg2.connect(dbname=f"{self.username}_game", user=f"{self.username}",
						password=f"{self.create_password()}", host="127.0.0.1")

	def sign_in(self):
		conn = psycopg2.connect(dbname=f"postgres", user=f"postgres", password="12", host="127.0.0.1")
		cur = conn.cursor()
		cur.execute(f"CREATE USER {self.username} WITH PASSWORD '{self.password}'")
		conn.commit()

		cur.close()
		conn.close()