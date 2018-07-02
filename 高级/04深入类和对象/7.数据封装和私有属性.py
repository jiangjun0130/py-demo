__author__ = 'jiangjun'
__date__ = '2018/6/21 下午10:24'


class Date:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return '{year}/{month}/{day}'.format(year=self.year,
                                             month=self.month,
                                             day=self.day)


class User:
    def __init__(self, birthday):
        self.__birthday = birthday

    def get_age(self):
        return 2018 - self.__birthday.year


user = User(Date(1990, 1, 30))
# print(user.birthday)
# 私有属性被改写为如下格式
print(user._User__birthday)
print(user.get_age())