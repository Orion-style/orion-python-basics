def show_user(user):
    print("ID:", user["id"])
    print("Name:", user["name"])
    print("Role:", user["role"])

user = {
    "id": 1,
    "name": "Vandis",
    "role": "Student"
}

show_user(user)