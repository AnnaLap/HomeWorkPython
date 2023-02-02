# Создайте программу для игры в 'Крестики-нолики'

board = list(range(1,10))

def draw_board(board):
    print (" -" * 6)
    for i in range(3):
        print (" ", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3])
        print (" -" * 6)


def play(board, win):
    count = 1
    while win == False:
        if count%2 == 0:
            position = int(input("Куда поставим X?  "))
            if (board[position - 1] == 'X') or (board[position - 1] == 'O'):
                print('Некорректный ввод')
                continue
            board[position - 1] = 'X'
        else:
            position = int(input("Куда поставим O?  "))
            if (board[position - 1] == 'X') or (board[position - 1] == 'O'):
                print('Некорректный ввод')
                continue
            board[position - 1] = 'O'
        draw_board(board)
        if check(board) == 1:
            break
        if (count == 9) and (win == False):
            print('Ничья!' )
            win = True
            return
        count += 1



def check(board):
    if (board[0] == 'X') and (board[1] == 'X') and (board[2] == 'X') or\
    (board[3] == 'X') and (board[4] == 'X') and (board[5] == 'X') or\
    (board[6] == 'X') and (board[7] == 'X') and (board[8] == 'X') or\
    (board[0] == 'X') and (board[4] == 'X') and (board[8] == 'X') or\
    (board[2] == 'X') and (board[4] == 'X') and (board[6] == 'X') or\
    (board[0] == 'X') and (board[3] == 'X') and (board[6] == 'X') or\
    (board[1] == 'X') and (board[4] == 'X') and (board[7] == 'X') or\
    (board[2] == 'X') and (board[5] == 'X') and (board[8] == 'X'):
        print ('Выиграли Х!')
        return 1
    if (board[0] == 'O') and (board[1] == 'O') and (board[2] == 'O') or\
    (board[3] == 'O') and (board[4] == 'O') and (board[5] == 'O') or\
    (board[6] == 'O') and (board[7] == 'O') and (board[8] == 'O') or\
    (board[0] == 'O') and (board[4] == 'O') and (board[8] == 'O') or\
    (board[2] == 'O') and (board[4] == 'O') and (board[6] == 'O') or\
    (board[0] == 'O') and (board[3] == 'O') and (board[6] == 'O') or\
    (board[1] == 'O') and (board[4] == 'O') and (board[7] == 'O') or\
    (board[2] == 'O') and (board[5] == 'O') and (board[8] == 'O'):
        print ('Выиграли O!')
        return 1


print('Welcome to X-O game!')
win = False
draw_board(board)
play(board, win)

        
