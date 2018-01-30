"""
    文档注释
"""

print('hello python!')
a = 1
b = a
a = 3
print(b)

mood = True

if mood:
    print("go to left")
    print('back away')
else:
    print("go to right")

ACCOUNT = 'jj'
PASSWORD = 'jj'

print('please input account...')
user_account = input()

print('please input password...')
user_password = input()

if user_account == ACCOUNT and user_password == PASSWORD:
    print('success...')
else:
    print('failed...')

