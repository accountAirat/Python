# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

# Старое решение
# num = input("Введите вещественное число: ")
# sum = 0
# for i in range(len(num)):
#     if num[i] != ",":
#         sum = sum + int(num[i])
# print(sum)

# Новое
print(sum(map(int, (filter(str.isdigit, input("Введите вещественное число: "))))))