__author__ = 'jiangjun'
__date__ = '2018/6/3 下午11:53'

from 异常.MyException import MyException

try:
    raise MyException('我的异常')
except MyException as e:
    print(e.message)