while True:
    print("1. Поздороваться")
    print("2. Показать цель")
    print("3. Выйти")

    command = input("Выберите команду: ")

    if command == "1":
        print("Приветствую Gs.Vandis!")
    elif command == "2":
        print("Попасть на стажировку на Backend-разработку!")
    elif command == "3":
        print("До скорых встреч, Gs.Vandis!")
        break
    else:
        print("Неверная команда. Пожалуйста, выберите снова.")