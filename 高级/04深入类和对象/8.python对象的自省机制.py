__author__ = 'jiangjun'
__date__ = '2018/6/21 下午10:37'

# 自省是通过一定的机制查询到对象的内部结构


class Person:
    name = 'jj'


class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name


user = Student('家里蹲')
# 通过__dict__查询属性
print(user.__dict__)
print(user.name)
print(Person.__dict__)

# dir更加强大，只有属性的名称，没有属性值
print(dir(user))