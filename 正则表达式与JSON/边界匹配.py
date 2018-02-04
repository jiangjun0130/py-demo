# 边界匹配

import re

qq = '1000000000001'

# 匹配位数为：4~8位
result = re.findall('\d{4,8}', qq)
print(result)  # ['10000000', '00001']

# 边界符匹配：以^开头，$结尾。 匹配完整的字符串，是否符合4到8位，不会进行上述匹配
result = re.findall('^\d{4,8}$', qq)
print(result)  # []

result = re.findall('000', qq)
print(result)  ['000', '000', '000']

# ^开头：表示必须以000开头
result = re.findall('^000', qq)
print(result)  # []

# $结尾：表示必须以000结尾
result = re.findall('000$', qq)
print(result)  # []