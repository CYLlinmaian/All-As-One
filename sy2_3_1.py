#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/15 22:05
# @Author  : CYLlinmaian
# @FileName: sy2_3_1.py
# @Software: PyCharm
a=input()
for i in range(len(a)):
    if ord('a')<=ord(a[i])<=ord('z'):
        print(chr((ord(a[i])+3-ord('a'))%26+ord('a')),end="")
    elif ord('A')<=ord(a[i])<=ord('Z'):
        print(chr((ord(a[i])+3-ord('A'))%26+ord('A')),end="")
    else:
        print(a[i],end="")