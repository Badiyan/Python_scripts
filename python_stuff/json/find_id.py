import json

fp = open("users.txt")

users = json.load(fp)

first_user = None

for user in users:
    if first_user is None or user["registered"] > first_user["registered"]:
        first_user = user

print(first_user['id'])