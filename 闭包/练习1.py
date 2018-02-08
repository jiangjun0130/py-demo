# 记录走路步数【非闭包】

# 【在代码中尽量少的使用全局变量，无法保证其他函数不会改变全局变量。导致函数没有自封闭性，非常容易受到另外函数或代码的影响。】

origin = 0 # 全局变量

def go(step):
    global origin
    new_pos = origin + step
    origin = new_pos  # 如果同名的局部变量出现在了函数内部，并且为赋值语句（局部变量被重新赋值），
                      # 此时，就不上到上一个作用域获取值。而是作为一个本地变量。就会报：local variable 'origin' referenced before assignment
                      #  解决方法：用global关键字强制将origin设置为【全局变量】
    return new_pos

print(go(2))
print(go(3))
print(go(6))