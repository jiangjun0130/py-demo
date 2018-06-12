__author__ = 'jiangjun'
__date__ = '2018/5/24 下午10:37'

class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError()

    @staticmethod
    def animal_talk(obj):
        obj.talk()


class Cat(Animal):

    def talk(self):
        print('I am a cat')


class Dog(Animal):

    def talk(self):
        print('I am a dog')

cat = Cat(name='tom')

dog = Dog(name='taidi')

Animal.animal_talk(cat)

Animal.animal_talk(dog)