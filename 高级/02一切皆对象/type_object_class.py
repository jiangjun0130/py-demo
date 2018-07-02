__author__ = 'jiangjun'
__date__ = '2018/6/15 下午5:50'

a = 1
b = 'abc'
print(type(1))
print(type(int))
# <class 'int'>
# <class 'type'>

print(type(b))
print(type(str))
# <class 'str'>
# <class 'type'>

# type->int->1
# type->class->obj

# object 是顶层基类
# type也是一个类，同时type也是一个对象


class Student:
    pass


class MyStudent(Student):
    pass


stu = Student()
print(type(stu))    # <class '__main__.Student'>
print(type(Student))    # <class 'type'>

print(int.__bases__)        # (<class 'object'>,)
print(str.__bases__)        # (<class 'object'>,)
print(Student.__bases__)    # (<class 'object'>,)
print(MyStudent.__bases__)  # (<class '__main__.Student'>,)

print(type.__bases__)   # (<class 'object'>,)

print(type(object)) # <class 'type'>
