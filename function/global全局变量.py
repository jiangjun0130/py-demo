
# global关键字可以把一个局部变量变成全局变量

def demo():
    global c
    c = 2

demo()
print(c)