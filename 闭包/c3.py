# 闭包内部赋值环境变量

def f1():
    a = 10
    def f2():
        a = 20
        print('1:' + str(a))
    print('2:' + str(a))
    f2()
    print('3:' + str(a))

f1()