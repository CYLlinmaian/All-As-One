#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/1 21:33
# @Author  : CYLlinmaian
# @FileName: sy1_4.py
# @Software: PyCharm
#汇率兑换程序
#1美元=6 人民币
TempStr=input("请输入带字符的金额(美元：d or D,人民币：r or R):")
if TempStr[-1] in ['d','D']:
    R=int(eval(TempStr[0:-1])*6)
    print("兑换成人民币为:{} RMB".format(R))
elif TempStr[-1] in ['r','R']:
    D=int(eval(TempStr[0:-1])/6)
    print("兑换成美元为：{} Dollar".format(D))
else:
    print("输入格式错误")