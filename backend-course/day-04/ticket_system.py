tickets = []
next_id = 1

while True:
    print("\n---Меню заявок---")
    print("1. Создать заявку")
    print("2. Просмотреть заявки")
    print("3. Найти заявку")
    print("4. Выйти")

    command = input("Выберите действие: ")
    
    if command == "1":
        title = input("Введите название заявки: ")
        ticket = {
            "id": next_id,
            "title": title,
            "status": "open"
        }
        tickets.append(ticket)
        next_id += 1

    elif command == "2":
        if not tickets:
            print("Заявок нет")
        else:
            for ticket in tickets:
                print("ID:", ticket["id"])
                print("Title:", ticket["title"])
                print("Status:", ticket["status"])
                print("---")

    elif command == "3":
        search_id = int(input("Введите ID заявки для поиска: "))
        found = False
        for ticket in tickets:
            if ticket["id"] == search_id:
                print("ID:", ticket["id"])
                print("Title:", ticket["title"])
                print("Status:", ticket["status"])
                found = True
                break
        if not found:
            print("Заявка с таким ID не найдена")

    elif command == "4":
        print("Выход из программы")
        break

    else:
        print("Неверная команда, попробуйте снова")