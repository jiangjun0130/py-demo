# 记录走路步数【闭包】
# 重要：闭包的环境变量有保存现场的功能，记忆上次调用的状态。

origin = 0

def factory(pos):
    def go(step):
        nonlocal pos
        new_pos = pos + step
        pos = new_pos  # 如果同名的局部变量出现在了函数内部，并且为赋值语句（局部变量被重新赋值），
                       # 此时，就不上到上一个作用域获取值。而是作为一个本地变量。就会报：local variable 'pos' referenced before assignment
                       #  解决方法：用nonlocal关键字强制将pos设置为【环境变量】
        return pos
    return go

tourist = factory(origin)
print(tourist(2))
print(tourist(3))
print(tourist(6))