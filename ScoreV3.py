#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy 
import scipy
import math
from scipy import special
#difficulty integral approximation
def S(n,m):
    #derivatives of erfinv
    y = special.erfinv((n-m)/(n+1))
    y1 = math.exp(y*y) * math.sqrt(math.pi) / 2
    y2 = 2 * y * y1 * y1
    y3 = 2 * y1 * (y * y2 + (2 * y**2 + 1) * y1**2)
    y4 = 2 * y1 * (y * y3 + (6 * y**2 + 3) * y1 * y2 + (4 * y**3 + 6 * y) * y1**3)
    #beta central moments
    a = n-m
    b = m+1
    u2 = a*b / ((a+b)**2 * (a+b+1))
    u3 = 2 * (b-a) * a * b / ((a+b+2) * (a+b)**3 * (a+b+1))
    u4 = (3 + 6 * ((a-b)^2 * (a+b+1) - a*b * (a+b+2)) / (a*b * (a+b+2) * (a+b+3))) * u2**2 
    #Put it all together
    return math.sqrt(2) * (y + 0.5 * y2 * u2 + 1/6 * y3 * u3 + 1/24 * y4 * u4)    
elapsed_objects = int(input("Enter elapsed objects"))
total_objects = int(input("Enter total objects"))
m = int(input("Enter misses"))
acc = float(input("Enter accuracy between 0 and 1"))
ScoreV3 = 1000000 * (0.7 * math.sqrt(S(total_objects,m)/S(total_objects,0)) + 0.3 * math.pow(acc,10)) * elapsed_objects / total_objects
print(ScoreV3)

