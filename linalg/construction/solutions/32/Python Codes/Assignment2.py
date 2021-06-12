# -*- coding: utf-8 -*-
"""Assignment2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tfm80Z_fJLERZ_pRf5JhS4qxF--e86Dv
"""

#Code by K.A. Raja Babu
#May 11, 2021
#Drawing a quadrilateral PQRS
import numpy as np
import matplotlib.pyplot as plt
from coeffs import * #refered from G.V.V sir's code

#Quadrilateral vertices
P = np.array([0,0])
Q = np.array([3.283,1.33j])
R = np.array([7.416,3]) 
S = np.array([7.5,0]) 

#Generating all lines
x_PQ = line_gen(P,Q)
x_PS = line_gen(P,S)
x_SQ = line_gen(S,Q)
x_PR = line_gen(P,R)
x_QR = line_gen(Q,R)
x_RS = line_gen(R,S)

#Plotting all lines
plt.plot(x_PQ[0,:],x_PQ[1,:],label='$PQ$')
plt.plot(x_PS[0,:],x_PS[1,:],label='$PS$')
plt.plot(x_SQ[0,:],x_SQ[1,:],label='$SQ$')
plt.plot(x_PR[0,:],x_PR[1,:],label='$PR$')
plt.plot(x_QR[0,:],x_QR[1,:],label='$QR$')
plt.plot(x_SR[0,:],x_SR[1,:],label='$SR$')

plt.plot(Q[0], Q[1], 'o')
plt.text(Q[0] * (1 + 0.1), Q[1] * (1 - 0.1) , 'Q')
plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 - 0.2), P[1] * (1) , 'P')
plt.plot(S[0], S[1], 'o')
plt.text(S[0] * (1 + 0.03), S[1] * (1 - 0.1) , 'S')
plt.plot(R[0], R[1], 'o')
plt.text(R[0] * (1 + 0.03), R[1] * (1 - 0.1) , 'R')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')