import json


f = open('users.json')

json_data = f.read()
users_list = json.loads(json_data)


males = list(filter(lambda user: user['gender'] == 'Male', users_list))
females = list(filter(lambda user: user['gender'] == 'Female', users_list))

print(len(males), len(females))
