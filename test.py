import json
import numpy as np

class Laptop():
	name = "somename"

class Stack():
	topPointer = 0
	innerList = []
	def push(item):
		innerList.append(item)		




#laptop1 = Laptop()
#laptop1.name = 'Dell Alienware'
#laptop1.processor = 'Intel Core i7'
#laptop1.newField = "chaman"
#jsonStr = json.dumps(laptop1.__dict__)
#print(jsonStr)
#()[]{}

charMap = { ')' : '(', '}' : '{', ']' : '[' }
openChars = ['(', '{', '[']

input = '{{()}}'

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