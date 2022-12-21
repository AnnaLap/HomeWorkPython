# Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, 
# а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

my_list = []
n = int(input('Enter n = '))
if n < 0:
    print('Only natural numbers')
    exit()
summa = 0 
for i in range(1,n+1):
    my_list.append(round((1+1/i)**i, 2))
    summa += round((1+1/i)**i,2)
print(f'Для n = {n} -> {my_list}')
#print(f'Сумма {sum(my_list)}') #easy way
print(f'Сумма {summa}')
