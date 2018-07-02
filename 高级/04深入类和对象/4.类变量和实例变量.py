__author__ = 'jiangjun'
__date__ = '2018/6/20 下午11:37'


class A:
    aa = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y


a = A(2, 3)

A.aa = 11   # 修改类变量
print(a.x, a.y, a.aa)   # 2 3 11
print(A.aa) # 11

a.aa = 100  # 【在对象a上新建一个aa变量，而不会改变类变量的值】
print(a.aa) # 100
print(a.__dir__())  # [..., aa ,...]

print(A.aa) # 11

b = A(7, 8)
print(b.aa) # 11