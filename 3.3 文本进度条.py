#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#TextProBar.py
import time
scale=20
print("{:-^10}".format("执行开始"))
start=time.perf_counter()
for i in range(scale+1):
    a='*'*i
    b='.'*(scale-i)
    c=(i/scale)*100
    dur=time.perf_counter()-start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end="")  #\r使光标回退
    time.sleep(0.1)
print("\n{:-^10}".format("执行结束"))