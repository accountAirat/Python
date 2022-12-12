x  = "qwerty asdfабвggh zxcvbnабв lkjhgf".split()
y = "абв"
x = list(filter(lambda i: y in i, x))

print(x)