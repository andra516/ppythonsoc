# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 15:33:28 2022

@author: henry
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

palidromes = []
## generate a number using two 3 digit numbers
## check it's a palindrome
for n1 in range(100, 999):
    for n2 in range(100, 999):
        N = n1*n2
        Nstring = str(N)
        # is N a palidrome?
        if Nstring == Nstring[::-1]:
            palidromes.append(N)
    
print(palidromes)
