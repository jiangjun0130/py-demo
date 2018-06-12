__author__ = 'jiangjun'
__date__ = '2018/5/27 下午8:48'


class Dog(object):
    """
    静态方法:只是名义上归类管理，实际上在静态方法里访问不了类或实例中的任何属性
    """

    def __init__(self, name):
        self.name = name

    @staticmethod
    def eat(name, food):
        print('%s is eating %s' % (name, food))


