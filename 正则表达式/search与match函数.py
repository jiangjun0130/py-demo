import re

s = 'A8C3721D86'


result = re.sub('\d', get_number, s)
print(result)