__author__ = 'jiangjun'
__date__ = '2018/4/22 下午10:29'

# with执行完毕时，会自动关闭文件并释放文件资源。with支持同时对多个文件的上下文进行管理
with open('yesterday', 'r', encoding='utf-8') as f, \
        open('yesterday2', 'r', encoding='utf-8') as f2:
    for line in f:
        print(line)

