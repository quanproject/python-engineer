# 第四章 笔记

#分支结构
'''
<表达式1> if <条件> else <表达式2>          紧凑型判断（表达式不是语句

if elif else                               多分支

and or not                                 与或非

'''
#异常处理
'''
try:                   当语句1发生错误时
<语句块1>              
except <异常类型>:      且符合异常类型时输出语句2（可以不写类型
<语句块2>
'''
try:
    num=eval(input("请输入一个整数："))
except NameError:
    print("输入的不是整数：")
'''
try:
<1>
except:
<2>
else:
<3>
finally:
<4>
1发生错误时执行2，1无错误执行3,最后一定执行4
'''

#循环结构
'''
#遍历循环
for <循环变量> in <遍历结构>
 <执行语句>
 实质是遍历结构中的每个变量一次放入循环变量中并执行语句，直到循环结构结束

for in range(M,N,K) 计数循环

for c in str       字符串遍历循环

for item in ls     列表遍历循环

for line（文件每一行） in fi（文件标示符）     文件遍历循环

#无限循环
while <条件>:
<语句块>

#循环控制保留字
break continue

#循环加入else 可以在循环正常执行完毕时执行else（没有被break退出
'''

#random 库 (随机数
'''
seed(a=None)        初始化种子（不填使用时间
random()            产生随机数（0-1）

randint(a,b)        产生[a,b]之间的整数
getrandbits(k)      产生k比特长的整数
uniform(a,b)        产生[a.b]之间的随机小数 
randrange(m,n[,k])  产生[a,b]之间k倍随机数
choise(seq)         随机选择列表seq中的一个元素            
shuffle(seq)        返回随机打乱顺序的seq列表           
'''