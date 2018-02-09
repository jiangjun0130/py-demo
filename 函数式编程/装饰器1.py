# 装饰器基础用法
import time

def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper

@decorator
def f1():
    print('This is f1 function')

f1()


