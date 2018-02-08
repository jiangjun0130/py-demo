# 闭包内部赋值环境变量

def f1():
    a = 10 # 局部变量
    def f2():
        #  a = 20 # 此时的a不是环境变量而是一个局部变量了，和外面的a不是一个概念了。所以此时已经不是一个闭包了。所以打印 f.__closure__ 为None
        # 所以环境变量不能变赋值，只能被【引用】
        return a
    return f2

f = f1()
print(f)
print(f.__closure__)