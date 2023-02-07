# Задайте список из нескольких чисел. Напишите программу, которая найдёт
# сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint as RI
from functools import reduce

def create_list(N):
    # for i in range(N):
    #     my_list.append(RI(0, 10))
    my_list = [ RI(0, 10) for _ in range(N) ]
    return my_list


def sum_not_even(my_list):
    sum = 0
    # notEven = []
    # notEven = list(filter(lambda x: (x % 2 != 0) and (x != 0), [my_list[i] for i in range(len(my_list))]))
    notEven = [my_list[i] for i in range(len(my_list)) if (i % 2 != 0) and (i != 0)]
    sum = reduce(lambda a, b: a + b, notEven)
    # for i in range(len(my_list)):
    #     if (i % 2 != 0) and (i != 0):
    #         sum += int(my_list[i])
    #         notEven.append(my_list[i])
    print('На нечетных позициях элементы', end=' ')
    print(*notEven, sep=', ', end='; ')
    print(f'Ответ = {sum}')


n = int(input('Введите колчество элементов в списке: '))
new_list = create_list(n)
print(new_list, end=' -> ')
sum_not_even(new_list)
