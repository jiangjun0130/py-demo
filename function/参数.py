# 参数：
# 1：必须参数
# 2：关键字参数
# 3：默认参数
# 4：可变参数


def add(x, y):
    # 形参
    result = x + y
    return result


c = add(1, 2)  # 实参
print(c)

# 关键字参数 优点：代码的可读性
d = add(y=2, x=1)
print(d)


# 声明默认参数
def print_student_files(name, gender='男', age=18, college='人名路小学'):
    print('我叫' + name)
    print('今年' + str(age) + '岁')
    print('我是' + gender + '生')
    print('我在' + college + '上学')

print_student_files('JJ', '男', 18, '人名路小学')

# 使用默认参数调用
print_student_files('Tim')
# 改变默认值
print_student_files('Kitty', '女', 16)

# 改变部分默认值，需要用关键字参数形式
print_student_files('Jason', college='近城镇小学')

# 可变参数
def demo(*param):
    print(param)
    print(type(param))

# 调用方式一
demo(1,2,3,4,5,6)
# (1, 2, 3, 4, 5, 6)
# <class 'tuple'>

# 调用方式二
a = (1,2,3,4,5,6)
demo(*a)
# (1, 2, 3, 4, 5, 6)
# <class 'tuple'>

# 可变参数与必须参数、默认参数一起运用时，需要将默认参数放到最后
def demo2(param1, *param3, param2=2):
    print(param1)
    print(param2)
    print(param3)

demo2('1',1,2,3,param2=22)
#  1
#  22
#  (1, 2, 3)

# 可变关键字参数列表
# param 类型为dict
def city_temperature(**param):
    print(param)
    print(type(param))  # <class 'dict'>
    for key, value in param.items():
        print(key, ':', value)

# 调用方式一
city_temperature(bj='32',xm='23', sh='31')

# 调用方式二，传入dict参数
a = {'bj':'32c','xm':"34",'sh':'22'}
city_temperature(**a)