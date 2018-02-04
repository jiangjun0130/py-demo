c = 1

def func1():
    c = 2
    def func2():
        c = 3
        print(c)
    func2()

# 作用域链
func1()