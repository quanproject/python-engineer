#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#TempConvent.py
TempStr=input("请输入带有符号的温度值：")
if TempStr[-1] in ['F','f']:
    C=(eval(TempStr[0:-1])-32)/1.8         #评估函数eval 去掉两侧引号并执行内部语句
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C','c']:
    F=1.8*eval(TempStr[0:-1])+32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入的格式错误")