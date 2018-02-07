import  json

json_str = '{"name":"jj", "age":28}'

student = json.loads(json_str)
# dict
print(student)
print(student['name'])
print(student['age'])

json_str2 = '[{"name":"jj", "age":28, "flag":false},{"name":"jj", "age":28}]'
students = json.loads(json_str2)
# list
print(type(students))
print(students)
