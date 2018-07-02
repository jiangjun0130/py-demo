__author__ = 'jiangjun'
__date__ = '2018/6/22 下午3:25'

import contextlib


@contextlib.contextmanager
def file_open(file_name):
    print('file open...')
    yield {}
    print('file end')


with file_open('test.txt') as f_opend:
    print('file processing...')