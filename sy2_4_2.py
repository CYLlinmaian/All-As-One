#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/16 15:16
# @Author  : CYLlinmaian
# @FileName: sy2_4_2.py
# @Software: PyCharm
import time
scale=50
print("------开始------".center(scale // 2,"-"))
start=time.perf_counter()
for i in range(scale+1):
    a="*" * i
    b="." * (scale-i)
    c=(i/scale) * 100
    dur=time.perf_counter()-start
    time.sleep(0.1)
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end="")
print("\n"+"------结束------".center(scale // 2,"-"))