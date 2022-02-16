#I can be placed before V (5) and X (10) to make 4 and 9. 
#X can be placed before L (50) and C (100) to make 40 and 90. 
#C can be placed before D (500) and M (1000) to make 400 and 900.
import numpy as np
symbolMap = { 'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000 }
s = "MCMXCIV"
sum = 0

negativeChars = {'IV' : 2, 'IX' : 2, 'XL' : 20, 'XC' : 20, 'CD' : 200, 'CM' : 200}

negativeCharSequence = ''
negativeSum = 0

for symbol in s:
    sum = sum + symbolMap[symbol]
    print(negativeCharSequence)
    if (negativeCharSequence == ''):
        negativeCharSequence = symbol
    else:
        if (len(negativeCharSequence) == 2):
            if (negativeChars.__contains__(negativeCharSequence) == True):
                negativeSum = negativeSum + negativeChars[negativeCharSequence]
            negativeCharSequence = negativeCharSequence[1] + symbol
        else:
            negativeCharSequence = negativeCharSequence + symbol


if (negativeChars.__contains__(negativeCharSequence) == True):
    negativeSum = negativeSum + negativeChars[negativeCharSequence]
    
print(sum - negativeSum)
