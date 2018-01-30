
print('基础用法\r\n')
for x in range(0, 10):
    print(x)

print('递增\r\n')
for x in range(0, 10, 2):
    print(x, end=' | ')

print('递减\r\n')
for x in range(10, 0, -2):
    print(x, end=' | ')

print('\n')
#  打印奇数位元素
# 方法一：for循环
a = [1, 2, 3, 4, 5, 6, 7, 8]
print('打印奇数位元素，方法一：for循环\r\n')
for i in range(0, len(a), 2):
    print(a[i], end='|')
print('\n')
# 方法二：切片
print('打印奇数位元素，方法二：切片\r\n')
b = a[0:len(a):2]
print(b)
