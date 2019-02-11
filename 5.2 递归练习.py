#!/usr/bin/env python 
# -*- coding:utf-8 -*-

#1. 实现s[::-1] 字符串反转
def rvs (s):
    if s == "":
        return s
    else:
        return rvs(s[1:])+s[0]
str1 ="abcde"
print(rvs(str1))

#2.  斐波那契数列
def f(n):
    if n==1 or n==2:
        return 1
    else:
        return f(n-1)+f(n-2)
print(f(10))

#3.  汉诺塔问题
count=0
def hanoi(n,src,dst,mid):
    global count
    if n==1:
        print("{}:{}->{}".format(1,src,dst))
        count+=1
    else:
        hanoi(n-1,src,mid,dst)
        print("{}:{}->{}".format(n,src,dst))
        count+=1
        hanoi(n-1,mid,dst,src)
hanoi(3,'A','B','C')
print(count)