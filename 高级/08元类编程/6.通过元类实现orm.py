__author__ = 'jiangjun'
__date__ = '2018/7/2 下午3:37'

import numbers

class Field:
    pass


class IntField(Field):
    """
    自定义的类只需要实现以下3个方法中的一个，就是一个属性描述符.
    称为 数据描述符（Data Descriptor）
    """

    def __init__(self, db_column, min_value=None, max_value=None):
        self._value = None
        self.min_value = min_value
        self.max_value = max_value
        self.db_column = db_column
        if min_value is not None:
            if not isinstance(min_value, numbers.Integral):
                raise ValueError('min_value must be int')
            elif min_value < 0:
                raise ValueError('min_value must be positive int')

        if max_value is not None:
            if not isinstance(max_value, numbers.Integral):
                raise ValueError('max_value must be int')
            elif max_value < 0:
                raise ValueError('max_value must be positive int')

        if min_value is not None and max_value is not None:
            if min_value > max_value:
                raise ValueError('min_value must be smaller than max_value')

    def __get__(self, instance, value):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
             raise ValueError('int value need...')
        if value < self.min_value or value > self.max_value:
            raise ValueError('value must between min_value and max_value.')
        self._value = value


class CharField(Field):

    def __init__(self, db_column, max_length=None):
        self._value = None
        self.db_column = db_column

        if max_length is None:
            raise ValueError('must set max_length for charfield')

        self.max_length = max_length

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError('str value need...')
        if len(value) > self.max_length:
            raise ValueError('value length must small max_length.')
        self._value = value


class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        if name == 'BaseModel':
            return super().__new__(cls, name, bases, attrs, **kwargs)

        fields = {}
        for key, value in attrs.items():
            if isinstance(value, Field):
                fields[key] = value

        attrs_meta = attrs.get('Meta', None)
        _meta = {}
        db_table = name.lower()
        if attrs_meta is not None:
            db_table = getattr(attrs_meta, 'db_table', None)

        _meta['db_table'] = db_table
        attrs['_meta'] = _meta
        attrs['fields'] = fields
        del attrs['Meta']
        return super().__new__(cls, name, bases, attrs, **kwargs)


class BaseModel(metaclass=ModelMetaClass):

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        return super().__init__()

    def save(self):
        fields = []
        values = []
        for key, value in self.fields.items():
            db_column = value.db_column
            if not db_column:
                db_column = key.lower()
            fields.append(db_column)

            value = getattr(self, key)
            values.append(str(value))

        sql = 'insert into {db_table} ({fields}) value ({values})'.format(db_table=self._meta['db_table'],
                                                                          fields=','.join(fields),
                                                                          values=','.join(values))
        print(sql)


class User(BaseModel):
    name = CharField(db_column='', max_length=10)
    age = IntField(db_column='', min_value=0, max_value=100)

    class Meta:
        db_table = 'user'


if __name__ == '__main__':
    user = User(name='tom', age=10)
    user.save()