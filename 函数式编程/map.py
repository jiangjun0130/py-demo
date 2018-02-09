# 推荐多使用
# 求一个数组的平方运算

list_x = [1,2,3,4,5,6,7,8]

def square(x):
    return x**2

# 进化1
#for x in list_x:
#    print(square(x))

# 进化2
result = map(square, list_x)
print(list(result))

# 进化3
result = map(lambda x: x**2, list_x)
print(list(result))

# 进化4
list_y = [1,2,3,4,5,6,7,8]
result = map(lambda x, y: x**2+y, list_x, list_y)
print(list(result))