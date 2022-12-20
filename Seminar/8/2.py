numbers = [2, 3, 4, 5, 6, 7, 5]
diff = [a*b for a, b in zip(numbers, numbers[:(len(numbers)//2) - 1: -1])]
print(diff)