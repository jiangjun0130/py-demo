__author__ = 'jiangjun'
__date__ = '2018/4/15 下午11:23'

#  文件句柄
f = open('yesterday', encoding='utf-8', mode='r')

print(f.read())

f = open('yesterday2', encoding='utf-8', mode='w')

f.writelines('Hello\n')
f.writelines('JJ\n')

# append模式【不能读】
f = open('yesterday2', encoding='utf-8', mode='a')
f.writelines('Nice to meet you!')

f.close()

#  ------------------------------------------------------
f = open('yesterday', encoding='utf-8', mode='r')
# 读取单行
print(f.readline())
f.close()

#  ----------------------low loop--------------------------------
f = open('yesterday', encoding='utf-8', mode='r')

for index, line in enumerate(f.readlines()):
    if index == 9:
        print('--------------------我是分割线---------------------')
        continue
    print(line.strip())

f.close()

#  ----------------------高效率 读取大文件--------------------------------

f = open('yesterday', encoding='utf-8', mode='r')

# f被变成一个迭代器
index = 0
for line in f:
    if index == 9:
        print('--------------------我是分割线22---------------------')
        index += 1
        continue
    print(line)
    index += 1
