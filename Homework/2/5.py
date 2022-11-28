# Реализуйте алгоритм перемешивания списка.
import random
array = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
for i in range(len(array)):
    a = random.randint(0,len(array)-1)
    b = random.randint(0,len(array)-1)
    array[a], array[b] = array[b], array[a]
    a, b = b, a
print(array)
