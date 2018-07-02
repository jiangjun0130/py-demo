__author__ = 'jiangjun'
__date__ = '2018/6/24 下午11:27'

from datetime import date, datetime

# __getattr__、__get__attribute__
# __getattr__：在查找不到属性的时候调用
# __getattribute__：查找属性时首先进入该方法(尽量不要覆盖该方法)


class User:

    def __init__(self, name, birthday, info={}):
        self.name = name
        self.birthday = birthday
        self.info = info

    def __getattr__(self, item):
        print('not found attr...')
        return self.info[item]

    def __getattribute__(self, item):
        return 'haha'


if __name__ == '__main__':
    user = User('tom', date(year=1990, month=1, day=31), info={'company': "alibaba"})
    # print(user.age) # not found attr...
    print(user.company)