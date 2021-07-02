# -*- coding: utf-8 -*-
"""Assignment-4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1asmxv7njCaeINhN2EMGEXk8B0y0FbPyL
"""

import matplotlib.pyplot as plt
import numpy as np
 
x = np.linspace(-4, 4, 200)
 
y = x**2-3
 
a = 1
b = 0
c = -3
 
d1 = -b + np.sqrt(b**2-4*a*c)
d2 = -b - np.sqrt(b**2-4*a*c)
d1 = d1/(2*a)
d2 = d2/(2*a)
 
plt.plot(x,y,label='$y=x^2-3$')
plt.grid()
 
plt.plot(d2,0, 'o')
plt.text(d2,0.6, 'A')
plt.plot(d1, 0, 'o')
plt.text(d1,1.0, 'B')
plt.plot(0,-3, 'o')
plt.text(0,-3,'c')
 
#show plot
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend()
 
plt.show()