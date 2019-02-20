#!/usr/bin/env python 
# -*- coding:utf-8 -*-
#https://python123.io/resources/pye/%E6%96%B0%E6%97%B6%E4%BB%A3%E4%B8%AD%E5%9B%BD%E7%89%B9%E8%89%B2%E7%A4%BE%E4%BC%9A%E4%B8%BB%E4%B9%89.txt
#https://python123.io/resources/pye/%E5%85%B3%E4%BA%8E%E5%AE%9E%E6%96%BD%E4%B9%A1%E6%9D%91%E6%8C%AF%E5%85%B4%E6%88%98%E7%95%A5%E7%9A%84%E6%84%8F%E8%A7%81.txt

import jieba
import wordcloud
f=open("新时代中国特色社会主义.txt","r",encoding="utf-8")
t=f.read()
f.close()
ls=jieba.lcut(t)
txt=" ".join(ls)
w=wordcloud.WordCloud(font_path="msyh.ttc",\
    width=1000,height=700,background_color="white")
w.generate(txt)
w.to_file("grwordcloud.png")