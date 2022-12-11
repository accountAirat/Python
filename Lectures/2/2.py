# import files as h # импорт функций из файла, можно делить программу

# print(h.f(2))

# def d(*num): # неограниченное колличество аргументов

# def x(q, z = 3): # можно умножить str на int(колличество str), если z не пода1ёётся, тогда оно 3.

# Кортеж - это не изменяемый список
# a = (2,3)
# print(a[0])
# 1 Лист >>> в кортеж
# colors = ['red', 'green', 'blue']
# print(colors)
# t = tuple(colors)
# print(t)

# 2 Лист >>> Кортеж >>> Вложили целый кортеж в переменную
# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))

# 3 Словари - по ключу
# dictionary = {}
# dictionary = \  
#  {
#  'up': '↑',
#  'left': '←',
#  'down': '↓',
#  'right': '→'
#  } # обратный слешь даёт писать не в одну строку
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) 

# 4 Множество - Неупорядоченые УНИКАЛЬНЫХ элементов
# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a)) # set
# print(type(b)) 


# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red') # Добавить элемент, который уже есть не получится
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red') # Удалить элемент
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { } Отчистить множества
# print(colors) # set()


# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}  Копирование
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}  Объединение
# i = a.intersection(b) # i = {8, 2, 5}  Пересечение, одинаковые элементы
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q = a \
#  .union(b) \
#  .difference(a.intersection(b))

#  Неизменяемое множество 

# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})
