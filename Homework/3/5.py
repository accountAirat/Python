# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
listFib = [0]
n = 10

while len(listFib) < n * 2 + 1:
    if listFib[0] == 0:
        listFib.insert(0, 1)
        listFib.append(1)
    if listFib[0] == 1:
        listFib.insert(0, -1)
        listFib.append(1)
    else:
        listFib.insert(0, listFib[1]-listFib[0])
        listFib.append(listFib[-1]+listFib[-2])
print(listFib)
