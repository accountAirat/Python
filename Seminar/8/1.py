import random
a = random.randint(5, 11)
b = [1, 1]
[b.append(b[i-2] + b[i-1]) for i in range(2, a)] + [b.insert(0, b[1] - b[0]) for i in range(a + 1)]
print(b)