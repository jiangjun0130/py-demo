__author__ = 'jiangjun'
__date__ = '2018/4/22 下午10:29'

f = open('yesterday', 'r', encoding='utf-8')
f_new = open('yesterday.bak', 'w', encoding='utf-8')

for line in f:
    if "肆意的快乐" in line:
        line = line.replace('肆意的快乐等我享受', '肆意的快乐等JJ享受')
    f_new.write(line)

f.close()
f_new.close()