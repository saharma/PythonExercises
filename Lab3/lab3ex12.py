def pay(wage, hours):
	if hours < 40:
		print(wage * hours)
	else:
		print((wage * 40) + ((hours-40)*1.5*wage))

pay(10, 41)		
