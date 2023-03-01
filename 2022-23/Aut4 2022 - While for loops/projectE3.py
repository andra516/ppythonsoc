# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 15:25:57 2022

@author: henry

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

number = 600851475143

primefactors = []


for k in range(1, number):
    if number%k == 0:
        # k is a factor of number
        # check if k is prime
        kfactors = []
        for i in range(2,k-1):
            if k%i == 0:
                kfactors.append(i)
        if len(kfactors) == 0:
            primefactors.append(k)
            
uniquefactors = set(primefactors)
