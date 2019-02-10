#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#公式计算
pi=0
N=100
for k in range(N):
    pi+=1/pow(16,k)*(\
    4/(8*k+1)-2/(8*k+4)-\
    1/(8*k+5)-1/(8*k+6))           #\换行标志
print("圆周率的值为(公式):{}".format(pi))

#蒙特卡洛方法
from random import random
from time import perf_counter
DARTS=1000*1000
hits=0.0
start=perf_counter()
for i in range(1,DARTS+1):
    x,y=random(),random()
    dist=pow(x**2+y**2,0.5)
    if dist <=1.0:
        hits+=1
pi=4*(hits/DARTS)
print("圆周率的值为（蒙特卡洛）:{}".format(pi))
print("运行时间:{:.5f}".format(perf_counter()-start))