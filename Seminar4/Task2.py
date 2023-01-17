# B. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# Будем считать Task1 и Task2 одним большим заданием, поделенным на две части, 
# тогда нам известны к1 и к2
from Task1 import k1, k2
from collections import Counter

def read_file(file):  # Получение данных из файла
    with open(str(file), 'r') as data:
        pol = data.read()
    return pol


def create_dictionary(pol, n):
    pol = pol.replace(' = 0', '').replace('*', '').replace(' + ', 'x').replace(' -', 'x-')
    pol = pol.split('x')
    degree = []
    degree = pol[1::2]
    degree[-1] = '1'
    degree.append('0')
    del pol[1::2]
    my_dict = {}

    for i in range(n+1):
        my_dict[degree[i]] = int(pol[i])
    return(my_dict)

def sum_dictionaries(d1, d2):
    d = d1.copy()
    for k, v in d2.items():
        d[k] = d.get(k, 0) + v
    return(d)


def get_polynom(dict):
    s = ''
    for key, value in dict.items():
        if (key == list(dict)[0]) or (dict.get(key) < 0) and (key != list(dict)[-2]) and (key != list(dict)[-1]):
            s += f'{dict.get(key)}x**{key} '
        elif (key == list(dict)[-1]):
            if (dict.get(key) < 0):
                s += f' {dict.get(key)} = 0'
            else:
                s += f' + {dict.get(key)} = 0'
        elif (key == list(dict)[-2]):
            if (dict.get(key) < 0):
                s += f' {dict.get(key)}x'
            else:
                s += f' + {dict.get(key)}x'
        elif (dict.get(key) > 0):
            s += f' + {dict.get(key)}x**{key}'
    return(s)


polynom1 = read_file('Polynom1.txt')
polynom2 = read_file('Polynom2.txt')
dict_poly1 = create_dictionary(polynom1, k1)
dict_poly2 = create_dictionary(polynom2, k2)
res_dict = sum_dictionaries(dict_poly1, dict_poly2)
#print(res_dict)
sorted_tuple = sorted(res_dict.items(), key=lambda x: x[0], reverse = True)
# print(sorted_tuple)
sorted_tuple = dict(sorted_tuple)
# print(sorted_tuple)
res_string = get_polynom(sorted_tuple)
print(f'{res_string} <- sum')
with open('Polynom3.txt', 'w') as data:
    data.write(res_string)


