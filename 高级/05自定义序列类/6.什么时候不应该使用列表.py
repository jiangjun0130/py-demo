__author__ = 'jiangjun'
__date__ = '2018/6/22 下午5:14'

# array, deque
# 数组

import array
# array和list的区别：
# array只能存放指定的数据类型

my_array = array.array('i')
my_array.append(1)
my_array.append('abnc') # TypeError: an integer is required (got type str)
