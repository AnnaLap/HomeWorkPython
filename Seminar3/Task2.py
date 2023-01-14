# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random


def create_list(N, my_list):
    for i in range(N):
        my_list.append(random.randint(1, 10))
    return (my_list)


def multiply_pairs(my_list):
    res_list = []
    num = len(my_list)
    for i in range(len(my_list)):
        if (i <= len(my_list)/2) and (num > len(my_list)/2):
            res_list.append(my_list[i] * my_list[num-1])
            num -= 1
    print(res_list)


new_list = []
n = int(input('Введите колчество элементов в списке: '))
create_list(n, new_list)
print(new_list, end=' => ')
multiply_pairs(new_list)
