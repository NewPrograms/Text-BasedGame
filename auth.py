import psycopg2
import sys
from setup import Setup

class Auth():
	def __init__(self, username = None, password = None):
		# These two define the username and password
		if username and password is None:
			self.username = "postgres"
			self.password = "12"
		else:
			self.username = username
			self.password = password

	def auth(self):
		# This is to autheticate the user
		# How to define permanently what is the username, and password.
		# Without using parameters in auth.
		try:
			self.log_in()
			self.log_out
			return True
		except:
			self.sign_in()
			# Give log_in a default value
			Setup(self.username, self.password)
			return True

	def log_in(self,):
		# This is a function that let's the user log_in
		# This is a function that log's the user in
		self.conn = psycopg2.connect(dbname=f"{self.username}_game", user=f"{self.username}",
						password=f"{self.password}", host="127.0.0.1")
		self.cur = self.conn.cursor()

	def sign_in(self):
		conn = psycopg2.connect(dbname=f"postgres", user=f"postgres", password="12", host="127.0.0.1")
		cur = conn.cursor()
		cur.execute(f"CREATE USER {self.username} WITH PASSWORD '{self.password}'")
		conn.commit()

		cur.close()
		conn.close()

	def log_out(self):
		self.cur.close()
		self.conn.close()

