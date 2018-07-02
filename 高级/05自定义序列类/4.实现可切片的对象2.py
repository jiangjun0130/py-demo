__author__ = 'jiangjun'
__date__ = '2018/6/22 下午4:08'

from _collections_abc import __all__
import numbers


class Group:

    # 支持切片操作
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        self.staffs.reverse()

    def __getitem__(self, item):
        cls = type(self)

        if isinstance(item, slice):
            # 返回group类型
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=self.staffs)
        elif isinstance(item, numbers.Integral):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=self.staffs[item])

    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs)

    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False


staffs = ['tom', 'lily', 'jack']
group = Group(group_name='管理员', company_name='阿里巴巴', staffs=staffs)
# 切片 slice
print(group[:2])
# 取值
print(group[0])

print(len(group))

if 'tom' in group:
    print('yes')
else:
    print('no')

reversed(group)

pass