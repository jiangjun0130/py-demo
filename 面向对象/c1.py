
class Student():
    # 【类变量】
    sum = 0

    # 构造函数（特殊的实例方法）
    def __init__(self, name, age):
        # 【实例变量】
        # 在【实例方法】中操作【实例变量】
        self.name = name
        self.age = age
        # 申明私有实例变量，则在变量名前加2个下划线
        self.__score = 0
        # 在【实例方法】中操作【类变量】
        self.__class__.sum += 1
        print('总人数：' + str(self.__class__.sum))

    # 实例方法：self代表的是实例本身
    def do_homework(self):
        print('dohomework...')

    def marking(self, score):
        self.__score = score
        print(self.name + '同学考试得分：' + str(self.__score))

    # 类方法：cls代表的是类本身
    @classmethod
    def plus_sum(cls):
        # 【类方法】中操作【类变量】
        cls.sum += 1
        #print(cls.sum)
        #print(name)

    # 静态方法：建议不要经常使用。和面向对象关联较弱
    @staticmethod
    def add(x, y):
        # 静态方法访问【类变量】
        #print('static method:' + str(Student.sum))
        #print(name)
        pass


# 定义和调用类不建议在同一个模块中
#student = Student()
#student.do_homework()


# 方法和函数的区别

# 方法：设计层面
# 函数：程序运行、过程式的一种称谓

# 变量和数据成员的区别

# 变量：在模块中声明
# 数据成员：在类中声明的变量