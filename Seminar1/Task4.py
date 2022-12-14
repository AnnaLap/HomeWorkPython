# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from math import sqrt
x1 = int(input('X1 = '))
y1 = int(input('Y1 = '))
x2 = int(input('X2 = '))
y2 = int(input('Y2 = '))
print(f'distance between A{x1,y1} and B{x2,y2} is {round(sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)}')