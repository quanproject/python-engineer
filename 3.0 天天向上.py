#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#DayDayUp.py
fact=0.01
day=1.0
for i in range(365):
    if i%7 in [0,6]:
        day*=(1-fact)
    else:
        day*=(1+fact)
print("只有工作日努力上涨：{:.2f}".format(day))