import json

user =  {"name": "Badian", "gender": "male", "age": 24}

file = open('new_user','w')

json.dump(user, file)

file.close()

file = open('new_user', 'r')
print(file.read())