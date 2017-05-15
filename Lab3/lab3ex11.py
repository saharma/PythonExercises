a = [3,5,1,7,9]
b = [4,2,6,3,9]
r = []

def intersect(l,m):
	return list(set(l)&set(m))

print(intersect(a,b))


