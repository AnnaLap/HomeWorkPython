# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. Играют 
# два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются 
# сделавшему последний ход.
# b) Подумайте как наделить бота 'интеллектом'


from random import randint as ri

def game(num: int, candy: int):
    count = 1
    while candy > 0:
        if (count%2 != 0):
            winner = num
        else:
            if num == 1:
                winner = num + 1
            else:
                winner = num - 1
        if winner == 2:
            if (count == 1):
                taken = candy%29
            else:
                if taken > candy:
                    taken =  candy
                else:
                    taken = 29 - taken
            print(f'{count} ход. Бот забирает {taken} шт. конфет' )
        else:
            taken = int(input(f'{count} ход. Игрок № {winner} - выберите число конфет, которое хотите взять: ' ))
        if (taken > 28) or (taken < 1):
            print('Ты можешь взять только от 1 до 28 конфет за ход!')
            break
        else:
            count += 1
            candy -= taken
            print(f'Количество конфет в игре = {candy}')
        if candy == 0:
         print(f'Конец игры. Игрок № {winner} забирает все конфеты!' )
                 
    return()


num_player = ri(1,2)
quantity = int(input('Введите число конфет: '))
print(f'Игрок № 2 - бот. Первый ход за игроком № {num_player}')
game(num_player, quantity)
