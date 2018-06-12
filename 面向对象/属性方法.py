__author__ = 'jiangjun'
__date__ = '2018/5/27 下午9:21'


class Dog(object):
    """
    属性方法:把一个方法变成一个静态属性
    """

    def __init__(self, name):
        self.name = name
        self.__food = None

    @property
    def eat(self):
        print('%s is eating %s' % (self.name, self.__food))

    @eat.setter
    def eat(self, food):
        print('set to food:%s' % food)
        self.__food = food

    @eat.deleter
    def eat(self):
        del self.__food
        print('del property')


d = Dog('二哈')
d.eat = '包子'
d.eat

del d.eat

d.eat
