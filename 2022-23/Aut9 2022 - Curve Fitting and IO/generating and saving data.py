# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 17:04:39 2022

@author: henry
"""

import numpy as np
import matplotlib.pyplot as plt

def model_function(x, a,b):
    
    return x*a * np.exp(-b*x**2)



x = np.linspace(-8,8,100)
a = 0.5
b = 1/4

y = model_function(x, a, b) + 0.01*np.random.randn(len(x))



simulated_data = np.vstack((x,y)).T



np.savetxt('simulated_data.csv', simulated_data, delimiter=',')


fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111)
ax.scatter(x,y, color='red', marker='+', label='')
plt.show()
