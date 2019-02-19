#!/usr/bin/env python 
# -*- coding:utf-8 -*-
'''
资源：
中文 三国演义 https://python123.io/resources/pye/threekingdoms.txt
英文 哈姆雷特 https://python123.io/resources/pye/hamlet.txt
'''
#哈姆雷特
print("{:=^20}".format("哈姆雷特词频"))
def getText():
    txt=open("hamlet.txt","r").read() #文件读取
    txt=txt.lower()                   #全部转化为小写，去除大小写干扰
    for ch in '!"#$%^&*()_+-={}[];,./:<>?":':   #将所有特殊字符转化为空格
        txt=txt.replace(ch," ")
    return txt
def hamlet():
    hamletTxt=getText()
    words=hamletTxt.split()   #分割并返回列表
    counts={}           #空字典
    for word in words:   #读入
        counts[word]=counts.get(word,0)+1
    items=list(counts.items())   #转化为列表
    items.sort(key=lambda x:x[1],reverse=True) #以第二个为参数从大到小排列
    for i in range(10):
        word,count=items[i]
        print(i+1,"{0:<10}{1:>5}".format(word,count))
hamlet()

#三国演义
print("{:=^20}".format("三国演义词频"))
def threekingv1():
    import jieba
    txt=open("threekingdoms.txt","r",encoding="utf-8").read()
    words=jieba.lcut(txt)
    counts={}
    for word in words:
        if len(word)==1:
            continue
        else:
            counts[word]=counts.get(word,0)+1
    items = list(counts.items())  # 转化为列表
    items.sort(key=lambda x: x[1], reverse=True)  # 以第二个为参数从大到小排列
    for i in range(15):
        word,count = items[i]
        print(i + 1, "{0:<10}{1:>5}".format(word, count))
threekingv1()

#三国演义人物出场统计
print("{:=^20}".format("三国演义人物出场统计"))
def threekingv2():
    import jieba
    txt=open("threekingdoms.txt","r",encoding="utf-8").read()
    excludes={"将军","却说","荆州","二人","不可","不能","如此"}
    words=jieba.lcut(txt)
    counts={}
    for word in words:
        if len(word)==1:
            continue
        elif word=="玄德曰"or word=="玄德":
            wordr="刘备"
        elif word=="孔明曰"or word=="诸葛亮":
            wordr="孔明"
        elif word=="孟德"or word=="丞相":
            wordr="曹操"
        elif word=="关公"or word== "云长":
            wordr="关羽"
        else:
            wordr=word
        counts[wordr]=counts.get(wordr,0)+1
    for word in excludes:   #词库排除
        del counts[word]
    items = list(counts.items())  # 转化为列表
    items.sort(key=lambda x: x[1], reverse=True)  # 以第二个为参数从大到小排列
    for i in range(5):
        word,count = items[i]
        print(i + 1, "{0:<10}{1:>5}".format(word, count))
threekingv2()