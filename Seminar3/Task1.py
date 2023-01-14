# Задайте список из нескольких чисел. Напишите программу, которая найдёт
# сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random


def create_list(N, my_list):
    for i in range(N):
        my_list.append(random.randint(0, 10))
    return (my_list)


def sum_not_even(my_list):
    sum = 0
    notEven = []
    for i in range(len(my_list)):
        if (i % 2 != 0) and (i != 0):
            sum += int(my_list[i])
            notEven.append(my_list[i])
    print('На нечетных позициях элементы', end=' ')
    print(*notEven, sep=', ', end='; ')
    print(f'Ответ = {sum}')


new_list = []
n = int(input('Введите колчество элементов в списке: '))
create_list(n, new_list)
print(new_list, end=' -> ')
sum_not_even(new_list)
