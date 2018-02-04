import pack.p1 as p1

# 导入__init__.py模块时，直接引用包名即可
import pack as p

# 导入模块第二种方法，导入具体的变量，也可以导入一个模块。直接使用即可。
from pack.p1 import b

# 导入模块所有的变量，不推荐使用，引入不明确
from pack2.p1 import *


# 引入__init__.py模块变量
print(p.aa)

print(b)

print(p1)
