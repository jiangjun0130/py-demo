__author__ = 'jiangjun'
__date__ = '2018/6/24 下午11:39'


from datetime import date, datetime
import numbers

"""
属性描述符：可以控制属性复制时的一些行为。如参数校验等
"""


class IntField(object):
    """
    自定义的类只需要实现以下3个方法中的一个，就是一个属性描述符.
    称为 数据属性描述符（Data Descriptor）
    """
    def __get__(self, instance, value):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
             raise ValueError('int value need...')
        if value < 0:
            raise ValueError('value invalid...')
        self.value = value

    def __delete__(self, instance):
        pass


class NonDataIntField:
    """
    非数据属性描述符
    """
    def __get__(self, instance, value):
        return self.value


class User:

    age = IntField()
    name = NonDataIntField()

if __name__ == '__main__':
    user = User()
    # print(user.get_age())

    # user.age = 'axx'
    # print(user.age) # ValueError: int value need...
    user.age = 28
    print(user.__dict__)    # {}    # 如果属性是数据属性描述符，则会进入属性描述符中，不会进入对象中

    user.name = 'tom'
    print(user.__dict__)    # {'name': 'tom'}      # 如果属性是非数据属性描述符，则会进入对象中

    print(getattr(user, 'age'))  # 28


'''
如果user是某个类的实例，那么user.age（以及等价的getattr(user,’age’)）
首先调用__getattribute__。如果类定义了__getattr__方法，
那么在__getattribute__抛出 AttributeError 的时候就会调用到__getattr__，
而对于描述符(__get__）的调用，则是发生在__getattribute__内部的。
user = User(), 那么user.age 顺序如下：

（1）如果“age”是出现在User或其基类的__dict__中， 且age是data descriptor， 那么调用其__get__方法, 否则

（2）如果“age”出现在user对象的__dict__中， 那么直接返回 obj.__dict__[‘age’]， 否则

（3）如果“age”出现在User或其基类的__dict__中

（3.1）如果age是non-data descriptor，那么调用其__get__方法， 否则

（3.2）返回 __dict__[‘age’]

（4）如果User有__getattr__方法，调用__getattr__方法，否则

（5）抛出AttributeError

'''