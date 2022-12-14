# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list_1 = [2, 3, 4, 5, 6]

# Старое решение

# list_2 = []
# for i in list_1:
#     list_2.append(i * list_1.pop())
# print(list_2)


# ДЗ 6 урока. Решение новыми методами
print(list(map(lambda x : x * list_1.pop(), list_1)))