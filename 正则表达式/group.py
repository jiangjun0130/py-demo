import re

s = 'life is short,i use python'

result = re.search('life(.*)python', s)
# group(0):返回的是匹配的完整结果
print(result.group(0))  # life is short,i use python

# group(1):返回的是完整匹配结果内部的分组
print(result.group(1))  #  is short,i use

result = re.findall('life(.*)python', s)
print(result)  # [' is short,i use ']

s = 'life is short,i use python, i love python'

result = re.search('life(.*)python(.*)python', s)
print(result.group(0))  # life is short,i use python, i love python
print(result.group(1))  #  is short,i use
print(result.group(2))  # , i love
#print(result.group(0,1,2))
# 返回了group(1)、group(2)
print(result.groups())  # (' is short,i use ', ', i love ')