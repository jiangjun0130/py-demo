__author__ = 'jiangjun'
__date__ = '2018/4/15 下午11:23'

#  光标
f = open('yesterday', encoding='utf-8', mode='r')

print(f.readline())
print(f.readline())
print(f.readline())
print(f.tell())
print(f.seek(0)) # 回到开始

print(f.tell()) # 打印当前位置
print(f.readline())