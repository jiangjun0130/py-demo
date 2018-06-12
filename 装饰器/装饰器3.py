__author__ = 'jiangjun'
__date__ = '2018/4/24 下午2:46'

user, pwd = 'jj', '123'


def auth(func):

    def wrapper(*args, **kwargs):
        username = input('Username:').strip()
        password = input('Password:').strip()
        if username == user and password == pwd:
            print('\033[31;1mUsername has passed authentication\033[0m')
            res = func(*args, **kwargs)
            print('after authentication')
            return res

    return wrapper


def index():
    print('this is index')


@auth
def home():
    print('this is home')
    return 'Home Page'


@auth
def bbs():
    print('this is bbs')


index()
print(home())
bbs()