__author__ = 'jiangjun'
__date__ = '2018/6/21 下午10:04'


class Date:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return '{year}/{month}/{day}'.format(year=self.year,
                                             month=self.month,
                                             day=self.day)

    def tomorrow(self):
        self.day += 1

    # 静态方法的缺点：返回的Date是硬编码
    @staticmethod
    def parse_from_str(date_str):
        year, month, day = tuple(date_str.split('-'))
        return Date(int(year), int(month), int(day))

    # 如果方法返回与类型无关，则可以使用
    @staticmethod
    def valid_date_str(date_str):
        year, month, day = tuple(date_str.split('-'))
        if int(year) > 0 and (int(month) > 0 and int(month) <= 12) and (int(day) > 0 and int(day) <= 31):
            return True
        else:
            return False

    @classmethod
    def from_str(cls, date_str):
        year, month, day = tuple(date_str.split('-'))
        return cls(int(year), int(month), int(day))


date = Date(2018, 6, 21)
print(date)

date.tomorrow()
print(date)

# 用staticmethod完成初始化
new_day = Date.parse_from_str('2018-6-22')
print(new_day)

# 用classmethod完成初始化
new_day2 = Date.from_str('2018-6-23')
print(new_day2)

print(Date.valid_date_str('2018-6-232'))