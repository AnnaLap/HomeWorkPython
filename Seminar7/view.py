

def main_menu():
    commands = ['Показать все контакты',
                'Открыть файл',
                'Сохранить файл',
                'Новый контакт',
                'Изменить контакт',
                'Удалить контакт',
                'Найти контакт',
                'Выйти из программы']
    print('Меню команд: ')
    for i in range(len(commands)):
        print(f'\t{i+1}. {commands[i]}')
    user_input = int(input('Выберите команду из меню: '))
    print('\n')
    while True:
        if (1 > user_input) or (user_input > 8):
            print('Введено некорректное значение. Попробуйте снова\n')
            user_input = int(input('Выберите команду из меню: '))
            print('\n')
        break
    return (user_input)


def show_contacts(phone_book: list, ui: int):
    if len(phone_book) > 0:
        print('id     Имя           Телефон   Комментарий')
        for i in range(len(phone_book)):
            print(
                f'{i+1}. {phone_book[i][0]} {phone_book[i][1]} ({phone_book[i][2]})')
        print('\n')
    else:
        if ui == 7:
            print('Совпадений не найдено\n')
        else:
            print('Телефонная книга пуста или не загружена\n')


def load_success():
    print('Телефонная книга загружена успешно\n')


def save_success():
    print('Телефонная книга сохранена успешно\n')


def new_contact():
    new = []
    name = input('Введите имя контакта: ')
    phone = input('Введите телефон контакта: ')
    comment = input('Введите комментарий к контакту: ')
    return name, phone, comment


def find_contact():
    search = input('Введите искомое значение: ')
    return search


def get_id(phone_book: list):
    id = int(input('Введите значение id контакта: '))
    while True:
        if (id < 1) or (id > len(phone_book)):
            print('Введен некорректный id. Попробйте снова\n')
            id = int(input('Введите значение id контакта: '))
            print('\n')
        break
    return id


def saving_choice():
    exit = int(input(
        'Исходный и конечный файл различаются. Сохранить изменения перед выходом? (0 - нет, 1 - да): '))
    if (exit == 1) or (exit == 0):
        pass
    else:
        print('Некорректное значение. Попробйте снова\n')
        exit = int(input('Сохранить изменения перед выходом? (0 - нет, 1 - да): '))
        print('\n')
    return exit
