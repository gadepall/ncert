# -*- coding: utf-8 -*-
"""Assignment3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YCSg8VKwMvN5Nx9PLe1ntVAgaRX94u0J
"""

#Code by K.A. Raja Babu
#May 19, 2021
import numpy as np
import matplotlib.pyplot as plt
from coeffs import * #refered from G.V.V sir's code

#centre and radius of circles
O=np.array([0,0])
r1=2.5
r2=4

#point on circles
A1=np.array([O[0]+r1,O[1]])
A2=np.array([O[0],O[1]+r2])

#Generating all lines
x_OA1 = line_gen(O,A1)
x_OA2 = line_gen(O,A2)

#Plotting all lines
plt.plot(x_OA1[0,:],x_OA1[1,:],label='$r=2.5$')
plt.plot(x_OA2[0,:],x_OA2[1,:],label='$r=4$')

#Plotting the first circle of radius 2.5
c1 = 2.5
theta1 = np.linspace(0,2*np.pi,50)
x1 = c1*np.cos(theta1)
y1 = c1*np.sin(theta1)

plt.plot(x1,y1,label='$circle with (r=2.5)$')

#Plotting the second circle of radius 4
c2 = 4
theta2 = np.linspace(0,2*np.pi,50)
x2 = c2*np.cos(theta2)
y2 = c2*np.sin(theta2)

plt.plot(x2,y2,label='$circle with (r=2.5)$')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.text(0,0,'O')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
plt.show()