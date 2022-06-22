# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 18:26:18 2022

@author: abbas
"""

import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import signal

#input the number of datapoints to take

points=100
t=np.linspace(1,240,points)

#creates an array to hold the combined fourier wave for all odd harmonics

total=np.zeros(points)

#plots each harmonic

for i in range (1, 25):
    y = (200 / i * math.pi) * np.sin(2/240 * math.pi * i * t)/10
    #adds y-values of all odd harmonics to "total" array
    if i%2 == 1:
        total = total + y
    #plt.plot(t,y)

#plots a0/2

a0=np.full(points, 50)
#plt.plot(t, a0)

#plots fourier wave of odd harmonics

#total = total + a0
plt.plot(t,total)

#plots square wave

plt.plot(t, 50 * signal.square(1 * np.pi * 2/240 * t))

#sets graph parameters, axes and title 

plt.grid()
plt.ylim(-120,120)
plt.xlabel('Time')
plt.ylabel("Amplitude")
plt.title('Fourier Series up to n=3 and Square Wave')
