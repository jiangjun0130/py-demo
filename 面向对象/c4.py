
from c3 import Human

# 继承：先引入要继承的类，然后在类定义的括号中即可
class Student(Human):

    def __init__(self, school, name, age):
        self.school = school
        #Human.__init__(self,name,age)
        super(Student, self).__init__(name, age)

    # 如果子类有和父类一样的方法，python会优先调用子类的方法，而不会调用父类方法
    def do_homework(self):
        print('this is subclass method dohomework...')
        #super(Student,self).do_homework()