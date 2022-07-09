#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/16 14:43
# @Author  : CYLlinmaian
# @FileName: sy2_3_2.py
# @Software: PyCharm
x=input("请输入需要解密的数据:")
print("解密成功:")
for p in x:
    if "a" <= p <= "z":
        print(chr(ord("a")+(ord(p)-ord("a")-3)%26), end='')
    elif "A" <= p <= "Z":
        print(chr(ord("A")+(ord(p)-ord("A")-3)%26), end='')
    else:
        print(p, end='')
