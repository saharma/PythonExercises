str = input("Enter Words: ")

words = str.split(' ')

wordMap = {}

for word in words:
	word_len = len(word)

	if word_len not in wordMap:
		wordMap[word_len] = []

	wordMap[word_len].append(word)

print(wordMap)