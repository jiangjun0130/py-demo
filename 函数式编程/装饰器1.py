# 装饰器基础用法
import time
from functools import wraps

def decorator(func):

    # wraps注解作用：解决在引入装饰器以后，原函数的name、doc等属性被更改。
    @wraps(func)
    def wrapper():
        print(time.time())
        func()
    return wrapper

@decorator
def f1():
    print('This is f1 function')

f1()

print(f1.__name__)  # wrapper

