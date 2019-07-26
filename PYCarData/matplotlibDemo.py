#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 10:10:08 2019

@author: lixin
"""
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9]
y = [11,5,3,4,15,1,17,2,19]
x1 = [1,2,3,4,5,6,7,8,9]
y1 = [1,25,3,14,25,1,7,12,9]
plt.xlabel('month')
plt.ylabel('sales')
plt.title("sales of company\n2019 company A and company B")
import matplotlib.pyplot as plt
plt.plot(x,y,label = "company A")
plt.plot(x1,y1,label = "company B")
plt.legend()
plt.show()