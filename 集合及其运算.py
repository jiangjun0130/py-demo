__author__ = 'jiangjun'
__date__ = '2018/4/15 下午10:37'

list_1 = [1, 4, 5, 7, 4, 8, 10, 8]

set_1 = set(list_1)

# 列表去重，可以转换为set
print(set_1, type(set_1))  # {1, 4, 5, 7, 8, 10} <class 'set'>


set_2 = set([2, 6, 0, 66, 22, 8, 4])

# 集合：求交集
print(set_1.intersection(set_2))  # {8, 4}

# 集合：求并集
print(set_1.union(set_2))  # {0, 1, 2, 66, 4, 5, 6, 7, 8, 10, 22}

# 集合：求差集
print(set_1.difference(set_2))  # {1, 10, 5, 7}

# 集合：求对称差集
print(set_1.symmetric_difference(set_2))  # {0, 1, 2, 66, 5, 6, 7, 10, 22}

# 集合：求子集
print(set_1.issubset(set_2))  # False
print(set_1.issuperset(set_2))


# 交集
print(set_1 & set_2)  # {8, 4}

# 并集
print(set_1 | set_2)  # {0, 1, 2, 66, 4, 5, 6, 7, 8, 10, 22}

# 差集
print(set_1 - set_2)  # {1, 10, 5, 7}

# 对称差集
print(set_1 ^ set_2)  # {0, 1, 2, 66, 5, 6, 7, 10, 22}


# 新增操作
set_1.add(999)
print(set_1)

# 新增多项
set_1.update([888, 777, 555])

# 删除
set_1.remove(1)
print(set_1)
