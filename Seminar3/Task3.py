# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random


def create_list(N, my_list):
    for i in range(N):
        my_list.append(round(random.uniform(0, 10.99), 2))
    return (my_list)


def diff_nums(my_list):
    fractional_list = []
    for i in range(len(my_list)):
        fractional_list.append(round(my_list[i] - int(my_list[i]), 2))
    print(round(max(fractional_list) - min(fractional_list), 2))


new_list = []
n = int(input('Введите колчество элементов в списке: '))
create_list(n, new_list)
print(new_list, end=' => ')
diff_nums(new_list)
