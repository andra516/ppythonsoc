# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 09:15:37 2022

@author: henry
"""

import numpy as np 
import matplotlib.pyplot as plt

def func(c):
    l = []
    z = -0.7
    for i in range(20):
        z = z**2 + c
        if np.isnan(z) == True:
            return False
        else: l.append(z)
    x1 = abs(l[1] - l[0])
    x2 = abs(l[18] - l[19])
    if x1 < x2:
        return False
    else: return True

# print(func(-1.5 + 1j))

re = []
im = []
x_arr = np.linspace(-1.5, 0.5, 10)
y_arr = np.linspace(-1.2, 1.2, 10)  
for x in x_arr:
    for y in y_arr:
        c = x + y*1j
        if func(c) == True:
            #print(c.real)
            #print(c.imag)
            re.append(c.real)
            im.append(c.imag)
            
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111)

ax.scatter(re, im, marker='o', color='k')
plt.show()