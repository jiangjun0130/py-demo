__author__ = 'jiangjun'
__date__ = '2018/5/14 下午11:52'

import shutil

f1 = open('readme.txt', 'r', encoding='utf-8')

f2 = open('test.txt', 'w', encoding='utf-8')

shutil.copyfileobj(f1, f2)

shutil.copyfile("readme.txt", "test2.txt")

# 拷贝文件和权限
# shutil.copy()

# shutil.copy()

# 递归拷贝
# shutil.copytree()

# 递归删除
# shutil.rmtree()

# 压缩
# shutil.make_archive()