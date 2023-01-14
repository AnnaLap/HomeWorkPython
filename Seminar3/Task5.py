# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи


def Fibonacci(n):
    if (n == 1) or (n == 2):
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


def negaFibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return -1
    else:
        return negaFibonacci(n - 2) - negaFibonacci(n - 1)


number = int(input('Введите число k = '))
my_list = [0]
for i in range(1, number + 1):
    my_list.append(Fibonacci(i))
    my_list.insert(0, negaFibonacci(i))
print(my_list)
