

name = input("Enter your name: ")
	

tees = "t", "T"
if name.startswith(tees):
	print("Name okay")
	if len(name) < 3:
		print("Too short")

	elif len(name) > 6:
		print("Too long")

	else:
		print("YEA BOI")	
	
else:
	print("Enter a name that begins with t")
	name = input("Enter your name: ")
	


