# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

n = 360
Ans = []
d = 2
while d * d <= n:
    if n % d == 0:
        Ans.append(d)
        n //= d
    else:
        d += 1
if n > 1:
    Ans.append(n)
print(Ans)