__author__ = 'jiangjun'
__date__ = '2018/7/2 上午10:43'


class User:
    def __new__(cls, *args, **kwargs):
        """
        在对象生成之前，控制对象的生成过程，并不会生成类的对象。
        如果__new__函数不返还对象，则不会调用__init__函数
        :param args:
        :param kwargs:
        :return:
        """
        print('in new')
        return super().__new__(cls)

    def __init__(self, name):
        """
        完善对象的
        :param name:
        """
        self.name = name
        print('in init')


if __name__ == '__main__':
    user = User(name='tom')