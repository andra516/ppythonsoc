# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 15:07:19 2022

@author: henry
"""

'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''


multiples = []

N = 1000

for num in range(1, N):
    if num%3 ==0 or num%5==0:
        multiples.append(num)
        
        
print(multiples)

print(sum(multiples))

