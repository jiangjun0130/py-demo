import re

language = 'javacPython\ngo'

result = re.findall('python', language)
print(result)  # []

# re.I：忽略大小写import re

language = 'javacPython\ngo'

result = re.findall('python', language)
print(result)  # []

# re.I：忽略大小写
# re.S：匹配所有的字符，包括换行符
result = re.findall('python.{1}', language, re.I | re.S)
print(result)  # ['Python']
# re.S：匹配所有的字符，包括换行符
result = re.findall('python.{1}', language, re.I | re.S)
print(result)  # ['Python']