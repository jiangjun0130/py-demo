__author__ = 'jiangjun'
__date__ = '2018/6/23 上午9:33'

from _collections_abc import Mapping, MutableMapping

# dict属于mapping类型

a = {}
print(isinstance(a, MutableMapping))