# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

from functools import reduce

# num = float(input('Enter float number: '))

# if number < 0:
#     number *= (-1)
# number = lambda x: x*(-1) if (x < 0) else x
string = input('Enter float number: ')
print(string, end= '')
string = string.replace('-', '').replace('.', '')
my_list = [int(i) for i in str(string)]
# print(my_list)
# my_list = list(map(int, string.split()))
# sum = 0
# for item in str(number(num)):
#     if item != '.':
#         sum += int(item)
sum = reduce(lambda a, b: a + b, my_list)
print(f' -> {sum}')