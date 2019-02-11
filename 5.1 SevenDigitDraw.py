#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#七段数码管绘制
import turtle
import time
def drawgap():        #数码管之间的间隔
    turtle.penup()
    turtle.fd(5)
def drawline(draw):   #一段数码管
    drawgap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawgap()
    turtle.right(90)

def drawdigit(digit):   #一个数字
    drawline(True) if digit in [2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,1, 3, 4, 5, 6,7, 8, 9] else drawline(False)
    drawline(True) if digit in [0,2, 3, 5, 6, 8, 9] else drawline(False)
    drawline(True) if digit in [0,2, 6, 8] else drawline(False)
    turtle.left(90)
    drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,7,8,9,] else drawline(False)
    drawline(True) if digit in [0,1,2,3,4,7,8,9,] else drawline(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)

def drawdate(date):        #字符串转化为单个数字并绘制
    for i in date:
        if i=='=':
            turtle.color("blue")
            turtle.write('年', font=('Arial', 18, "normal"))
            turtle.color('red')
            turtle.fd(40)
        elif i =='-':
            turtle.color("blue")
            turtle.write('月', font=('Arial', 18, "normal"))
            turtle.color('red')
            turtle.fd(40)
        elif i=="+":
            turtle.color("blue")
            turtle.write('日', font=('Arial', 18, "normal"))
            turtle.color('red')
            turtle.fd(40)
        else :
            drawdigit(eval(i))

def main():
    turtle.setup(800,350,200,200)
    turtle.hideturtle()
    turtle.pensize(5)
    turtle.pencolor('red')
    turtle.penup()
    turtle.fd(-300)
    timenow=time.strftime("%Y=%m-%d+",time.gmtime()) #获取系统时间并格式化
    drawdate(timenow)
    turtle.done()
main()