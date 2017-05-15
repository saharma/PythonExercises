#2015 Q1

userTxt = input("Insert Text: ")


def my_swapcase(s):
	txt = []

	for c in s:
	    if c.isupper():
	    	txt.append(c.lower())
	    else:
	        txt.append(c.upper())
	print(''.join(txt))


my_swapcase(userTxt)	

