# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

dayNumber = int(input("Введите номер дня недели: ")) 
if dayNumber == 6 or dayNumber == 7:
    print("да")
elif dayNumber > 0 and dayNumber < 6:
    print("нет")
else:
    print("Такого дня недели нет")
