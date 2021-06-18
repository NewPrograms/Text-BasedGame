import time
import sys
from operator import itemgetter
from numpy.random import choice
class Choices:

	def __init__(self):
        pass
    
	def options(self):
		print(
			"[1] Attack!\n",
			"[2] Run!\n",
			"[3] Defend!\n",
			"[4] Hide!\n"
				)

	def results(self):
		chosen = input("Choose: ")

		self.count = self.countdown(5)

		if chosen == "1":
			pass
		elif chosen == "2":
			self.result = self.run()
			return self.result
		elif chosen == "3":
			pass
		elif chosen == "4":
			self.result = self.hide()
			return self.hide
		
		else:
			print("Invalid Choice!")
			sys.exit()
		
		if self.count == 'stop':
			self.random_choice()
		
		else:
			time.sleep(5-self.count)


	def run(self):
		self.succ_chance = self.calc_success()
		self.fail_chance = abs(1-self.succ_chance)
		choices = ['Successful', 'You got hit!']
		result = choice(choices, p=[self.succ_chance, self.fail_chance])
		return result

	def hide(self):
		choices = ['Successful', 'The creature saw you!', 'The creature saw you and pounced at you!']
	   	self.result = choice(choices,  p=[0.2, 0.5, 0.3])
		return self.result

	def attack(self):
		pass
	def calc_success(self):
		self.statement =  'SELECT health, stamina FROM player'
		self.values = self.pull.pull_val(self.statement)
		self.health, self.stamina = itemgetter(0,1)(self.values)
		result = (self.health/100 + self.stamina/100)/3
		return result

	def countdown(time_sec):
		while time_sec:
			mins, secs = divmod(time_sec, 60)
			timeformat = '{:02d}:{:02d}'.format(mins, secs)
			print(timeformat, end='\r')
			time.sleep(1)
			time_sec -= 1

		return "stop"

	def random_choice(self):
		choices = [self.attack(), self.hide(), self.run(), self.defend()]
		res = choice(choices)
		return res

if __name__ == '__main__':
	choices = Choices()
	choices.results()