# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 15:37:56 2022

@author: henry
"""

notFound = True
num = 1
maxDivisor = 20

while notFound:
    num += 2
    divisibleFlag = []
    for divisor in range(1,maxDivisor+1):
        if num%divisor == 0:
            divisibleFlag.append(1)
        else:
            divisibleFlag.append(0)
    if sum(divisibleFlag) == maxDivisor:
        notFound=False

print(num)

