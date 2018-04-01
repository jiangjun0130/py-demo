__author__ = 'jiangjun'
__date__ = '2018/4/1 下午11:21'


name = input('name:')
age = input('age:')
job = input('job:')
salary = input('salary:')

info = '''
------------info of %s-----------------
Name: %s
Age: %s
Job: %s
salary: %s
''' % (name, name, age, job, salary)

print(info)

info2 = '''
------------info of {_name}-----------------
Name: {_name}
Age: {_age}
Job: {_job}
salary: {_salary}
'''.format(_name=name,_age=age,_job=job,_salary=salary)

print(info2)