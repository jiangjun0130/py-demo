__author__ = 'jiangjun'
__date__ = '2018/5/24 下午10:41'


class A:
    def __init__(self):
        print('A')


class B(A):
    def __init__(self):
        print('B')


class C(A):
    def __init__(self):
        print('C')


class D(B, C):
    pass


obj = D()