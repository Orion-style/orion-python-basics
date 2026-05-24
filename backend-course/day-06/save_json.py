import json

user_data = {
    'id': 1,
    'username': 'Gs. Vandis',
    'role': 'student'
}

with open("user_data.json", "w", encoding="utf-8") as file:
    json.dump(user_data, file, ensure_ascii=False, indent=4)

print("Данные сохранены в user_data.json")