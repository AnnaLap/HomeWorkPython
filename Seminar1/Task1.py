# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

number = int(input('Add number of week day: '))
if 0 < number < 8:
    if number > 5:
        print("yes, it's weekend ;)")
    else:
        print("no, it's weekday ;(")
else:
    print("number is out of range")
