#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#eekNamePrint.py


weekStr="一二三四五六天"
weekId=eval(input("请输入你要输入的星期数字："))
pos=weekId-1
print("星期"+weekStr[pos:pos+1]+chr(10004))
#输出星期