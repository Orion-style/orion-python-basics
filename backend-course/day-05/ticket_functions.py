def create_ticket(ticket_id, title):
    ticket = {
        'id': ticket_id,
        'title': title,
        'status': 'open'
    }

    return ticket

def show_ticket(ticket):
    print("ID:", ticket['id'])
    print("Title:", ticket['title'])
    print("Status:", ticket['status'])

ticket = create_ticket(1, "Не работает вход")
show_ticket(ticket)