#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:29:24 2024

@author: reggiehacker
"""
import numpy as np
import matplotlib.pyplot as plt

v0 = 50
ang = 30
g = 9.81

#convert to radians
angrad =  np.radians(ang)

#total time in air
tt = 2*(v0*np.sin(angrad))/g

#time intervals
time_intervals = np.linspace(0,tt, 50)

#empty arrays
x_intervals = np.empty(len(time_intervals))
y_intervals = np.empty(len(time_intervals))



#Loop
for i in time_intervals:
    index=np.where(time_intervals==i)
    x = float(v0*np.cos(angrad)*i)
    y = float((v0*np.sin(angrad)*i)-(0.5*g*(i**2)))
    x_intervals[index] = x
    y_intervals[index] = y
    
#subplot sizes
plt.subplots(1,3, figsize= (10, 5))
#subplot
plt.subplot(1,3,1)
plt.plot(time_intervals, x_intervals)
plt.xlabel('time')
plt.ylabel('horizontal distance')
plt.title('x vs t')

plt.subplot(1,3,2)
plt.plot(time_intervals, y_intervals)
plt.xlabel('time')
plt.ylabel('vertical distance')
plt.title('y vs t')

plt.subplot(1,3,3)
plt.plot(x_intervals, y_intervals)
plt.label('horizontal distance')
plt.ylabel('vertical distance')
plt.title('y vs x')

plt.tight_layout()
plt.show()