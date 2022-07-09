#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/5/1 21:36
# @Author  : CYLlinmaian
# @FileName: sy1_5.py
# @Software: PyCharm
#PythonDraw.py
import turtle
turtle.setup(650, 350, 200, 200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("pink")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
turtle.done()