# Author: Derek Royse
# Project Euler - Problem 007:
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.
# What is the 10,001st prime number?
import math

limit = 10001
done = False
counter = 0
current = 2

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
    
while done is False:
    if isPrime(current):
        counter+=1
    if counter == limit:
       done = True
       break
    current+=1
    
print(current)
    
    

