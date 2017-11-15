# Author: Derek Royse
# Project Euler - Problem 016
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

from math import pow
 
answer = 0
 
toCount = str(int(pow(2,1000)))
 
for i in toCount:
    answer += int(i)   
 
print(answer)