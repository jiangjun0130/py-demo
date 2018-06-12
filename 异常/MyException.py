__author__ = 'jiangjun'
__date__ = '2018/6/3 下午11:52'


class MyException(Exception):

    def __init__(self, msg):
        self.message = msg
    # def __str__(self):
    #     return self.message