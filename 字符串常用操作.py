__author__ = 'jiangjun'
__date__ = '2018/4/15 下午2:13'

name = 'my name is tom'
print(name.capitalize())  # My name is tom

print(name.count('a'))  # 1

print(name.center(50, '-'))  # ------------------my name is tom------------------
print(name.ljust(50, '-'))   # my name is tom------------------------------------
print(name.rjust(50, '-'))   # ------------------------------------my name is tom


print(name.endswith('m'))  # True


name = 'my name is {name} and {years} old'
print(name.format(name='jack', years=18))  # my name is jack and 18 old

print(name.format_map({'name': 'Luci', 'years': 20}))  # my name is Luci and 20 old

print('+'.join(['1', '2', '3', '4']))  # 1+2+3+4

print('Tom'.lower())  # tom
print('tom'.upper())  # TOM

# 去除左边的空格回车
print('\nHello'.lstrip())  # Hello
# 去除又边的空格回车
print('Hello\n'.rstrip())  # Hello
# 去除左右两边的空格回车
print('\nHello  Haha\n'.strip())


# sql = '''
#      SELECT e.id,e.project_name,e.upload_time,e.batch,f.sn,f.project_name AS sub_name FROM
#      (SELECT c.id,c.project_name,c.upload_time,d.id AS batch_id,d.batch FROM
#      (SELECT a.id,a.`project_name`,b.upload_time FROM  project_bidding_info AS a LEFT JOIN project_notice_info AS b ON a.id=b.project_id WHERE a.id=1) AS c
#       LEFT JOIN batch_project AS d ON d.batch_Project_id =c.id) AS e LEFT JOIN sub_project AS f ON f.batch_subProject_id =e.batch_id
#       WHERE  e.project_name LIKE '%{name}%' OR e.upload_time LIKE '%{time}%' OR  e.batch LIKE '%{batch}%' OR f.sn LIKE '%{sn}%' OR f.project_name LIKE '%{name}%'
# '''
#
# print(sql.format(name='名称', time='xxx', batch='001', sn='002')
# )

tpl_params = "{'name': %s, 'project_name': %s}" % ('江俊', '哈哈')
print(tpl_params)