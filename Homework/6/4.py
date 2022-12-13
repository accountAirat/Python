# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Старое решение
# n = int(input("Введите число: "))
# a,b = map(int, input("Введите две позиции через пробел: ").split())
# num = []
# prod = 0
# for i in range(-n, n+1):
#     num.append(i)
# prod = num[int(a)] * num[int(b)]
# print(num , prod)

# Новое решение
n = int(input("Введите число: "))
a,b = map(int, input("Введите две позиции через пробел: ").split())
list = [i for i in range(-n, n+1)]
print(list, list[a] * list[b])