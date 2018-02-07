# 数量词
# *：匹配0次或无限次
# +：匹配1次或无限次
# ？：匹配0次或1次

import re

a = 'python 1111 java  789 php'

# 贪婪匹配
result = re.findall('[a-z]{3,6}',a)
print(result)
#  ['python', 'java', 'php']

# 非贪婪匹配:?
result = re.findall('[a-z]{3,6}?',a)
#  ['pyt', 'hon', 'jav', 'php']
print(result)

b = 'pytho0python1pythonn2'

result = re.findall('python*',b)
print(result)
#  ['pytho', 'python', 'pythonn']

result = re.findall('python+',b)
print(result)
#  ['python', 'pythonn']

result = re.findall('python?',b)
print(result)
#  ['pytho', 'python', 'python']
