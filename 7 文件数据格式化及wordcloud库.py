#第七章 笔记


#文件类型（展示方式
'''
文本文件       二进制文件
.txt .py       .png  .avi
'''
tf=open("f.txt","rt")
print(1,tf.readline())
tf.close()

#文件的打开和关闭
'''
###打开###
<变量名>=open(<文件名>,<打开模式>)

文件名
绝对路径：D:/python-engineer/f.txt    （使用斜杠/或者双反斜杠\\防止与反斜杠冲突
相对路径: f.txt

打开模式
r     只读，文件不存在报错 FileNotFoundError （默认
w     覆盖写，文件不存在则创建，存在就覆盖
x     创建写，不存在创建，存在报错 FileExistsError
a     追加写，存在就追加写入，不存在就创建
b     二进制打开
t     文本形式打开（默认
+     配合r w x a 在原功能基础上增加读写功能

###关闭###
<变量名>.close()

'''

#文件内容的读取
'''
<f>.read(size=-1)         读入全部内容，若给出参数，则读入前size长度
<f>.readline(size=-1)     读入一行内容，若给出参数，读入该行的前size长度
<f>.readlines(hint=1)     读入所有行，给出参数则读入前hint行
'''
fname=input("请输入要打开的文件名称：")  #文件的逐行遍历
fo=open(fname,"r")
for line in fo:   #也可以使用fo.readlines()
    print(2,line)
fo.close()

#数据的文件写入
'''
<f>.write(s)              向文件写入一个字符串或者字节流
<f>.writelines(lines)     将一个元素权威字符串的列表写入文件（将列表拼接在一起
<f>.seek(offset)          改变当前文件操作指针的位置，offset=0开头 1当前位置 2文件结尾
#在写入后立刻输出需要注意重新设置文件指针位置 seek（0）
'''
