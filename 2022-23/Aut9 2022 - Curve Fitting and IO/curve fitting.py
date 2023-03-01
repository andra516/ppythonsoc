# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 17:03:54 2022

@author: henry
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

### Define a model function
def model_function(x, a, b):
    return x*a * np.exp(-b*x**2)


### load in data
data = np.loadtxt('simulated_data.csv', delimiter=',')


### Plot the data, see what it looks like
x = data[:,0]
y = data[:,1]


### curve_fit call
popt, pcov = curve_fit(model_function, x, y, p0=[1,1])

#### Now plot data with overlay of fitted function

fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111)

ax.scatter(x,y, color='darkred', marker='+')
xModel = np.linspace(min(x), max(x), 1000)
a, b = popt
ax.plot(xModel, model_function(xModel, a,b), 'darkgreen', linewidth=2, label=f'$a$={a:.2f},\n$b$={b:.2f}')

plt.legend()