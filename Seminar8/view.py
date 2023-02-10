
def input_class():
    chosen_class = input('Какой класс? ')
    while True:
        if (chosen_class != '6а') and (chosen_class != '6б') and (chosen_class != '6в'):
            print('Некорректный ввод. Попробйте снова\n')
            chosen_class = input('Какой класс? ')
            print('\n')
        break
    return chosen_class


def input_subject():
    chosen_subject = input('Какой предмет? ').lower()
    while True:
        if (chosen_subject != 'математика') and (chosen_subject != 'литература') and (chosen_subject != 'биология'):
            print('Некорректный ввод. Попробйте снова\n')
            chosen_subject = input('Какой предмет? ')
            print('\n')
        break
    return chosen_subject


def who_answer():
    who_answer = input('Кто будет отвечать? ')
    return who_answer


def what_mark():
    chosen_mark = int(input('На какую оценку ответил(а)? '))
    while True:
        if (int(chosen_mark) < 2) or (int(chosen_mark) > 5):
            print('Некорректный ввод. Попробйте снова\n')
            chosen_mark = int(input('На какую оценку ответил(а)? '))
            print('\n')
        break
    return chosen_mark


def list_of_child(journal: dict):
    for i, child in enumerate(journal, 1):
        print(f'{i}. {child:20}', end= '')
        print('[%s]' % ', '.join(list(map(str, journal.get(child)))))
