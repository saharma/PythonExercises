str1 = input("Please enter a string: ")
str2 = input("Please enter a second string: ")

if len(str1) == len(str2):
	print("These strings are the same length")
	if str1 == str2:
		print("They have the same contence")
	else:
		print("They do not have the same content.")	
else:
	print("These strings are not the same length. \n They do not have the same content.")	
