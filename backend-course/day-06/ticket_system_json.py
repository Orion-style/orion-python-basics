import os

tickets = []
next_id = 1
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, 'tickets.json')

import json
def create_ticket(ticket_id, title):
    return {
        'id': ticket_id,
        'title': title,
        'status': 'open'
    }
def show_ticket(ticket):
    print('ID:', ticket['id'])
    print('Title:', ticket['title'])
    print('Status:', ticket['status'])
    print('-----')

def show_all_tickets():
    if len(tickets) == 0:
        print('Заявок нет')
    else:
        for ticket in tickets:
            show_ticket(ticket)

def find_ticket_by_id(search_id):
    for ticket in tickets:
        if ticket['id'] == search_id:
            return ticket
        
while True:
    print("\n--- Меню заявок ---")
    print("1. Создать заявку")
    print("2. Показать все заявки")
    print("3. Найти заявку по ID")
    print("4. Сохранить заявки")
    print("5. Загрузить заявки")
    print("6. Выйти")

    command_input = input("Выберите действие: ")
    if command_input == '1':
        title = input("Введите название заявки: ")
        ticket = create_ticket(next_id, title)
        tickets.append(ticket)
        next_id += 1
        print('Заявка создана')

    elif command_input == '2':
        show_all_tickets()

    elif command_input == '3':
        search_id = int(input("Введите ID заявки для поиска: "))
        ticket = find_ticket_by_id(search_id)
        if ticket is None:
            print("Заявка с таким ID не найдена")
        else:
            show_ticket(ticket)
    
    elif command_input == '4':
        with open(FILE_PATH, 'w', encoding='utf-8') as file:
            json.dump(tickets, file, ensure_ascii=False, indent=4)
        print('Заявки сохранены в файл')

    elif command_input == '5':
        try:
            with open(FILE_PATH, 'r', encoding='utf-8') as file:
                tickets = json.load(file)
                if len(tickets) > 0:
                    next_id = tickets[-1]['id'] + 1
                else:
                    next_id = 1
            print('Заявки загружены из файла')
        except FileNotFoundError:
            print('Файл с заявками не найден')

    elif command_input == '6':
        print("Выход из программы")
        break
    else:
        print("Неверная команда, попробуйте снова")