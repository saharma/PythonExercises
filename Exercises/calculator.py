class Calculator:
	def __init__(numbers, num1, num2):
		numbers._num1 = num1
		numbers._num2 = num2

	def add(numbers):
		return numbers._num1 + numbers._num2

	def subtract(numbers):
		return numbers._num1 - numbers._num2

	def multiply(numbers):
		return numbers._num1 * numbers._num2

	def division(numbers):
		return numbers._num1 / numbers._num2	

	def modulo(numbers):
		return numbers._num1 % numbers._num2

	def power(numbers):
		return numbers._num1 ** numbers._num2				


num1 = float(input("Enter first number: "))	
num2 = float(input("Enter second number: "))	

calc = Calculator(num1, num2)

print(calc.add())
print(calc.subtract())
print(calc.multiply())
print(calc.division())
print(calc.modulo())
print(calc.power())
		