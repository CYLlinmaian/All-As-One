#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/13 18:05
# @Author  : CYLlinmaian
# @FileName: sy4_2.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
ax1 = plt.subplot2grid((2,2), (0, 0), colspan=2)
t = np.linspace(0, 6, 100)
y = np.exp(-t)*np.cos(2*np.pi*t)
plt.plot(t, y, 'k', color='g', linewidth=3, linestyle="-")
#plt.show()
ax2 = plt.subplot2grid((2,2), (1, 0), colspan=2)
a = np.linspace(0, 6, 100)
y = np.cos(2*np.pi*a)
plt.plot(t, y, 'k', color='b', linewidth=3, linestyle="-")
plt.show()
