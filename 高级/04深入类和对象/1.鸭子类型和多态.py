__author__ = 'jiangjun'
__date__ = '2018/6/19 下午10:37'


class Cat(object):
    def say(self):
        print('I am a cat')


class Dog(object):
    def say(self):
        print('I am a dog')


class Duck(object):
    def say(self):
        print('I am a duck')


animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()