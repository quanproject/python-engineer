#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
文件格式规定
行进距离，转向判断0左1右，转向角度，rgb三色
例： 300，1，144，0，1，0   使用010颜色向前300，随后右转144度
'''
import turtle as t
t.title("自动轨迹绘制")
t.setup(800,600,0,0)
t.pencolor("red")
t.pensize(5)
#数据读取
datals=[]
f=open("data.txt")
for line in f:
    line=line.replace("\n"," ")
    datals.append(list(map(eval,line.split(","))))  #map函数，用第一个参数（函数）依次作用在第二个参数（组合类型）上
f.close()
#绘制
for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])
t.done()