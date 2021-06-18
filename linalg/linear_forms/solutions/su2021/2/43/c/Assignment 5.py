# -*- coding: utf-8 -*-
"""ASSIGNMENT 5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Q54zdLNmUWEIHDXSDehqEoNSfWU9SJdw
"""

from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
 
def plot_planes(a1,b1,c1,d1,a2,b2,c2,d2):
    x = np.linspace(-1,1,10)
    y = np.linspace(-1,1,10)
 
    X,Y = np.meshgrid(x,y)
    Z1 = (d1 - a1*X - b1*Y) / c1
    Z2 = (d2 - a2*X - b2*Y) / c2
 
    fig = plt.figure()
    ax = fig.gca(projection='3d')
 
    ax.set_xlabel('x axis')
    ax.set_ylabel('y axis')
    ax.set_zlabel('z axis')
 
    surf1 = ax.plot_surface(X, Y, Z1)
    surf2 = ax.plot_surface(X, Y, Z2)
 
    plt.title('Parallel Planes')
    plt.show()
plot_planes(2,-2,4,-5,3,-3,6,1)