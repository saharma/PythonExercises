grades = [[95,92,86,87], [66,54], [89,72,100], [33,0,0]]

def avg(list):
	for l in list:
		print(sum(l)/len(l))

avg(grades)		