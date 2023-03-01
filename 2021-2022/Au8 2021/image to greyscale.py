# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 11:27:48 2021

@author: henry
"""

import PIL
import numpy as np
import matplotlib.pyplot as plt


dogImage = PIL.Image.open('dog.png')

dogArray = np.asarray(dogImage)

print(dogArray)


plt.imshow(dogImage)
