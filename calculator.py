#!/usr/bin/env python3

import sys, csv

# 定义一个命令行参数类
class Args():
    
    # 初始化对象，读取命令行中输入的所有参数到l列表中
    def __init__(self):
        l = sys.argv[1:]
        # 获得l列表中的-c索引，index('-c')＋1获取-c后的参数，即配置文件的路径.并将列表中的该值赋值给类中的属性
        self.c = l[l.index('-c')+1]
        self.d = l[l.index('-d')+1]
        self.o = l[l.index('-o')+1]

# 创建Args()的对象
args = Args()

# 定义一个配置文件类
class Config():
    
    # 初始化对象，定义一个config属性，调用内部函数_a(), 并将返回值写入类的config属性
    def __init__(self):
        self.config = self._a()
    # 创建内部函数，用来读取配置文件中的内容
    def _a(self):
         # 初始化存储配置项和值的字典
         d = {'s':0}
         # 通过args实例，读取对象中的c属性的值，即打开配置文件并以读取所有行的方式读取数据
         with open(args.c) as f:
             for i in f.readlines():
                 # 使用字符串split('=')将配置想和值切分开
                 l = i.split(' = ')
                 # 使用strip()去掉字符串两边的空格，并将值分别赋值给m,n
                 m, n = l[0].strip(), l[1].strip()
                 # 当m的值等于社保缴费基数下限或上限时，将n转化为浮点型，并赋值给字典中m
                 if m == 'JiShuL' or m == 'JiShuH':
                     d[m] = float(n)
                 # 否则 ？
                 else:
                     d['s'] += float(n)
         return d

# 调用Config()类的属性config，创建该属性的实例
config = Config().config


# 定义一个计算税费的函数，i是工资金额，z为整数型的工资金额，sb是各项社保费总额，x是应纳税所得额，s是应纳税额，sh为税后工资
def cal_tax(i):
    z = int(i)
    sb = z * config.get('s')
    if z < config.get('JiShuL'):
        sb = config['JishuL'] * config.get('s')
    if z > config.get('JiShuH'):
        sb = config['JishuH'] * config.get('s')
    x = (z - sb -3500)
    if x < 0:
        s = 0
    elif x <= 1500:
        s = x * 0.03
    elif x <= 4500:
        s = x * 0.1 - 105
    elif x <= 9000:
        s = x * 0.2 - 555
    elif x <= 35000:
        s = x * 0.25 - 1005
    elif x <= 55000:
        s = x * 0.3 - 2755
    elif x <= 80000:
        s = x * 0.35 - 5505
    else:
        s = x * 0.45 - 13505
    sh = z - sb - s
    return [z, format(sb, '.2f'), format(s, '.2f'), format(sh, '.2f')]
    

# 定义一个用户数据类
class UserData():
    # 初始化对象
    def __init__(self):
        # 打开并读取用户数据文件，写入l列表中
        with open(args.d) as f:
            l = list(csv.reader(f))
        # ？
        self.value = 1

data = UserData().value

# 以写入的方式打开员工工资单文件
with open(args.o, 'w') as f:
     # ？
     for a, b in data:
         x = cal_tax(b)
         x.insert(0, a)
         csv.writer(f).writerow(x)
