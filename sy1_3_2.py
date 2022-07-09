#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/1 22:09
# @Author  : CYLlinmaian
# @FileName: sy1_3_2.py
# @Software: PyCharm
import turtle as t
t.Pen()  # 获得画笔
my_color=("red", "green", "yellow", "blue")
t.width(3)  # 画笔宽度
t.speed(3)  # 画笔画的速度
for i in range(10):  # 0,1,2,3,4
    t.penup()  # 抬起笔
    t.goto(0, -i * 10)
    t.pendown()  # 放画笔
    t.color(my_color[i % len(my_color)])  # 对my_color的数量取余数
    t.circle(10 + i * 10)      # 半径100
t.done()                  # 程序执行完，窗口仍然在
