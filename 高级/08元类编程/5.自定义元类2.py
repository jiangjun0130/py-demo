__author__ = 'jiangjun'
__date__ = '2018/7/2 上午10:59'


class BaseClass:
    def answer(self):
        return 'I am base class'

# 什么是元类？
# 元类是创建类的类。 对象->class(对象)->type


class MetaClass(type):

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)


class User3(metaclass=MetaClass):

    """
    创建User的过程，委托给了元类MetaClass
    """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'user3'


# python中类的实例化过程， 会首先寻找metaclass，通过metaclass去创建User类
# type去创建类对象，通过类对象创建实例对象


if __name__ == '__main__':
    user = User3(name='tom')
    print(user)