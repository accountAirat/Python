# Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

xA = int(input("Введите X, не 0: "))
yA = int(input("Введите Y, не 0: "))
xB = int(input("Введите X, не 0: "))
yB = int(input("Введите Y, не 0: "))
print(round(((xA-xB)**2 + (yA - yB)**2)**0.5 , 2))
