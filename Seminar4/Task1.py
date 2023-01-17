# A. Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


def create_list(n, my_list):
    for i in range(n + 1):
        my_list.append(random.randint(-100, 100))
        while my_list[0] == 0:
            my_list[0] = random.randint(-100, 100)
    return (my_list)


def polynomial(my_list):
    s = ''
    for i in range(len(my_list)):
        if i != len(my_list) - 1 and (my_list[i] != 0 and i != len(my_list) - 2):
            s += f'{my_list[i]}x**{len(my_list) - i - 1}'
            if my_list[i + 1] > 0:
                s += ' + '
            else:
                s += ' '
        elif i == len(my_list) - 2 and (my_list[i] != 0):
            s += f'{my_list[i]}x'
            if my_list[i + 1] > 0:
                s += ' + '
            else:
                s += ' '
        elif i == len(my_list) - 1 and (my_list[i] != 0):
            s += f'{my_list[i]}'
    s += ' = 0'
    return (s)


k1 = int(input('Введите значение k1 = '))
k2 = int(input('Введите значение k2 = '))
koef_list1 = []
koef_list2 = []
create_list(k1, koef_list1)
print(polynomial(koef_list1))
create_list(k2, koef_list2)
print(polynomial(koef_list2))
with open('Polynom1.txt', 'w') as data:
    data.write(polynomial(koef_list1))
with open('Polynom2.txt', 'w') as data:
    data.write(polynomial(koef_list2))