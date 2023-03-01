## -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 09:02:32 2022

@author: henry
"""

### IMPORT DEPENDENCIES
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate

### WRITE THE DERIVATIVES FUNCTION
def derivatives(y, t, w):
    '''
    Compute the derivative of y wrt t
    Inputs:
        - y: array containing y[0]: x, y[1]: v
        - t: array, float representing time
        - w: float representing freq.
    Output:
        - dydt: array containing dydt[0] = v, dydt[1] = -w^2 x
    '''
    dydt = np.zeros(shape=len(y))
    dydt[0] = y[1]
    dydt[1] = - w**2 * y[0]
    
    return dydt

### SET UP INITIAL VALUES AND T ARRAY

w = (1,)
### INTEGRATION LINE
y0 = np.array([0, 1])
tArray = np.linspace(0, 10, 100)

intData = integrate.odeint(derivatives, y0, t=tArray, args=w)


positions = intData[:,0]
velocities = intData[:,1]

fig = plt.figure(figsize=(10,10))
ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)



ax1.plot(tArray, positions, color='darkblue', label='$Positions$')
ax2.plot(tArray, velocities, color='orange', linestyle='--', label='$Velocities$')
ax3.plot(positions, velocities, color='purple', label='Phase plane')


ax1.grid()
ax2.grid()
ax3.grid()
ax1.legend(fontsize=15)
ax2.legend(fontsize=15)
ax3.legend(fontsize=15)

plt.show()












