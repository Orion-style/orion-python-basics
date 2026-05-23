tickets = [
    {
        "id": 1,
        "title": "Не работает вход",
        "status": "open"
    },
    {
        "id": 2,
        "title": "Ошибка оплаты",
        "status": "closed"
    },
    {
        "id": 3,
        "title": "Нужна помощь",
        "status": "open"
    }
]

for ticket in tickets:
    print("ID:", ticket["id"])
    print("Title:", ticket["title"])
    print("Status:", ticket["status"])
    print("---")