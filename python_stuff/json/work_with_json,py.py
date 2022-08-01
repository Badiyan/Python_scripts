import json

file = open('user.json')

user = json.load(file)

file.close()

print(user)

print('User age = ', user['age'],'\n')
print('User name = ', user['name'],'\n')
print('User gender = ', user['gender'],'\n')