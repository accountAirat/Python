# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

s = float(input("Введите число: "))
c = int(input("Введите точность: "))
print(round(s , c))
print(s//1+float(str(s%1)[:c+2]))