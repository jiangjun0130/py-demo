from functools import reduce

list_x = [1,2,3,4,5,6,7,8]

# 连续计算，连续调用lambda
result = reduce(lambda x, y: x + y, list_x)
print(result)

# 执行过程：将上一次计算的结果作为x，后一个结果作为y。连续进行计算
# （（1+2）+3）+4...