import json

file = open('customers')

customers = json.load(file)

file.close()

for customer in customers:
    if customer['gender']=='female':
        print(customer)