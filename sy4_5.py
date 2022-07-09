#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/13 18:29
# @Author  : CYLlinmaian
# @FileName: sy4_5.py
# @Software: PyCharm
import numpy as np
import matplotlib.pyplot as plt
a = np.arange(0.0, 5.0, 0.02)
plt.plot(a, np. cos(2*np.pi*a),'r--')
plt.xlabel('横轴:时间',fontproperties= 'SimHei' , fontsize=15,color= 'green')
plt.ylabel('纵轴:振幅',fontproperties= 'SimHei' , fontsize=15)
plt.title(r'正弦波 $y=cos(2\pi x$)',fontproperties='SimHei', fontsize=25)
plt.text(2, 1, r'$\mu=100$', fontsize=15)
plt.axis([-1, 6, -2, 2])
plt .grid(True)
plt.savefig('sy4_5', dpi=1000)  #PNG文件
plt . show( )
