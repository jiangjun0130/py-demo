__author__ = 'jiangjun'
__date__ = '2018/6/21 下午10:48'


class A:
    def __init__(self):
        print('A')


class B(A):
    def __init__(self):
        print('B')
        # python3对调用super进行了简化
        super().__init__()


class C(A):
    def __init__(self):
        print('C')
        super().__init__()


class D(B, C):
    def __init__(self):
        print('D')
        super().__init__()

#b = B()
# c = C() # C A

# d = D() # D B C A

print(D.__mro__)    # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)


