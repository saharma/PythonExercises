albert = "albert einstein"
bertie = "bertie"

result = ""
for x in bertie:
	for y in albert:
		if y == x:
			result = result + y
			break		
print(result)			