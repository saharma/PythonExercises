class BankAccount:
	def __init__(self, balance=0):
		self.balance = balance	

	def withdraw(self, amount):
	   	self.balance = self.balance - amount

	def deposit(self, amount):
		self.balance = self.balance + amount	

	def get_balance(self):
		return self.balance	


ba = BankAccount(100)
print(ba.get_balance())
ba.deposit(50)
ba.withdraw(25)
print(ba.get_balance())		