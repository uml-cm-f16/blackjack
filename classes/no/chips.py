class Chips():

	def __init__(self, balance = 0):
		self.__wager = 0
		self.__balance = balance

	def __repr__(self):
		tmp = Template("$balance C")
		return tmp.substitute(balance=self.__balance)



	def __decrease(self, amount):
		self.__balance -= amount

	def wage(self, amount):

	def increase(self, amount):
		self.__balance += amount

	def balance(self):
		return self.__balance

