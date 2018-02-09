# 过滤元素
list_x = [1,0,1,0,1,0,1,0]

# 过滤非0数字
result = filter(lambda x: True if x == 1 else False, list_x)
print(list(result))

list_u = ['a','X','h','C']

# 过滤小写
result = filter(lambda x:  x.isupper(), list_u)
print(list(result))