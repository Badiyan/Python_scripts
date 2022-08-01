import json
fp = open("user_addresses.txt")
users_list = json.load(fp)

print(users_list[0]['address']['city'])