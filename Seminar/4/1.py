data = open('file.txt', 'a', encoding='UTF-8')

while True:
    string = input("Введите строку: ")
    if string == "":
        break
    data.write(string + '\n')

data.close()


# with open ('file.txt', 'a') as data:
# data.write(input()+"\n")