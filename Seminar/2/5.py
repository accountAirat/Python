# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
#     *Пример:*
    
#     - Для N = 5: 1, -3, 9, -27, 81

# n = int(input())
# n2 = 1
# print(n2)
# for i in range(1, n):
#     n2 = n2 * (-3)
#     print(n2)

n = int(input("Введите число: "))
for i in range(n):
    print((-3)**i)
