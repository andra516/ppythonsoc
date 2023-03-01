# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 13:54:39 2022

@author: henry
"""

def divisible_by_20(number):
    d = []
    number = 10
    for i in range(1,21):
        if number%i == 0:
            d.append(1)
        else:
            d.append(0)
    if sum(d) == 20:
        return True
    else:
        return False
    

flag =False
number = 20

while not flag:
    flag = divisible_by_20(number)
    number+=1
        
        
        
    