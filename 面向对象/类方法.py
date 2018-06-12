__author__ = 'jiangjun'
__date__ = '2018/5/27 下午9:13'


class Dog(object):
    """
    类方法:只能访问类变量，不能访问实例变量
    """

    def __init__(self, name):
        self.name = name

    @classmethod
    def eat(cls, name, food):
        print('%s is eating %s' % (name, food))


d = Dog('二哈')
d.eat('二哈', '包子')