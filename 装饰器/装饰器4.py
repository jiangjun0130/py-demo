__author__ = 'jiangjun'
__date__ = '2018/4/24 下午2:46'

# 装饰器新增参数
user, pwd = 'jj', '123'


def auth(auth_type):
    print('auth_type:', auth_type)

    def outer_wrapper(func):

        def wrapper(*args, **kwargs):
            print('wrapper func args', *args, **kwargs)
            if auth_type == 'local':
                username = input('Username:').strip()
                password = input('Password:').strip()
                if username == user and password == pwd:
                    print('\033[31;1mUsername has passed authentication\033[0m')
                    res = func(*args, **kwargs)
                    print('after authentication')
                    return res
                else:
                    exit('\033[31;1mInvalid username or password\033[0m')
            elif auth_type == 'ldap':
                print('this is ldap authentication')
            return wrapper

        return outer_wrapper


def index():
    print('this is index')


@auth(auth_type='local')
def home():
    print('this is home')
    return 'Home Page'


@auth(auth_type='ldap')
def bbs():
    print('this is bbs')


index()
print(home())
bbs()