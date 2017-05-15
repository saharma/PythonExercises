words = ['bat', 'ball', 'yarn','basket', 'badminton' ]

words.sort()
print(words[0])
print(words[len(words)-1])

if('badminton' in words):
	print('true')
else:
	print('false')	

words[len(words)-1] = 'beach'

print(words)
