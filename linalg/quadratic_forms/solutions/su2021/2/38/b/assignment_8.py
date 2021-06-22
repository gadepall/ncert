# -*- coding: utf-8 -*-
"""Assignment-8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KA51YM0-v5Z19odHbRVmVFIKYIfC7F_0
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111)
len = 150
y = np.linspace(-1,1,len)

#Generate line points
def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB


#hyper parameters
V = np.array(([1,0],[0,-16]))
f = -16
u = np.array(([0,0]))
Vinv = LA.inv(V)

#Eigenvalues and eigenvectors
D_vec,P = LA.eig(V)
D = np.diag(D_vec)
uconst = u.T@Vinv@u-f
a = np.sqrt(np.abs(uconst/D_vec[0]))
b = np.sqrt(np.abs(uconst/D_vec[1]))

def hyper_gen(y):
	x = 4*np.sqrt(1+y**2)
	return x

#Affine Parameters
c = -Vinv@u
R =  np.array(([4,0],[0,1]))
ParamMatrix = np.array(([a,0],[0,b]))


#Generating the Standard Hyperbola
x = hyper_gen(y)
xStandardHyperLeft = np.vstack((-x,y))
xStandardHyperRight = np.vstack((x,y))

#Plotting points
A = np.array([4,0])
B = np.array([-4,0])
f = np.array([np.sqrt(17),0])
M = np.array([np.sqrt(17),0.25])
N = np.array([np.sqrt(17),-0.25])

#Latus rectum
x_MN = line_gen(M,N)
plt.plot(x_MN[0,:],x_MN[1,:],label='$Latus rectum$')


#Plotting the standard hyperbola
plt.plot(xStandardHyperLeft[0,:],xStandardHyperLeft[1,:],label='Standard hyperbola',color='b')
plt.plot(xStandardHyperRight[0,:],xStandardHyperRight[1,:],color='b')


plt.plot(0,0, 'o',color='r',markersize=3)
plt.text(0.2 ,-0.2,'C')
plt.plot(4,0, 'o',color='r',markersize=3)
plt.text(3.5 ,-0.2,'A')
plt.plot(-4,0, 'o',color='r',markersize=3)
plt.text(-3.9 ,0.2,'B')
plt.plot(4.123,0.25, 'o',color='r',markersize=3)
plt.text(4.3 ,0.4,'M')
plt.plot(4.123,-0.25, 'o',color='r',markersize=3)
plt.text(4.3 ,-0.4,'N')
plt.plot(4.123,0, 'o',color='r',markersize=3)
plt.text(4.3 ,0.1,'f')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.show()