__author__ = 'jiangjun'
__date__ = '2018/6/24 下午11:16'

from datetime import date, datetime


class User:

    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0

    def get_age(self):
        return datetime.now().year - self.birthday.year

    # 计算属性
    # 把函数编程属性描述符
    @property
    def age(self):
        return datetime.now().year - self.birthday.year

    @age.setter
    def age(self, value):
        self._age = value


if __name__ == '__main__':
    user = User('tom', date(year=1990, month=1, day=31))
    # print(user.get_age())
    print(user.age)
    user.age = 30
    print(user._age)
