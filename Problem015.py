# Author: Derek Royse
# Project Euler - Problem 015:
# Starting in the top left corner of a 2×2 grid, and only being able to move to 
# the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

from math import factorial

width = 20
height = 20

# routes = total!/width!/height!
print(int((factorial(width+height)/factorial(width)/factorial(height))))