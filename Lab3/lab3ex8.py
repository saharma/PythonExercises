def month(n):
	if (n > 0) and (n < 13):
		months = {1 : 'Jan', 2 : 'Feb', 3 : 'Mar', 4 : 'Apr', 5 : 'May', 6 : 'Jun',
		7 : 'Jul', 8 : 'Aug', 9 : 'Sep', 10 : 'Oct', 11 : 'Nov', 12 : 'Dec'}
		return months[n]
	else: 
		print("Pick a number between 1 and 12")	

print(month(90))		

