from c1 import Student

student = Student('JJ', 18)
#student.do_homework()
Student.plus_sum()
student.plus_sum()
# 如果在构造函数中，没有对属性进行初始化，并且当属性有默认值时，如果在【实例方法】调用中，没有获取到变量值时，则会到类作用域中获取对应的属性值。
# 如果是在【类方法】中，则不会到类作用域中获取对应的属性值。
print(student.name)

#print(student.__dict__)
#print(Student.__dict__)

#Student.add(1,2)

student.marking(59)

# 在这里能设置__score，不是因为设置的私有属性没有生效。而是因为Python是动态语言的特性，在这里时实际上是给student实例，新增了一个__score实例变量
student.__score = -1
print(student.__score)
# {'name': 'JJ', 'age': 18, '_Student__score': 59, '__score': -1}
# 从上面可以分析出：Python会把私有变量重新命名为：_[类名][变量名]。所以在以申明的名称访问时，会报错。
print(student.__dict__)

# 验证上述说明：会进行报错。'Student' object has no attribute '__score'
#student2 = Student('Tim',18)
#print(student2.__score)