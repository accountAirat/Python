def write(phonebook):
    data = open('phonebook_new.csv', 'w')
    for x in range(0, len(phonebook)):
        for y in range(0, len(phonebook[x])):
            data.writelines(f'{phonebook[x][y]};')
        data.writelines('\n')
    data.close()
