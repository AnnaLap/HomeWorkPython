phone_book = []
path = 'book.txt'


def get_phone_book():
    global phone_book
    return phone_book


def update_phone_book(contact: list):
    global phone_book
    phone_book.append(contact)


def open_phone_book():
    global phone_book
    global path
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
        for line in data:
            phone_book.append(line.strip().split(';'))


def save_phone_book():
    global phone_book
    global path
    data = []
    for line in phone_book:
        data.append(';'.join(line))
    with open(path, 'w', encoding='UTF-8') as file:
        data = file.write('\n'.join(data))


def search_contact(search: str):
    global phone_book
    search_results = []
    for line in phone_book:
        for field in line:
            if search in field:
                search_results.append(line)
                break
    return search_results


def edit_contact(n: int, line: list):
    global phone_book
    for i in range(len(phone_book)):
        if i+1 == n:
            phone_book[i] = line
    return


def delete_contact(n: int):
    global phone_book
    for i in range(len(phone_book)):
        if i+1 == n:
            del phone_book[i]
    return


def get_difference():
    global phone_book
    global path
    current_data = []
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for line in data:
        current_data.append(line.strip().split(';'))
    get_phone_book()
    if phone_book == current_data:
        return 0
    else:
        return 1
