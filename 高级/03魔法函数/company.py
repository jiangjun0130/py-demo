__author__ = 'jiangjun'
__date__ = '2018/6/18 下午11:44'

"""
03魔法函数：以"__"开头，以"__"结尾的函数。可以增强类的特性
一定要使用python提供的魔法函数，自定义是没用的
"""


class Company(object):

    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]


company = Company(['tom', 'jim', 'cook'])

# employee = company.employee
# for em in employee:
#     print(em)

print('---直接for循环---')


for em in company:
    print(em)


print('---切片---')

company1 = company[:2]


for em in company1:
    print(em)

print('---len---')

print(len(company1))

