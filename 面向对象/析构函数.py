__author__ = 'jiangjun'
__date__ = '2018/5/18 下午5:15'

# 析构函数：在实例释放、x销毁的时候执行。通常用于做一些收尾工作，如关闭数据库连接、关闭打开的临时文件


class Person:

    sex = 'F'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("%s 销毁...释放资源...", self.name)

    def __str__(self):
        return self.name + "--" + str(self.age)


p1 = Person(name='tom', age=18)

print(p1, p1.sex)

del p1

p2 = Person(name='lily', age=19)
print(p2, p2.sex)