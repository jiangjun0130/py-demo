__author__ = 'jiangjun'
__date__ = '2018/6/22 下午5:23'


# 列表推导式
# 1.提取出1-20之间的奇数
odd_list = [i for i in range(21) if i % 2 == 1]
print(odd_list)

# 列表生成式性能高于列表操作


# 生成器表达式
odd_gen = (i for i in range(21) if i % 2 == 10)
print(type(odd_gen))   # <class 'generator'>
for item in odd_gen:
    print(item)

odd_list2 = list(odd_gen)
print(type(odd_list2))
print(odd_list2)

# 字典推导式
my_dict = {'tom1': 22, 'tom2': 23, 'tom3': 24}
reversed_dict = {value: key for key, value in my_dict.items()}
print(reversed_dict)    # {22: 'tom1', 23: 'tom2', 24: 'tom3'}

# 集合推导式
my_set = {key for key, value in my_dict.items()}
print(type(my_set)) # <class 'set'>
print(my_set)   # {'tom2', 'tom1', 'tom3'}

