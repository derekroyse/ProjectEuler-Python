# Author: Derek Royse
# Project Euler - Problem 017:
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out 
# in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 
# letters. The use of "and" when writing out numbers is in compliance with British 
# usage.

def getTen(x):
    if x == "9":
        return "nineteen"
    if x == "8":
        return "eighteen"
    if x == "7":
        return "seventeen"
    if x == "6":
        return "sixteen"
    if x == "5":
        return "fifteen"
    if x == "4":
        return "fourteen"    
    if x == "3":
        return "thirteen"
    if x == "2":
        return "twelve"
    if x == "1":
        return "eleven"
    if x == "0":
        return "ten"
    else:
        return ""

def singleDigit(x):
    if x == "9":
        return "nine"
    if x == "8":
        return "eight"
    if x == "7":
        return "seven"
    if x == "6":
        return "six"
    if x == "5":
        return "five"
    if x == "4":
        return "four"    
    if x == "3":
        return "three"
    if x == "2":
        return "two"
    if x == "1":
        return "one"
    else:
        return ""
def doubleDigit(x):
    if x == "9":
        return "ninety"
    if x == "8":
        return "eighty"
    if x == "7":
        return "seventy"
    if x == "6":
        return "sixty"
    if x == "5":
        return "fifty"
    if x == "4":
        return "forty"    
    if x == "3":
        return "thirty"
    if x == "2":
        return "twenty"
    else:
        return ""
def tripleDigit(x):
    if x == "9":
        return "ninehundred"
    if x == "8":
        return "eighthundred"
    if x == "7":
        return "sevenhundred"
    if x == "6":
        return "sixhundred"
    if x == "5":
        return "fivehundred"
    if x == "4":
        return "fourhundred"    
    if x == "3":
        return "threehundred"
    if x == "2":
        return "twohundred"
    if x == "1":
        return "onehundred"  
    else:
        return ""

def getWord(numberString):
    returnString = ""
    if numberString == "1000":
        return "onethousand"
    elif len(numberString) == 3 and numberString[1] == "1":
        returnString += tripleDigit(numberString[0])
        if numberString[1] + numberString[2] != "00":
            returnString += "and"
        returnString += getTen(numberString[2])
    elif len(numberString) == 2 and numberString[0] == "1":
        returnString += getTen(numberString[1])   
    elif len(numberString) == 3:
        returnString += tripleDigit(numberString[0])
        if numberString[1] + numberString[2] != "00":
            returnString += "and"
        returnString += doubleDigit(numberString[1])
        returnString += singleDigit(numberString[2])
    elif len(numberString) == 2:
        returnString += doubleDigit(numberString[0])
        returnString += singleDigit(numberString[1])
    elif len(numberString) == 1:
        returnString += singleDigit(numberString[0])
    else:
        return ""
        
    return returnString
    
answer = 0

for i in range(1, 1001):
  answer += len(getWord(str(i)))
    
print(answer)   