choice = input('Enter C for celsius-fahrenheit conversion or F for fahrenheit-celcius conversion: ')
if choice == 'C' or choice == 'c':
	celsius = int(input('Enter degree Celsius: '))
	fahrenheit = ((celsius * 9)/5) + 32
	print(fahrenheit)
elif choice == 'F' or choice == 'f':
	fahrenheit = int(input('Enter degree fahrenheit: '))
	celsius = ((fahrenheit - 32) * 5) / 9
	print(celsius)
else:
	print('Invalid choice. Exit')