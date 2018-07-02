__author__ = 'jiangjun'
__date__ = '2018/6/23 上午9:38'

a = {'tom1': {'company': 'alibaba'}, 'tom2': {'company': 'alibaba'}, }

# clear:清空字典
# a.clear()
# print(a)

# copy：浅拷贝
# new_dict = a.copy()
# new_dict['tom1']['company'] = 'baidu'
# print(new_dict)
# print(a)


# 深拷贝
import copy
new_dict = copy.deepcopy(a)
new_dict['tom1']['company'] = 'baidu'
print(new_dict) # {'tom1': {'company': 'baidu'}, 'tom2': {'company': 'alibaba'}}

print(a)    # {'tom1': {'company': 'alibaba'}, 'tom2': {'company': 'alibaba'}}

# fromkeys:将一个可迭代的对象转换为dict
new_list = ['tom1', 'tom2']

new_dict = dict.fromkeys(new_list, {'company':'alibaba'})
print(new_dict) # {'tom1': {'company': 'alibaba'}, 'tom2': {'company': 'alibaba'}}


# setdefault: 如果没有取到对应key的值，则设置默认值之后返回 D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
default_value = new_dict.setdefault('tom3', {'company': 'tencent'})
print(default_value)    # {'company': 'tencent'}
print(new_dict) # {'tom1': {'company': 'alibaba'}, 'tom2': {'company': 'alibaba'}, 'tom3': {'company': 'tencent'}}

# update: 将2个Iterable合并
new_dict.update({'tom4': {'company': 'didi'}})
print(new_dict) # {'tom1': {'company': 'alibaba'}, 'tom2': {'company': 'alibaba'}, 'tom3': {'company': 'tencent'}, 'tom4': {'company': 'didi'}}

new_dict.update(tom5='google', tom6='microsoft')
print(new_dict) # {'tom1': {'company': 'alibaba'}, 'tom2': {'company': 'alibaba'}, 'tom3': {'company': 'tencent'}, 'tom4': {'company': 'didi'}, 'tom5': 'google', 'tom6': 'microsoft'}