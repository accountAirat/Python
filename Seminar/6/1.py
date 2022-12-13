string = '-8 11 0 -23 140 1'
string = list(map(int, string.split()))
print(*filter(lambda x: 100 > abs(x) > 9, string))
# 11 -23