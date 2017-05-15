class Person:
	def __init__(self, name, year):
		self._name = name
		self.year = year

	def get_age(self):
		return 2017 - self.year

	def get_name(self):
		return self._name 

	def get_details(self):
		return self._name 

