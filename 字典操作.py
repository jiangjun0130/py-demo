__author__ = 'jiangjun'
__date__ = '2018/4/15 下午4:08'

info = {
    "stu001": 'Tom',
    "stu002": 'Mike',
    'stu003': 'Lily'
}

# 查找，如果不存在，则报错
print(info['stu001'])  # Tom

# 如果不存在，则返回None
print(info.get('stu009'))

# 新增字典
info['stu004'] = 'JJ'


# python通用del
del info['stu001']

info.pop('stu002')

# 随机删除
info.popitem()


# 循环
# 建议使用
for i in info:
    print(i, info[i])


for k,v in info.items():
    print(k, v)

# 两者区别：
# 第一种高效很多。因为是通过索引取值。
# items()把一个字典变成一个列表。每个元素是一个元组。因为是把字典转换为列表，如果数据量大的话，性能将会很低。