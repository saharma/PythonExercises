class Animal: 
	def __init__(self, name, age):
		self._name = name
		self._age = age

	def describe(self):
		return 'This is {} and she is {} years old'.format(self._name, self._age)

	def speak(self):	
		raise NotImplemented('Speak method is not implemented')


class Dog(Animal):
	def __init__(self, name, age, breed):
		super().__init__(name, age)
		self._breed = breed

	def speak(self):
		return 'Woof woof!'

	def describe(self):
		return super().describe() + 'She is a {}'.format(self._breed)	


my_dog = Dog('Daisy', 3, 'labrador')

description = my_dog.describe()
print('Description: {}'.format(description))

speech = my_dog.speak()
print('She says: "{}"'.format(speech))	

