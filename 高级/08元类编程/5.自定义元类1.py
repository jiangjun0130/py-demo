__author__ = 'jiangjun'
__date__ = '2018/7/2 上午10:59'


def create_class(name):
    if name == 'user':
        class User:
            def __str__(self):
                return 'user'
        return User
    elif name == 'company':
        class Company:
            def __str__(self):
                return 'company'
        return Company


def say(self):
    return 'I am user'


class BaseClass:
    def answer(self):
        return 'I am base class'


if __name__ == '__main__':
    # MyClass = create_class('user')
    # my_obj = MyClass()
    # print(my_obj)

    # 动态创建类【一般开发中很少这样用】
    User = type('User', (), {'name': 'user', 'say': say})
    my_obj = User()
    print(my_obj.name)  # useranswer
    print(my_obj.say())     # I am user

    # 动态创建类并指定基类【一般开发中很少这样用】
    User2 = type('User', (BaseClass,), {'name': 'user', 'say': say})
    my_obj = User2()
    print(my_obj.answer())  # I am base class

