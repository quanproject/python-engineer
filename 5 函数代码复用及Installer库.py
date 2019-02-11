#第五章 笔记

#函数
'''
def <函数名>(<必须参数>，<可选参数>,<可变参数（*b）>):
    <函数体>
    return <返回值>
'''
#计算n!//m
def fact1(n,m=1):         #可选参数m
    s=1
    for i in range(1,n+1):
        s*=i
    s//=m
    return s,m         #可以返回多个值（元祖类型
print(fact1(10,5))

def fact2(n,*b):           #可变参数
    s=1
    for i in range(1,n+1):
        s*=i
    for j in b:
        s*=j
    return s
print(fact2(10,4,6,2))  #调用不限个数

#全局变量及局部变量
'''
1.使用global声明来在局部范围内使用和修改全局变量
2.全局声明的组合数据类型不需要声明便可在局部范围修改
'''

#lambda函数
'''
<函数名>=lambda<参数>:<表达式>
'''
f=lambda x,y:x+y
print(f(2,3))


#pyInstaller库(.py转换为可执行文件(.exe  第三方库
'''
安装：
cmd 执行 pip install pyinstaller
'''
'''
常用命令
-F 生成打包文件
-h 帮助菜单
--clean 清理过程文件
-i 关联图标(.ico)
'''