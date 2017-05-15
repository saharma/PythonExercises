try:
	aFile = open("calculator.py", "r")
	print(aFile.read())
	aFile.close()
except IOError, e:
	print('catching IO exception')