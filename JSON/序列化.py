import json

students = [
    {'name': 'jj', 'age': 28, 'flag': False},
    {'name': 'tom', 'age': 28, 'flag': True}
]

json_str = json.dumps(students)
print(type(json_str)) # str
print(json_str)