# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 15:22:12 2022

@author: henry

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

terms = [1, 2]
eventerms = [2]


while terms[-1] < 4e6:
    newterm = terms[-1]+terms[-2]
    terms.append(newterm)
    if newterm % 2 == 0:
        eventerms.append(newterm)
    
    
    
print(terms)
print(eventerms)
    

