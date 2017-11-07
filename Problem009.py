# Author: Derek Royse
# Project Euler - Problem 009
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

class GetOutOfLoop( Exception ):
    pass

answer = 0
sum = 0
 
def isPyTriplet(a,b,c):
    if (a * a) + (b * b) == (c * c):
        return True
    else:      
        return False       
 
try:
    for i in range(500):
        for j in range(i+1, 500):
            for k in range(j+1, 500):
                sum = i + j + k
                if isPyTriplet(i,j,k) and sum == 1000:
                    answer = i * j * k
                    raise GetOutOfLoop
except GetOutOfLoop:
    pass

print(answer) 
