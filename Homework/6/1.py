# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


# 1) Моё решение
# print(list(set([1, 1, 3, 2, 2, 1, 1, 1, 1])))

# 2) Решение на разборе
# n = [1, 1, 3, 2, 2, 1, 1, 1, 1]
# a = []
# for i in n:
#     if n.count(i) == 1:
#         a.append(i)
# print(a)

# 3) ДЗ 6 урока. Решение новыми методами
n = [1, 1, 3, 2, 2, 1, 1, 1, 1]
print(*filter(lambda x: n.count(x) == 1, n ))