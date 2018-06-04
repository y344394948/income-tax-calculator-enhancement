#!/usr/bin/env python3

import sys
import csv
from collections import namedtuple

# 使用 namedtuple 的方式来存储个税计算表
# 优势是避免了使用索引来获取个税阶梯和税率造成代码难以维护的状态
IncomeTaxQuickLookupItem = namedtuple(
    'IncomeTaxQuickLookupItem',
    ['start_point', 'tax_rate', 'quick_substractor']
)

# 个税起征点 3500
INCOME_TAX_START_POINT = 3500

# 个税计算表，采用列表存储的方式，每一行都是一个 namedtuple
# 每个 namedtuplt 包含该计算阶梯的起始薪资、税率、速算扣除数
INCOME_TAX_QUICK_LOOKUP_TABLE = [
    IncomeTaxQuickLookupItem(80000, 0.45, 13505),
    IncomeTaxQuickLookupItem(55000, 0.35, 5505),
    IncomeTaxQuickLookupItem(35000, 0.30, 2755),
    IncomeTaxQuickLookupItem(9000, 0.25, 1005),
    IncomeTaxQuickLookupItem(4500, 0.2, 555),
    IncomeTaxQuickLookupItem(1500, 0.1, 105),
    IncomeTaxQuickLookupItem(0, 0.03, 0)
]

# 命令行参数处理类
class Args(object):

    # 初始化的时候读取命令行中输入的所有参数到self.args列表中
    def __init__(self):
        self.args = sys.argv[1:]
    
    # 以_开头的函数为类对象的内部函数，不会被外部使用，option指-c/-d/-o，该函数是用来提取参数 -c/-d/-o 后面的值
    def _value_after_option(self, option):
    try:
        # 首先获得参数 -c/-d/-o 所在位置在列表 sys.args中的索引值
        index = self.args.index(option)
        # 获取 -c/-d/-o 所在位置的下一个位置的字符串就是对应的值
        return self.args[index + 1]
    except (ValueError, IndexError):
        # 如果获取出错，则打印错误信息并退出
        print('Parameter Error')
        exit()

    #获取 -c 参数对应的值，即配置文件的路径
    #@property 将函数变成属性，例如：调用时可通过args.config_path方式获取配置文件的路径
    @property
    def config_path(self):
        return self._value_after_option('-c')

    #获取 -d 参数对应的值，即用户工资数据文件的路径
    @property
    def userdate_path(self):
        return self._value_after_option('-d')
    
    #获取 -o 参数对应的值，即输出的用户工资单文件的路径
    @property
    def export_path(self):
        return self.value_after_option('-o')

# 创建命令行参数处理的对象 args
# 在此处创建的原因是后续的 class Config 的代码定义中需要用到这个对象
args = Args()

# 配置文件读取处理类
class Config(object):


    # 初始化的时候调用

    def __init__(self):
        self.config = 
    
    def _read_config(self):
        # 从 args 对象中获得配置文件路径
        config_path = args.config_path
        # 初始化存储配置项和值的字典
        config = {}
        # 打开配置文件读取数据
        with open(config_path) as f:
            #读取每一行数据
            for line in f.readlines():
                # 使用 ＝ 分割每一行的内容，注意需要去掉每行两边的空格
                key, value = line.strip()

config = Config()

# 用户工资文件处理类
class UserData(object):


userdata = UserData()

#税后工资计算类
class IncomeTaxCalculator(object):




if __name__ = '__main__':
