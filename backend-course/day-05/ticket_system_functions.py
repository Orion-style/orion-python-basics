tickets = []
next_id = 1

def create_ticket(ticket_id, title):
    return {
        "id": ticket_id,
        "title": title,
        "status": "open"
    }

def show_ticket(ticket):
    print("ID:", ticket["id"])
    print("Название:", ticket["title"])
    print("Статус:", ticket["status"])
    print("-----")

def show_all_tickets():
    if len(tickets) == 0:
        print("Заявок пока нет")
    else:
        for ticket in tickets:
            show_ticket(ticket)

def find_ticket_by_id(search_id):
    for ticket in tickets:
        if ticket["id"] == search_id:
            return ticket

    return None

while True:
    print("\n--- Меню заявок ---")
    print("1. Создать заявку")
    print("2. Показать все заявки")
    print("3. Найти заявку по ID")
    print("4. Выйти")

    command = input("Выберите команду: ")

    if command == "1":
        title = input("Введите название заявки: ")

        ticket = create_ticket(next_id, title)
        tickets.append(ticket)
        next_id = next_id + 1

        print("Заявка создана")

    elif command == "2":
        show_all_tickets()

    elif command == "3":
        search_id = int(input("Введите ID заявки: "))
        ticket = find_ticket_by_id(search_id)

        if ticket is None:
            print("Заявка не найдена")
        else:
            show_ticket(ticket)

    elif command == "4":
        print("Выход")
        break

    else:
        print("Неизвестная команда")