# B. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# Будем считать Task1 и Task2 одним большим заданием, поделенным на две части, 
# тогда нам известны к1 и к2

from itertools import zip_longest


def read_file(file):  # Получение данных из файла
    with open(str(file), 'r') as data:
        pol = data.read()
    return pol

def create_pol(pol, n):
    pol = pol.replace(' = 0', '').replace('*', '').replace(' + ', 'x').replace(' -', 'x-')
    pol = pol.split('x')
    degree = []
    degree = pol[1::2]
    degree[-1] = '1'
    degree.append('0')
    del pol[1::2]
    # my_dict = {}

    # for i in range(n+1):
    #     my_dict[degree[i]] = int(pol[i])
    revdeg = list(map(int, reversed(degree)))
    revpol = list(map(int, reversed(pol)))
    # print(revpol)
    return(revpol)

def create_deg(pol, n):
    pol = pol.replace(' = 0', '').replace('*', '').replace(' + ', 'x').replace(' -', 'x-')
    pol = pol.split('x')
    degree = []
    degree = pol[1::2]
    degree[-1] = '1'
    degree.append('0')
    del pol[1::2]
    # my_dict = {}

    # for i in range(n+1):
    #     my_dict[degree[i]] = int(pol[i])
    revdeg = list(map(int, reversed(degree)))
    # print(revdeg)
    return(revdeg)


def sum_dictionaries(d1, d2):

    # d = d1.copy()
    # for k, v in d2.items():
    #     d[k] = d.get(k, 0) + v
    return()


# def get_polynom(dict):
#     s = ''
#     for key, value in dict.items():
#         if (key == list(dict)[0]) or (dict.get(key) < 0) and (key != list(dict)[-2]) and (key != list(dict)[-1]):
#             s += f'{dict.get(key)}x**{key} '
#         elif (key == list(dict)[-1]):
#             if (dict.get(key) < 0):
#                 s += f' {dict.get(key)} = 0'
#             else:
#                 s += f' + {dict.get(key)} = 0'
#         elif (key == list(dict)[-2]):
#             if (dict.get(key) < 0):
#                 s += f' {dict.get(key)}x'
#             else:
#                 s += f' + {dict.get(key)}x'
#         elif (dict.get(key) > 0):
#             s += f' + {dict.get(key)}x**{key}'
#     return(s)


polynom1 = read_file('Polynom1.txt')
polynom2 = read_file('Polynom2.txt')
dict_poly1 = create_pol(polynom1, 4)
dict_poly2 = create_pol(polynom2, 6)
dict_deg1 = create_deg(polynom1, 4)
dict_deg2 = create_deg(polynom2, 6)
zippedpol = [x+y for x, y in zip_longest(dict_poly1, dict_poly2, fillvalue = 0)]
# print(zippedpol)
if len(dict_deg1) > len(dict_deg2):
    dict_deg = dict_deg1
else:
    dict_deg = dict_deg2
zipped = list(zip(dict_deg, zippedpol))
itog = list(reversed(zipped))
print(itog)
for i in range(len(zipped)):
        if i == len(zipped)-1:
            print(f' {itog[i][1]} = 0')
        else:
            if i == len(zipped)-2:
                print(f'{itog[i][1]}x', end= '')
            else:
                print(f'{itog[i][1]}x**{itog[i][0]}', end= '')
                print(f' + ', end= '')
        
  
# res_dict = sum_dictionaries(dict_poly1, dict_poly2)
#print(res_dict)
# print(sorted_tuple)
# print(sorted_tuple)

polynom1 = read_file('Polynom1.txt')
polynom2 = read_file('Polynom2.txt')

print()






