#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/6/13 18:22
# @Author  : CYLlinmaian
# @FileName: sy4_4.py
# @Software: PyCharm
import matplotlib. pyplot as plt
import numpy as np
a = np.arange(10)
plt.plot(a, a*1.5,'go-' ,a, a*2.5, 'rx',a, a*3.5,'*', a, a*4.5,'b-.')
plt.savefig('sy4_4', dpi=1000)  #PNG文件
plt . show( )
