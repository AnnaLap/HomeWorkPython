# Напишите программу, которая принимает на вход координаты
# точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x = 34; y = -30 -> 4
# - x = 2; y = 4-> 1
# - x = -34; y = -30 -> 3

coordX = int(input('Add x: '))
coordY = int(input('Add y: '))
if coordX == 0 or coordY == 0:
    print('incorrect values')
elif coordX > 0 and coordY > 0:
    print("quarter is 1")
elif coordX < 0 and coordY > 0:
    print("quarter is 2")
elif coordX < 0 and coordY < 0:
    print("quarter is 3")
elif coordX > 0 and coordY < 0:
    print("quarter is 4")
