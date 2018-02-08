from enum import Enum
# IntEnum:枚举值只能是int类型
# unique:枚举类型的值不能重复，即不能有别名
from enum import IntEnum,unique

@unique
class VIP(Enum):
    YELLOW = 1
    YELLOW_ALIAS = 1 # 别名
    GREEN = 2
    BLACK = 3
    RED = 4

a = 1
# 获取到对应的枚举
print(VIP(a))