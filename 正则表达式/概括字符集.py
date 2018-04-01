
# 概括字符集

# \d \D
# \w：匹配字母和数字、下划线    \W：取非单词字符(包括空格)
# \s：匹配空白字符             \S：取反
# .：匹配除换行符\n之外，其他所有字符

import re

a = 'python 1234j&ava567*go_+'

result = re.findall('[0-9]',a)
print(result) # ['1', '2', '3', '4', '5', '6', '7']

result = re.findall('[^0-9]',a)
print(result) # ['p', 'y', 't', 'h', 'o', 'n', ' ', 'j', '&', 'a', 'v', 'a', '*', 'g', 'o', '_', '+']

result = re.findall('\w',a)
print(result) # ['p', 'y', 't', 'h', 'o', 'n', '1', '2', '3', '4', 'j', 'a', 'v', 'a', '5', '6', '7', 'g', 'o', '_']

result = re.findall('\W',a)
print(result) # [' ', '&', '*', '+']


result = re.findall('\s',a)
print(result) # [' ']
