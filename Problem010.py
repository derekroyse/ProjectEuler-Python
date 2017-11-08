# Author: Derek Royse
# Project Euler - Problem 010:
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import math
 
limit = 2000000
sum = 0
 
def isPrime(x):
    # Eliminate even numbers > 2
    if x%2 == 0 and x > 2:
        return False
    # Loop starts at 3, test up to the sqrt of the input, test only odd numbers    
    else:
        for i in range(3,int(math.sqrt(x))+1,2):
            if x%i == 0:
                return False
        return True
 
for i in range(2, limit):
    if isPrime(i):
        sum += i
   
print(sum)