#第六章 笔记

#集合类型及操作
print("{:=^30}".format("集合类型"))
'''
不能改变且各不相同的数据类型的无序集合

{<元素>,<元素>,<元素>}
建立用{}和set()(空集合必须

观察下列输出
'''
A={"python",123,('python',123)}
print(1,A)
B=set("pypy123")
print(2,B)
C={"python",123,'python',123}
print(3,C)
'''
#集合运算（可以使用增强操作符！！
S|T    并     返回包含st的所有元素的集合
S-T    差     返回有s但无t的集合
S&T    交     返回st共有元素的集合
S^T    补     返回st不同元素的集合

S<=T S<T      判断ST的子集关系
S>=T S>t      判断ST的包含关系
'''
'''
#操作函数及方法
S.add（x)         若S中无x就添加x
S.discard（x）    移除S中的x，若S没有x，不报错
S.removed（x）    同上但会报错 KeyError，可以用于异常处理try except
S.clear（）       清空S
S.pop()           随机取出返回S的一个元素，若S为空报错 KeyError

S.copy()          返回S的副本
len(S)            返回S元素个数
x in S            判断S中是否有x
x not in S        判断S中是否没有x
set(x)            将其他类型转换为集合类型（数据去重
'''
try:
    while True:
        print(A.pop(),end="")
except:
    pass
print("\n",4,A) #变为空集合set()

#序列类型及操作
print("{:=^30}".format("序列类型"))
'''
有先后关系的一组任意类型的元素（是字符串、元祖、列表类型的基类

'''
'''
#操作符及函数

x in s
x not in s
x+t
s*n n*s
s[i]
s[i:j(:k)]

以下例子（类似字符串
'''
ls=["pythion",123,'.io']
print(1,ls[::-1])
'''
len(s)
min(s) max(s)              s中元素需要可以比较，否则报错 TypeError
s.index(x) s.index(x,i,j)  返回x（在i到j）第一次出现在s的位置
s.count(x)                 返回s中出现x的总次数
'''
#元组类型
print("元祖:\n")
'''
一旦创建就不能修改！

使用（）或tuple（）创建
'''
creature="cat","mao","neko"
print(1,creature)

color=(0x001100,"blue",creature)
print(2,color)

print(3,color[-1][-2])  #双索引

#列表类型
print("列表：\n")
'''
可修改

使用[]或者list（）创建列表（A=b等于A是b的别名，并没有创建新列表
'''
'''
#方法及操作

ls[i]=x         将列表第i位替换为x
ls[i:j:k]=lt    用lt替换ls的切片后列表
del ls[i]       删除ls中第i元素
del ls[i:j:k]   步长范围删除
ls+=lt          将lt元素增加到ls中

ls.append(x)    在列表最后增加一个元素
ls.clear()      清空ls
ls.copy()       创建一个新列表，并赋值ls的元素
ls.insert(i,x)  在列表ls 的第i位置增加元素x
ls.pop(i)       取出第i个元素
ls.remove(x)    删除ls中第一个出现的x元素
ls.reverse()    反转ls中的元素

'''

#字典类型及操作
print("{:=^30}".format("字典类型"))
'''
映射（自定义索引）的一种体现

创建使用{}和dict()，键值对用:表示(都可以生成空字典
{<键1>:<值1>,<键2>:<值2>,<键3>:<值3>}

<值>=<字典变量>[<键>]    给值（键）赋值新的键（值）
                        键值都不存在时直接添加新键值对
'''
D={"中国":"北京","美国":"华盛顿","法国":"巴黎"}
print(1,D)
print(2,D["中国"])
print(3,type(D))            #type检查变量类型
'''
#处理类型及方法
del d[k]    
k in d      判断 键 k是否在d中
d.key()     返回所有键信息
d.values()  返回所有值信息
d.items()   返回所有键值对信息

d.get(k,<default>)   若键k存在，返回对应值，不存在返回default值
d.pop(k,<default>)   取出操作（同上
d.popitem()          随机取出一个键值对，元组形式返回
d.clear()
len(d)

'''
print(4,D.items())

#jieba库（第三方中文分词库
print("{:=^30}".format("jieba库"))
'''
安装：
cmd 命令 pip install jieba
pycharm 文件内搜索安装
'''
'''
#分词模式
jieba.lcut(s)                精确模式（原文切分
jieba.lcut(s,cut_all=True)   全模式（所有组合列出,有冗余
jieba.lcut_for_search(s)     搜索引擎模式（精确模式下继续分词,有冗余
jieba.add_word(w)            向词库增加新词
'''
import jieba
print(jieba.lcut("中国是一个伟大的国家"))
