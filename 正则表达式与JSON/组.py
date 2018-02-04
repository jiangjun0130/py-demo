# 组：用"()"括号括起来的内容称为一组

import re

a = 'PythonJavaPythonPythonPythonPythonPython'

# 查找一组(Python）的字符重复若干次
result = re.findall('(Python){3}', a)
# 总结：()为且关系，[]为或关系
print(result)

