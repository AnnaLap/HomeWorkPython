# Реализуйте алгоритм перемешивания списка. 
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для и получения случайного int
import random

spisok = [1,2,3,4,5,6,7,8,9,10]
def shuffle_list(my_list):
    j = 0
    for i in range(len(my_list)):
        j = random.randint(0, len(my_list)-1)
        my_list[i], my_list[j] = my_list[j], my_list[i]
    return(my_list)

print(f'{spisok} -> {shuffle_list(spisok)}')
