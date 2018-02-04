#  只有在文件夹下新建一个__init__.py的文件，python就会认为这个文件夹是一个包。
#  __init__.py也是一个模块。模块名称为包名即可。
# 在导入模块的时候，python会首先执行包下的__init__.py

# __all__作用，导入包时，允许哪些模块被导入
#__all__ = ['p1']

aa = "this is init module"

x = "This is __init__.py file"

print(x)
