# Author: Derek Royse
# Project Euler - Problem 022:
# Using names.txt (right click and 'Save Link/Target As...'), a
# 46K text file containing over five-thousand first names, begin 
# by sorting it into alphabetical order. Then working out the 
# alphabetical value for each name, multiply this value by its 
# alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, 
# COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th 
# name in the list. So, COLIN would obtain a score of 938 * 53 = 
# 49714.
# What is the total of all the name scores in the file?

# Import text file
import csv
with open('files/names.txt', 'rb') as f:
    reader = csv.reader(f)
    nameList = list(reader)

# Sort list
sortedList = sorted(nameList[0])

# Find and sum alphabetical name value
answer = 0
for idx,name in enumerate(sortedList):
    nameScore = 0
    for c in name:
            nameScore += (ord(c)-64) * (idx+1)
    answer += nameScore
    
print(answer)