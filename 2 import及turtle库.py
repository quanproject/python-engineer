#第二章 笔记

#import 用法
'''
import <库名>
<库名>.<函数名>(<函数参数>)

from <库名> import <函数名>  
限定一个函数可以不写库名直接调用

from <库名> import* 
<函数名>(<函数参数>)

import <库名> as <自定义别名>
<别名>.<函数名>(<函数参数>)

'''


#turtle 库使用
'''
画布控制
t.setup(x,y)         设置画布的像素
t.title(str)         设置窗口名称
t.hideturtle()       隐藏小箭头

画笔参数控制
turtle.pendown()    turtle.pd()    笔落下
turtle.penup()      turtle.pu()    笔抬起
turtle.pensize()    turtle.width() 笔宽度
turtle.pencolor("black")           笔颜色（颜色字符串）
turtle.pencolor(0.63,0.13,0.94)          （rgb小数值及元祖值）
'''
'''
画笔运动控制
t.forward(d)             t.fd(d)   向正方向行进d
t.circle(r,extend=None)            以方向左侧r处为圆心画extend角度（默认360°）  
t.write(zi,fort=(格式))            按照格式绘制汉字zi
'''
'''
方向控制函数
t.setheading(angle)       t.seth(angle)  设定方向角度（绝对）
t.right(angle)                           相对左右转angle°      
t.left(angle)
'''

#range函数
'''
range(N)  产生0到N-1的整数序列
range(M,N)   M到N-1
'''

