# a - открытие для добавления данных (может создать)
# r - открытие для чтения данных
# w - открытие для записи(перезапись) данных (может создать)
# w +, r + добавить и читать

# 1 вариант, надо закрывать
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors)
# data.write('\nLine 2\n')
# data.write('Line 3\n')
# data.close()


# exit()

# 2 вариант сам закрывается
# with open('file.txt', 'w') as data:
#     data.write('Line 2\n')
#     data.write('Line 3\n')

# Чтение
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close

def f (x):
    return x**2