x = input("Enter a list of words")

words = x.split()

for y in words:
	if len(y) == 4:
		print(y)