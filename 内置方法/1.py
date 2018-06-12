__author__ = 'jiangjun'
__date__ = '2018/4/26 上午11:30'

# all()会循环括号内的每一个元素，如果括号内的所有元素都是真的，或者如果iterable为空，则返回True，如果有一个为假的那么就返回False
print(all([0, 1, -5]))  # False

# 循环元素，如果有一个元素为真，那么就返回True，否则就返回False
print(any([0, 1, -5]))  # True
print(any([]))  # False


# 返回一个对象是否可以被执行
def func():
    pass


print(callable(func)) # True
print(callable(123))  # False

# compile 动态加载代码段
code = """
print('***************')
print(all([0, 1, -5])) 
print(callable(123))
print('***************')
"""

# 方法一
py_obj = compile(code, 'err.log', 'exec')
exec(py_obj)

# 方法二
exec(code)