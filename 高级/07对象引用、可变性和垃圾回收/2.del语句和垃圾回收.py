__author__ = 'jiangjun'
__date__ = '2018/6/24 下午9:33'


# python中垃圾回收的算法是采用 引用计数
# 引用计数减为0时, python解释器就会将对象回收

a = object()
b = a

del a   # 计数-1
print(b)    # <object object at 0x101ba5100>

print(a)    # NameError: name 'a' is not defined


class A:
    def __del__(self):
        pass