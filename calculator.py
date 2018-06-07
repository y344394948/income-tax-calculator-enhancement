#!/usr/bin/env python3
# _*_ coding: utf-8 _*_    #用的是utf-8编码

# 导入系统接口，调用命令行参数
import sys
# 导入纯文本文件模块
import csv

# 定义一个命令行参数类，从命令行获得路径
class Args():
    
    # 定义初始化函数，self是指向实例的，读取命令行中输入的参数(除了第一个参数./calculator.py)到l列表中
    def __init__(self):
        l = sys.argv[1:]
        # 获得l列表中的-c索引，index('-c')＋1获取-c后的参数，即配置文件的路径.并将列表中的该值赋值给类中的属性
        try:
            self.c = l[l.index('-c')+1]
            self.d = l[l.index('-d')+1]
            self.o = l[l.index('-o')+1]
        except ValueError:
            print('Parameter Error')
            exit()

# 创建Args()的对象，实例化该对象，才会自动调用__init__初始化函数，执行后面的内容，不实例化就不会执行__init__函数，不能获得类中的属性
args = Args()

# 定义一个配置文件类，从配置路径里面获得配置文件
class Config():
    
    # 定义初始化函数，定义一个config属性，调用内部函数_read_config(), 并将返回值写入类的config属性
    def __init__(self):
        self.config = self._read_config()
    # 创建内部函数，用来读取配置文件中的内容
    def _read_config(self):
         # 初始化存储配置项和值的字典,s是社保比例的和
         d = {'s':0}
         # 通过args实例，读取对象中的c属性的值，即打开配置文件并以读取所有行的方式读取数据
         with open(args.c) as f:
             for i in f.readlines():
                 # 使用字符串split('=')将配置想和值切分开
                 l = i.split(' = ')
                 # 第一组第一个参数为key，第二个参数为value，使用strip()去掉字符串两边的空格，并将值分别赋值给m,n
                 m, n = l[0].strip(), l[1].strip()
                 # 当m的值等于社保缴费基数下限或上限时，将n转化为浮点型，并将第一个和第二个放入字典中
                 if m == 'JiShuL' or m == 'JiShuH':
                     d[m] = float(n)
                 # 否则后面的数据项依次放入字典中，可以通过d['s']获得比例和上下限
                 else:
                     d['s'] += float(n)
         return d

# 调用Config()类的属性config，创建该属性的实例
config = Config().config


# 定义一个计算税费的函数，i是工资金额，z为整数型的工资金额，sb是各项社保费总额，x是应纳税所得额，s_tax是应纳税额，sh为税后工资
def cal_tax(i):
    z = int(i)
    sb = z * config.get('s')
    if z < config.get('JiShuL'):
        sb = config['JiShuL'] * config.get('s')
    if z > config.get('JiShuH'):
        sb = config['JiShuH'] * config.get('s')
    x = (z - sb -3500)
    if x < 0:
        s_tax = 0
    elif x <= 1500:
        s_tax = x * 0.03
    elif x <= 4500:
        s_tax = x * 0.1 - 105
    elif x <= 9000:
        s_tax = x * 0.2 - 555
    elif x <= 35000:
        s_tax = x * 0.25 - 1005
    elif x <= 55000:
        s_tax = x * 0.3 - 2755
    elif x <= 80000:
        s_tax = x * 0.35 - 5505
    els_taxe:
        s_tax = x * 0.45 - 13505
    sh = z - sb - s_tax
    return [z, format(sb, '.2f'), format(s_tax, '.2f'), format(sh, '.2f')]
    

# 定义一个用户数据类
class UserData():
    # 初始化对象
    def __init__(self):
        # 打开并读取用户数据文件，写入l列表中
        with open(args.d) as f:
        # reader是csv读取文件的方法，把文件内容读取出来成为列表
            l = list(csv.reader(f))
        # 将列表赋值给类属性value，实例的value值就是列表
        self.value = l

# 调用类属性value,创建用户数据类的实例
data = UserData().value

# 以写入的方式打开员工工资单文件
with open(args.o, 'w') as f:
     # 遍历data工号列表，a是工号，b 是工资
     for a, b in data:
         # 把工资调入函数中，返回一个列表
         x = cal_tax(b)
         # 在x列表索引为0的位置插入工号a，也就是101
         x.insert(0, a)
         # 调用csve的写入方法，写入f,也就是输出的args.o里面，row表示一行
         csv.writer(f).writerow(x)
