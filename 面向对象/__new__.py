__author__ = 'jiangjun'
__date__ = '2018/5/28 下午11:30'


class Foo(object):

    def __init__(self, name):
        self.name = name


f = Foo(name='Jack')
print(type(f))  # <class '__main__.Foo'>
print(type(Foo))  # <class 'type'>


# 创建类的特殊方式

def fun(self):
    print('hello')

Foo2 = type('Foo2', (object,), {'func': fun})
print(type(Foo2)) # <class 'type'>

