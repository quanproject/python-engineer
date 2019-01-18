#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#  q:需要多少的工作日成长量才能比的上全年成长量？

#计算df成长下的全年总成长函数
def DayUp(df):
    dayup=1
    for i in range(365):
        if i%7 in [0,6]:
            dayup*=0.99
        else:
            dayup*=(1+df)
    return dayup

dayfactor=0.01
while DayUp(dayfactor) < 37.78:  #循环判断
    dayfactor+=0.001

print("需要工作日成长量：{:.3f}".format(dayfactor))