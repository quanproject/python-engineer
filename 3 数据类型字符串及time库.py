#第三章 笔记

#整数类型
'''
二进制 0b1111 OB110
八进制 0o123 0O12315
十六进制 0x5123 0X1231
'''

#浮点数类型
'''
不确定尾数，使用round解决 round(a,b)  将a的小数点b位后四舍五入取整
'''
if 0.1+0.2==0.3:
    print("1 ok")
else:
    print("2 false")
#这里将输出false
if round(0.1+0.2,10)==0.3:
    print("3 ok")
#输出ok

#复数类型
z=1.2+3j
print(z.real,z.imag)  #获取复数的实部和虚部函数



#数值操作
'''
幂运算
x**y         x的y次方（y为小数开根


abs(x)                取x的绝对值
divmod（x，y）        返回x和y的商余       (x/y,x%y)
pow（x,y,[,z]）       (x**y)%z
round(x,[,d])         四舍五入

int(x) float(x) complex(x)     数值转换
'''

#字符串操作
'''
三单引号 双引号 单引号 三种字符串表示方式
保证字符串中可以包含单引号和双引号

索引  
字符串[N]  访问N标号的字符

切片
字符串[M:N]     返回M到N
字符串[M:N:K]   以步长K在范围NM内进行切片（K为-1时可作为逆序

转义符\     表达字符本意
'''

#字符串操作符
'''
x+y         连接x和y
x*n         复制n次字符串x（可以反过来写
x in s      判断x是不是s的子串
'''

#字符串处理函数
'''
len(x)            返回字符串长度
str(x)            将任何其他类型转换为字符串类型   （与eval相反
hex(x)   oct(x)   将整数转换为十六进制或八进制的字符串
chr（u）          返回u（Unicode编码）对应字符
ord（x）          返回x（字符）对应编码
'''
print(ord('❤'),chr(10000))
for i in range(12):
    print(chr(9800+i),end="")          #end等于空代表每次输出不换行

#字符串处理方法(以字符串str为例
'''
str.append(c)                      将c添加到字符串str后面
str.lower()   str.upper()          将字符串全部转换为大/小写
str.split(sep=None)                将字符串用sep分割，返回其列表
str.count(sub)                     返回sub在字符串出现的次数
str.replace(old,new)               将字符串中old字符替换为new字符
str.centre(width[,fillchar])       根据宽度width居中，并用fillchar填充
str.strip(chars)                   去除字符串两端的chars字符（可以是多个“=1a”）去除（碾压墙x
str.join(iter)                     将str加入到每个iter字符的后面，除了最后一个（注意主次
'''

#字符串格式化.format（）

"{}:计算机{}的CPU占用率为{}%".format("2018-10-10","C",10)
#槽{}与for中每个逗号间隔的内容一一对应(槽中可以填数字来改变对应关系
'''
{<参数序号>:<格式控制标记>}
  ：      <填充>    <对齐>   <宽度>    <，>       <.精度>          <类型>
引导     填充单个    < > ^    槽输出   数字的千   浮点小数精度    b c d o x X
符号      字符     左右 居中    宽度    位分割符   字符串最大长度    e E f %

'''
print("\n{:=^20}".format("终止"))

#time库的使用
import time
'''
时间获取
time.time()      获取当前时间戳（浮点数）
time.ctime()     获取易读的当前时间（字符串）
time.gmtime()    获取可用于计算机处理的时间
'''
print(time.ctime())
'''
时间格式化
strftime（tpl,ts)    以tps格式输出ts时间
      %Y 年            %m 月数字   
      %B 月英文        %b 月缩写
      %d 日数字        %A 星期英文
      %a 星期缩写      %H 24h小时
      %h 12h小时       %p 上下午
      %M 分钟          %S 秒

strptime(str,tpl)  按照模板拆卸时间字符串
'''
t=time.gmtime()
print(time.strftime("%Y-%m-%d %H:%M:%S",t)) #模板控制
'''
程序计时
time.perf_counter()          返回CPU级别的精确时间计时（差值求程序运行时间
time.sleep(s)                程序休眠t秒
'''