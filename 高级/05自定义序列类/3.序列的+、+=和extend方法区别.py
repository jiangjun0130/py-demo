__author__ = 'jiangjun'
__date__ = '2018/6/22 下午3:55'

from _collections_abc import __all__

a = [1, 2]
b = a + [3, 4]
print(b)    # [1, 2, 3, 4]

a += [5, 6]
print(a)    # [1, 2, 5, 6]

a += (7, 8)
print(a)    # [1, 2, 5, 6, 7, 8]

# c = a + (3, 4)  # 异常：can only concatenate list (not "tuple") to list

# +=：可以为任意的序列类型。底层调用了__iadd__魔法函数

a.extend(range(3))
print(a)    # [1, 2, 5, 6, 7, 8, 0, 1, 2]

a.append([9, 10])   # append函数将参数作为一个值传入数组
print(a)    # [1, 2, 5, 6, 7, 8, 0, 1, 2, [9, 10]]

a.append((9, 10))   # append函数将参数作为一个值传入数组
print(a)    # [1, 2, 5, 6, 7, 8, 0, 1, 2, [9, 10], (9, 10)]
