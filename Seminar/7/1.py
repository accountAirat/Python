# # # 1)
# # a = [4,3,-10,1,7,12]
# # a.sort(key = lambda x: x%2)
# # print(a)
# # 2)
# string = 'Лена Енисей Волга Дон'
# # river = string.split()
# # river_res = sorted(river, key = lambda x: len(x), reverse = True)
# # print(' '.join(river_res))
# # 2.1)
# string = sorted(string.split(), key=lambda x: len(x))[::-1]
# print(*string)