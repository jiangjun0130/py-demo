__author__ = 'jiangjun'
__date__ = '2018/5/18 下午4:24'

#
# class Person:
#
#     sex = 'F'
#
#     mate_list = []
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return self.name + "--" + str(self.age)
#
#
# p1 = Person(name='tom', age=18)
# p1.sex = 'M'
# p1.mate_list.append('jack')
# print(p1, p1.sex, p1.mate_list)
# print(Person.mate_list)
#
#
# p2 = Person(name='lily', age=19)
# print(p2, p2.sex, p2.mate_list)
#
# print(Person.mate_list)




i = 1
print(id(i))
i +=1
print(id(i))