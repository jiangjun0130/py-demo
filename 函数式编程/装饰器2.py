# 装饰器可变参数
import time

def decorator(func):
    # *args：可变参数
    # **kw：字典类型
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)
    return wrapper

# 一个参数
@decorator
def f1(func_name):
    print('This is f1 function named ' + func_name)

# 两个参数
@decorator
def f2(func_name1, func_name2):
    print('This is f1 function named ' + func_name1)
    print('This is f1 function named ' + func_name2)

# 多个参数，有字典类型
@decorator
def f3(func_name1, func_name2, **kw):
    print('This is f1 function named ' + func_name1)
    print('This is f1 function named ' + func_name2)
    print(kw)

f1('test')
f2('name1','name2')
f3('name1','name2', a=1,b=2,c='123')