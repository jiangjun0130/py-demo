import re

a = 'C0C++3Java9C#5Python2Go'

# print(a.index('Python') > -1)
# print('Python' in a)
result = re.findall('Python', a)
if len(result) > 0:
    print('contains str')
else:
    print('not contains str')

# 找出a字符串的所有数字
result = re.findall('\d',a)
print(result)

s = 'abc, acc, afc, abc, abc'
# 找出每个单词中间为c或f的单词
result = re.findall('a[cf]c', s)
print(result)
# 取反操作
result = re.findall('a[^cf]c', s)
print(result)

# 找出每个单词中间为c-f之间的单词
result = re.findall('a[c-f]c', s)
print(result)