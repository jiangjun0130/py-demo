__author__ = 'jiangjun'
__date__ = '2018/4/15 下午11:23'

#  读写
f = open('yesterday2', encoding='utf-8', mode='r+')

print(f.readline())
print(f.readline())
print(f.readline())
print(f.tell())
print(f.writelines('-------------Nice-------------')) # 回到开始
f.close()



# 写读【很少用】
# f = open('yesterday2', encoding='utf-8', mode='w+')
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.tell())
# print(f.writelines('-------------Nice2-------------')) # 回到开始


# 追加读写
f = open('yesterday2', encoding='utf-8', mode='a+')
f.writelines('Nice to meet you!')