import numpy as np


input = '[[]{}{{}}'
charMap = { ')' : '(', '}' : '{', ']' : '[' }
openChars = ['(', '{', '[']
isValid = False
currentIndex = 0
myArray = np.chararray(10000)
for someChar in input:
    if (currentIndex == 0) :
        myArray[currentIndex] = someChar
        currentIndex = currentIndex + 1
    else:
        if (openChars.__contains__(someChar)):
            myArray[currentIndex] = someChar
            currentIndex += 1
        else:
            topChar = myArray[currentIndex - 1]
            if (ord(topChar) == ord(charMap[someChar])):
                currentIndex -= 1
            else:
                isValid = False
                break

if (currentIndex == 0):
    isValid = True

print(isValid)
