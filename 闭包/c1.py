# 闭包 = 函数 + 环境变量
# 闭包的意义：保存的是函数当时调用的【现场】

def curve_pre():
    a = 25 # 环境变量
    def curve(x):
        return a * x * x # a的取值会优先取环境变量
    return curve # 此时，返回的不仅仅是curve函数，还有环境变量

a = 10 # 全局变量。如果把环境变量注释以后，打印结果为：40.此时就不是一个闭包。因为读取的是全局变量
f = curve_pre()
print(f.__closure__) # 闭包的环境变量保存在内置变量__closure__中
print(f.__closure__[0].cell_contents) # 25 [环境变量]
print(f(2)) # 100
print(f(2)) # 100