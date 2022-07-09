#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/10 21:24
# @Author  : CYLlinmaian
# @FileName: sy2_1.py
# @Software: PyCharm
print(30-3**2+8//3**2+10%3)
'''
i=314159
j=bin(i)
k=oct(i)
l=hex(i)
print(j,k,l)
'''
print(5/5)

complex = 2.3e+3-1.34e-3j
print('复数 complex中的实部为：', complex.real)
print('复数 complex中的虚部为：', complex.imag)

print(30-3**2+8//3**2*10)
print(3*4**2/8%5)
print(2**2**3)

x = (1+3*3)*(16 % 7)/7
print(x)

n=input("请输入需要转换的数:")
print ("n用科学计数法表示为:""%e"%n)
print("n转换为十六进制数为:""%x"%n)
print("n转换为浮点数为：""%f"%n)
