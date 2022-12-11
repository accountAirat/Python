# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
k = random.randint(0,5)# Выбираем натуральную степень
n = random.randint(1,k+1)# Выбираем колличество коэффициентов 
s = []
for i in range(0, n):# Создаём список коэффициентов
    s.append(str(random.randint(0,100)))
print(s)

m = []
for i in range(0, n):
    if k-i > 1:# Собираем уровнение и вычисляем х в какой степени как оформить
        m.append(str(f"{s[i]}*x**{k-i}"))
    elif (k - i) == 1:
        m.append(str(f"{s[i]}*x"))
    elif (k - i) == 0:
        m.append(str(f"{s[i]}"))
    if i < n - 1:# Вычисляем какой знак нужно поставить + или = 0
        m.append(" + ")
    else:
        m.append(" = 0")
print(m)

with open('fffile.txt', 'w') as f:
    f.writelines(m)