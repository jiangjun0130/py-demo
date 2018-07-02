__author__ = 'jiangjun'
__date__ = '2018/6/20 下午11:31'

# 结论：使用isinstance判断对象的类型，而不是使用type


class A:
    pass


class B(A):
    pass


b = B()

print(isinstance(b, B)) # True
print(isinstance(b, A)) # True

print(type(b) is B) # True
print(type(b) is A) # False