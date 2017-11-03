# Author: Derek Royse
# Project Euler - Problem 005:
# 2520 is the smallest number that can be divided by 
# each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 20?
limit = 20
done = False
current = limit

while not done:
    for i in range(1, limit+1):
        if current % i == 0 and i == limit:
            done = True
        elif current % i == 0:
            continue
        else:
            current += limit
            break

print(current)