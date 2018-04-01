import re

language = 'javac++Pythongo'

# 将c++替换为kotlin
result = re.sub('c\+\+', 'Kotlin', language)
print(result) # javaKotlinPythongo

def convert(value):
    matched = value.group()
    return '!!' + matched + '!!'

result = re.sub('c\+\+', convert, language)
print(result) # java!!c++!!Pythongo

# 找出所有的数字，如果大于6则替换为9，小于6则替换为0
s = 'A8C3721D86'

def get_number(value):
    matched = value.group()
    if int(matched) >= 6:
        return '9'
    else:
        return '0'

result = re.sub('\d', get_number, s)
print(result) # A9C0900D99