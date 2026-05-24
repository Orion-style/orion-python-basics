import json

with open("day-06/user_data.json", "r", encoding="utf-8") as file:
    user_data = json.load(file)

print('ID:', user_data['id'])
print('Username:', user_data['username'])
print('Role:', user_data['role'])