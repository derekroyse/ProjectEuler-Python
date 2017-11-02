# Author: Derek Royse
# Project Euler - Problem 004:
# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

limit = 999
largest = 0

def isPalindrome(x):
    converted = str(x)
    firstHalf = converted[:int(len(converted)/2)]
    secondHalf= converted[int(len(converted)/2):]
    
    if firstHalf != secondHalf[::-1]:
        return False         
    else:    
        return True
    
for i in range(limit+1):
    for j in range(limit+1):
        if isPalindrome(i*j) and i*j > largest:  
            largest = i*j
        
print(largest)