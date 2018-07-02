__author__ = 'jiangjun'
__date__ = '2018/6/22 下午2:28'

# try except finally


def exe_try():
    try:
        print('code started')
        raise KeyError
        return 1
    except KeyError as e:
        print('key error')
        return 2    # 将2压入栈顶
    # else:
    #     print('other error')
    finally:
        print('finally')
        return 3    # 将3压入栈顶

print(exe_try())    # 3.返回的时候从栈顶取值


# 上下文管理器协议


class Sample:
    def __enter__(self):
        # 获取资源
        print('enter...')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 释放资源
        print('exit...')

    def do_something(self):
        print('do something')


with Sample() as sample:
    sample.do_something()