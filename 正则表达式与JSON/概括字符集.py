
# 概括字符集

# \d \D
# \w：匹配字母和数字、下划线    \W：取非单词字符(包括空格)
# \s：匹配空白字符             \S：取反

import re

a = 'python 1234j&ava567*go_+'

result = re.findall('[0-9]',a)
print(result)

result = re.findall('[^0-9]',a)
print(result)

result = re.findall('\w',a)
print(result)

result = re.findall('\W',a)
print(result)


result = re.findall('\s',a)
print(result)
