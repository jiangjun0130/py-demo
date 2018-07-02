__author__ = 'jiangjun'
__date__ = '2018/6/19 下午11:01'

# 鸭子类型和魔法函数构成了python语言的基础，也就是python语言的一种协议
# python本身不是通过继承一个类或者实现某一个接口，就具有某些特性。
# 而是只需要实现指定的魔法函数，就是某种类型的对象。


# 检查某个类是否有某种方法

class Company(object):

    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)


company = Company(['tom', 'jim', 'cook'])
# print(len(company))
# print(hasattr(company, '__len__'))

# 在某些情况下，希望判定某得对象的类型
from collections.abc import Sized
print(isinstance(company, Sized))


# 如何模拟一个抽象基类

class CacheBase1():
    """
    需要强制某个子类必须实现某些方法
    """

    def get(self, key):
        raise NotImplementedError

    def set(self, key, value):
        raise NotImplementedError


class RedisCache1(CacheBase1):
    pass

# 初始化的时候不会报错，只有在调用方法时才会抛出异常
#redis_cache = RedisCache1()
#redis_cache.set('key', 'value')


##################引入abc模块，设置metaclass后，
# 如果没有实现父类函数，在对象初始化时就会抛出异常################################

import abc


class CacheBase2(metaclass=abc.ABCMeta):
    """
    需要强制某个子类必须实现某些方法
    """
    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass

    def test(self):
        print('test...')


class RedisCache2(CacheBase2):
    def get(self, key):
        pass

    def set(self, key, value):
        pass

# 初始化抛出异常
redis_cache2 = RedisCache2()
redis_cache2.test()
