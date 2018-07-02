__author__ = 'jiangjun'
__date__ = '2018/6/24 下午9:49'


class Company:

    def __init__(self, name, staffs=[]):
        self.name = name
        self.staffs = staffs

    def add(self, staff_name):
        self.staffs.append(staff_name)

    def remove(self, staff_name):
        self.staffs.remove(staff_name)


com1 = Company('com1', ['tom1', 'tom2'])
com1.add('tom3')
com1.remove('tom1')
print(com1.staffs)  # ['tom2', 'tom3']


com2 = Company('com2')
com2.add('tom4')
print(com2.staffs)  # ['tom4']

com3 = Company('com3')
com3.add('tom5')
print(com2.staffs)  # ['tom4', 'tom5']

print(com3.staffs)  # ['tom4', 'tom5']

print(com3.staffs is com2.staffs)   # True

# 现象：com2和com3的staffs list为同一对象

# 原因：
    # 1：init函数默认staffs=[]，为空列表函数。com2和com3创建对象时，采用了默认的staffs空list
    # 2：list是可变对象
    # 3：所以com2和com3共用了一个list对象

# 结论：尽量不要采用list类型传递参数，或者要知道传递时候应该知道会被修改


def add(a, b):
    a += b
    return a


a = [1, 2]
b = [3, 4]

c = add(a, b)
print(c)    # [1, 2, 3, 4]

print(a)    # [1, 2, 3, 4]

print(b)    # [3, 4]


a = (1, 2)
b = (3, 4)

c = add(a, b)
print(c)    # (1, 2, 3, 4)

print(a)    # (1, 2)

print(b)    # (3, 4)
