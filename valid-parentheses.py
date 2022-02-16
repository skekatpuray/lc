import json
import numpy as np

input = '{{()}}'
charMap = { ')' : '(', '}' : '{', ']' : '[' }
openChars = ['(', '{', '[']
lst = []

isValid = False

for someChar in input:
	if (len(lst) == 0):
		lst.append(someChar)
	else:
		if (openChars.__contains__(someChar)):
			lst.append(someChar)
		else:
			topChar = lst.__getitem__(len(lst) - 1)
			if (topChar == charMap[someChar]):
				lst.pop()
			else:
				isValid = False
				break


if (len(lst) == 0):
	isValid = True

print(isValid)