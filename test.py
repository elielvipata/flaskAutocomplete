

file = open("words", "r")
lines = file.readlines()
words = []
for line in lines:
	words.append(line[0:-1])

print(words)
