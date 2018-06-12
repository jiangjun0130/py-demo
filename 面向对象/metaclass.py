__author__ = 'jiangjun'
__date__ = '2018/5/29 上午12:01'


class MyType(type):

    def __init__(self, what, bases=None, dict=None):
        print('MyType __init__')
        super(MyType, self).__init__(what, bases, dict)

    def __call__(self, *args, **kwargs):
        print('MyType __call__')
        obj = self.__new__(self, *args, **kwargs)
        self.__init__(obj, *args, **kwargs)


class Foo(object):

    __metaclass__ = MyType

    def __init__(self, name):
        self.name = name
        print('Foo __init__')

    def __new__(cls, *args, **kwargs):
        print('Foo __new__')
        obj = object.__new__(cls)
        # 个性化初始化等操作
        obj.id_card = '123'

        return obj

foo = Foo(name='jj')
print(foo.id_card)