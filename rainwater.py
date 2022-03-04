from ast import In

import unittest
Input = [0,1,0,2,1,0,1,3,2,1,2,1]

diff = []

maxHeight = 0

for level in Input:
    if (level > maxHeight):
        maxHeight = level
        diff.append(0)
    else: 
        diff.append( maxHeight - level )

print(Input)
print(diff)