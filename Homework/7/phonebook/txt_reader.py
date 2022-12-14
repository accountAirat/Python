def read():
    data = open('phonebook.txt', 'r', encoding='UTF-8')
    phonebook = []
    for i in data.readlines():
        phonebook.append(i.split())
    data.close()
    return phonebook
