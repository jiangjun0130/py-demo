__author__ = 'jiangjun'
__date__ = '2018/6/3 下午10:13'


def talk(self):
    print('%s is yelling...' % self.name)

class Dog(object):

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print('%s is eating %s' % (self.name, food))


dog = Dog(name='二哈')
# func_name = input('>>:').strip()
#
# if hasattr(dog, func_name):
#     func = getattr(dog, func_name)
#     func(food='狗粮')
# else:
#     setattr(dog, func_name, talk)
#     dog.talk(dog)

print(dog.__class__)
print(dog.name)