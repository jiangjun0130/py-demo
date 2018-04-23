__author__ = 'jiangjun'
__date__ = '2018/4/15 下午2:13'

name = 'my name is tom'
print(name.capitalize())  # My name is tom

print(name.count('a'))  # 1

print(name.center(50, '-'))  # ------------------my name is tom------------------
print(name.ljust(50, '-'))   # my name is tom------------------------------------
print(name.rjust(50, '-'))   # ------------------------------------my name is tom


print(name.endswith('m'))  # True


name = 'my name is {name} and {years} old'
print(name.format(name='jack', years=18))  # my name is jack and 18 old

print(name.format_map({'name': 'Luci', 'years': 20}))  # my name is Luci and 20 old

print('+'.join(['1', '2', '3', '4']))  # 1+2+3+4

print('Tom'.lower())  # tom
print('tom'.upper())  # TOM

# 去除左边的空格回车
print('\nHello'.lstrip())  # Hello
# 去除又边的空格回车
print('Hello\n'.rstrip())  # Hello
# 去除左右两边的空格回车
print('\nHello  Haha\n'.strip())
