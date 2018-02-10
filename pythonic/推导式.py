# 列表推导式

a = [1,2,3,4,5,6,7,8]

b = [i**2 for i in a]
print(b)  # [1, 4, 9, 16, 25, 36, 49, 64]

b = [i**2 for i in a if i >= 5]
print(b)  # [25, 36, 49, 64]

# 集合推导式

a = {1,2,3,4,5,6,7,8}

b = {i**2 for i in a}
print(b)  # {64, 1, 4, 36, 9, 16, 49, 25}

b = {i**2 for i in a if i >= 5}
print(b)  # {64, 25, 36, 49}

# 字典推导式
students = {'张三': 18, '李四': 19, '王五': 20}
# 提取key
b = [key for key,value in students.items()]
print(b)  # ['张三', '李四', '王五']

# key、value颠倒
b = {value:key for key,value in students.items()}
print(b)  # {18: '张三', 19: '李四', 20: '王五'}