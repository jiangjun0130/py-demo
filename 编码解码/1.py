__author__ = 'jiangjun'
__date__ = '2018/4/23 下午2:10'

import sys

# 字符串通过编码转换为字节码，字节码通过解码转换为字符串
# str--->(encode)--->bytes，bytes--->(decode)--->str

s = '你好'
s_to_unicode = s.encode('utf-8')
print(s_to_unicode)  # b'\xe4\xbd\xa0\xe5\xa5\xbd'
# s_to_gbk = s.decode('utf-8')

s_decode = s_to_unicode.decode('utf-8')
print(type(s_decode))  # <class 'str'>
print(s_decode)  # 你好

# 编码utf-8为什么不是decode转成unicode
# 因为python3默认就是【unicode】，utf-8可以看成是unicode的一个扩展集，所以其实name本身是一个unicode编码的，
# 所以可以通过encode编码成utf-8

# utf-8编码格式和gbk编码格式互转

name = '小明'
name1 = name.encode('utf-8')
name2 = name1.decode('utf-8')
name3 = name2.encode('gbk')
name4 = name3.decode('gbk')

print(type(name3))  # <class 'bytes'>
print(name3)  # b'\xd0\xa1\xc3\xf7'

print(type(name4))  # <class 'str'>
print(name4)  # 小明

# 从上面可以卡出name2本来是解码成utf-8的，后来有队name2进行了gbk编码，接着又再次对name3进行gbk解码
# 所以不难看出，其实utf-8和gbk之间都是通过unicode来做一个中间转换的操作
