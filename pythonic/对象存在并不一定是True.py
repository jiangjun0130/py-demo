
a = ''
b = False
c = []

print(a == None)  # False
print(b == None)  # False
print(c == None)  # False

if a:
    print('不为空串')
else:
    print('空串')

# if逻辑判断时，所有对象和True、False有对应关系
# 如：''，[] 均为False
# 但是None：永远是False

# __len__、__bool__将影响对象bool的取值。如果重写了__bool__方法，则__len__方法将不会被调用。
class Test():
    def __len__(self):
        return 0

    def __bool__(self):
        return True

test = Test()
print(bool(test))