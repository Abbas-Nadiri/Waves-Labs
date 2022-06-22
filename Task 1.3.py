# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 12:21:50 2022

@author: abbas
"""
import numpy as np
import matplotlib.pyplot as plt
import math

#loads in and parses text file containing x and y values

x1, y1 = np.loadtxt("semicirclehigh.txt", unpack=True, skiprows=1)

#plots the graph for the semi-circle

plt.plot(x1,y1,"x")

#creates an empty variable to add up the individual areas into

integral = 0

for i in range(0,len(y1)-1):
    
    if y1[i] == 0: #for the first triangle 
        triangle = float((y1[i+1]) * (x1[i+1]-x1[i]) / 2)
        integral = integral + triangle
        
    elif y1[i+1] == 0: #for the final triangle
        triangle2 = float((y1[i]) * (x1[i+1]-x1[i]) / 2)
        integral = integral + triangle2
        
    else:#for the trapezia
        trapezium = ((y1[i] + y1[i+1]) * (x1[i+1]-x1[i]) / 2)
        integral = integral + trapezium

print(integral) #prints the overall numerically integrated area
print(0.5 * math.pi *1)#prints the analytically calculated area of the semicircle where r=1