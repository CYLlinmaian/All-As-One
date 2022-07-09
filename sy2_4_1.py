#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/16 15:01
# @Author  : CYLlinmaian
# @FileName: sy2_4_1.py
# @Software: PyCharm
import time
scale=10
print("------开始------")
for i in range(scale+1):
    a,b='***' * i,'···' * (scale-i)
    c=(i/scale)*100
    print("%{:^3.0f}[{}->{}]".format(c,a,b))
    time.sleep(0.1)
print("------结束------")