__author__ = 'jiangjun'
__date__ = '2018/6/22 下午4:52'

import bisect

# 用来处理已排序的序列，用来维持已排序的序列，升序
# 二分查找

inter_list = []
bisect.insort(inter_list, 3)
bisect.insort(inter_list, 2)
bisect.insort(inter_list, 5)
bisect.insort(inter_list, 1)
bisect.insort(inter_list, 6)
print(inter_list)   # [1, 2, 3, 5, 6]

print(bisect.bisect(inter_list, 3)) # 3
print(bisect.bisect_left(inter_list, 3))    # 2