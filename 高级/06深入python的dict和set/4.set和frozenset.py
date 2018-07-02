__author__ = 'jiangjun'
__date__ = '2018/6/23 上午10:14'

# set集合 frozenset（不可变）
# 无需，不重复

s = set('abcde')

print(s)    # {'e', 'b', 'c', 'd', 'a'}
s = set(['a', 'b', 'c', 'd', 'e'])
print(s)    # {'e', 'b', 'c', 'd', 'a'}


# frozenset 可以作为dict的key
fs = frozenset('abcde')
print(fs)   # frozenset({'a', 'b', 'e', 'd', 'c'})


# 向set添加数据

s.add('f')

# update 合并2个set
s2 = set('xyz')
s.update(s2)
print(s)