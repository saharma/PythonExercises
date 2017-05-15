class Rectangle:
	def __init__(self, length, width):
		self.length = length
		self.width = width

	def perimeter(self):
		return 2*(self.width+self.length)

	def area(self):
		return int(self.length) * int(self.width)

r1 = Rectangle(3,4)
print(r1.perimeter())
print(r1.area())	

