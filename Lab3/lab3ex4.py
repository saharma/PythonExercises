class Person:
	def __init__(self, name, year):
		self._name = name
		self.year = year

	def get_age(self):
		return 2017 - self.year

	def get_name(self):
		return self._name 

	def get_details(self):
		return self._name + self.year

class Student(Person):
	def __init__(self, name, year, student_number):
		Person.__init__(self, name, year)
		self.student_number = student_number

	def get_details(self):
		return self.student_number

	def mature(self):
		return (self.get_age()> 23)

s = Student('Sahar',1991, 1280)
print(str(s.get_details()))
print(s.get_name())
print(s.mature())	