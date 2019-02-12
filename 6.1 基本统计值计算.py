#!/usr/bin/env python 
# -*- coding:utf-8 -*-
def GetNum():  #获取数字
    num=[]
    iNumStr=input("请输入数字（直接回车退出）：")
    while iNumStr!="":
        num.append(eval(iNumStr))
        iNumStr=input("请输入数字（直接回车退出）：")
    return num
def avage(num):   #求平均值
    s=0.0
    for n in num:
        s+=n
    return s/len(num)
def median(num):   #计算中位数
    sorted(num)                   #排序函数
    size=len(num)
    if size%2==0:
        med=(num[size//2-1]+num[size//2])/2
    else:
        med=num[size//2]
    return med
def main():
    n=GetNum()
    print("平均数：",avage(n))
    print("中位数：",median(n))
main()
