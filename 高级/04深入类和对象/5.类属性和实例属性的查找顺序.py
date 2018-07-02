__author__ = 'jiangjun'
__date__ = '2018/6/20 下午11:54'


class A:
    name = 'A'

    # def __init__(self):
    #     self.name = 'B'


a = A()
print(a.name)   # B。构造函数注释以后，打印值为：A
                # 结论：查找属性是从下往上查找