__author__ = 'jiangjun'
__date__ = '2018/6/19 下午2:37'


class Company(object):

    def __init__(self, employee_list):
        self.employee = employee_list

    def __str__(self):
        return ','.join(self.employee)

    # 开发模式下调用
    def __repr__(self):
        return ','.join(self.employee)


company = Company(['tom', 'jim', 'cook'])

print(company)

# 在python解释器下会调用repr
company