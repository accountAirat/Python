# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.

n = int(input("Введите число: "))
a,b = input("Введите две позиции через пробел: ").split()
num = []
prod = 0
for i in range(-n, n+1):
    num.append(i)
prod = num[int(a)] * num[int(b)]
print(num , prod)

