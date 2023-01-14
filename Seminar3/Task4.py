# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10


def demical_to_binary(n):
    res_list = []
    while n > 0:
        res_list.append(n%2)
        n //= 2
    print("".join(map(str, res_list[::-1])))

number = int(input('Введите десятичное число: '))
print(number, end=' -> ')
demical_to_binary(number)