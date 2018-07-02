__author__ = 'jiangjun'
__date__ = '2018/6/23 上午9:58'

# 建议不直接继承dict

from collections import UserDict


class MyDict(UserDict):

    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)


mydict = MyDict(one=1)
print(mydict)


from collections import defaultdict # 重写了__missing__

my_dict = defaultdict(dict)
print(my_dict['a']) # {}