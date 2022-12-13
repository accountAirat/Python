num = ["a", "b", "c", "g", "h"]
id = [4, 5, 6, 7]
x = [77, 66, 55]

a, b, c = map(list,zip(num, id, x))
print(a, b, c, sep="\n")

a,b,c=map(list,zip(a,b,c))
print(a, b, c, sep="\n")