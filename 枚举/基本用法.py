
from enum import Enum

class VIP(Enum):
    YELLOW = 1
    YELLOW_ALIAS = 1 # 别名
    GREEN = 2
    BLACK = 3
    RED = 4

for v in VIP:
    print(v)

for v in VIP.__members__:
    print(v)

for v in VIP.__members__.items():
    print(v)