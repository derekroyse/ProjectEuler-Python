# Author: Derek Royse
# Project Euler - Problem 003:
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
import math
limit = 600851475143
largestFactor = 0

def isPrime(x):
    for i in range(3,int(x/2),2):
        if x%i == 0:
            return False        
    return True

for i in range(1,int(math.sqrt(limit)),2):
    if limit%i == 0 and isPrime(i):        
        largestFactor = i
        
print(largestFactor)