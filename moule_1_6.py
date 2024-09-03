my_dict = {'Anna': 1978, 'Petya': 1996, 'Liza': 2003}
print('Словарь:', my_dict)
print('Присутствует в словаре:', my_dict['Liza'])
print('Отсутствует в словаре:', my_dict.get('Izya', 'Нет в словаре!'))
my_dict.update({'Vitaly': 1984,
                'Rimma': 1994})
petya_off = my_dict.pop('Petya')
print('Значение удаленной пары:', petya_off)
print('Измененный словарь', my_dict)
my_set = {8, 'Whisky', 5, 'Rum', 8, 3, 3, 'Rum', 5}
print('Множество:', my_set)
my_set.update({'Vodka', 9})
my_set.discard(5)
print('Измененное множество:', my_set)
