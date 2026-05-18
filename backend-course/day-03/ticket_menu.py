tickets = []

while True:
    print("\n--- Меню заявок ---")
    print("1. Создать заявку")
    print("2. Показать все заявки")
    print("3. Выйти")

    command = input("Выберите команду: ")

    if command == "1":
        title = input("Введите название заявки: ")
        tickets.append(title)
        print("Заявка успешно создана!")
    
    elif command == "2":
        if len(tickets) == 0:
            print("Нет заявок для отображения.")
        else:
            print("--- Список заявок ---")
            for ticket in tickets:
                print(f"- {ticket}")
    
    elif command == "3":
        print("До скорых встреч!")
        break

    else:
        print("Неверная команда. Пожалуйста, выберите снова.")