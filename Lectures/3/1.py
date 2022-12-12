# def f(x):
#    return x**3

# # g = f
# # print(f(2))
# # print(g(2))

# list = [(i, f(i)) for i in range(1,21) if i % 2 == 0]
# print(list)
# def select(f,col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# data = "1 2 3 4 5 7 6 5 8".split()
# res = select(int, data)
# res = where(lambda x: not x % 2, res)
# print(res)

# li = [x for x in range(1,20)]

# li = list(map(lambda x: x+10, li))
# print(li)

# data = list(map(int, input().split()))


data = [x for x in range(10)]
res = list(filter(lambda x: not x % 2, data))
print(res)


# num = [ "a", "b", "c"]
# id = [4, 5, 6, 7]
# x = [77, 66]
# data = list(zip(num, id, x))
#print(data)


# num = [ "a", "b", "c"]
# data = list(enumerate(num))
# print(data)