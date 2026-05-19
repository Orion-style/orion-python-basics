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
    }
]

search_id = int(input("Введите ID тикета для поиска: "))

found = False

for ticket in tickets:
    if ticket["id"] == search_id:
        print("ID:", ticket["id"])
        print("Title:", ticket["title"])
        print("Status:", ticket["status"])
        found = True
        break
if not found:
        print  ("Тикет с таким ID не найден")