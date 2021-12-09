import json
with open('users.json', 'r') as users_file:
    users = json.load(users_file)
for element in users:
    element.pop('users', None)
with open('users.json', 'w') as users_file:
    users = json.dump(users, users_file)