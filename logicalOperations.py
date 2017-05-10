class nameChecker
def __init__(name, name1):
	name._name1 = name1

enterName(name){
	name = input("Enter your name: ")
}

checkName(name){
	if name.startswith("t","T"):
		print("Name okay")
	else:
		print("Enter a name that begins with t")
  		name = input("Enter your name: ")
}

checkLength(name){
	if len(name) < 3:
		print("Too short")
		enterName(name)

	elif len(name) > 6:
		print("Too long")
		enterName(name)	

	else:
		print("YEA BOI")	
}
