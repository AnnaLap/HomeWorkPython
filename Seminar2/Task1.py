# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11


number = float(input('Enter float number: '))

if number < 0:
    number *= (-1)

sum = 0
for item in str(number):
    if item != '.':
        sum += int(item)
print(sum)