#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/10 11:35
# @Author  : CYLlinmaian
# @FileName: sy4_1.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
plt.plot([0,1,3,4,5,6,7,8,9,10,11,12], [15,20.5,23,28,30,33,34,35,35,36,37,39])
plt.title("实验四")
plt.xlabel('月份')
plt.ylabel('增长值')
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12])
plt.yticks([0,4,8,12,16,20,24,28,32,36,40,44,48])
plt.show()
