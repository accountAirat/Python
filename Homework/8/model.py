import datetime
def search_worker(data, key, value):
    return list(filter(lambda x: x.get(key,) == value, data))
def search_salary(data, salary, range_line):
    return list(filter(lambda x: range_line[0] < int(x.get(salary,0)) < range_line[1], data))
def add_worker(data, form, temp):
    temp.insert(0,len(data)+1)
    data.append(formation(form,temp))
    return data

def formation(form,line):
    string = dict(zip(form,line))
    return string

def read_txt(form):
    file = open('database.txt', 'r', encoding='UTF-8')
    data = []
    for i in file.readlines():
        data.append(formation(form,(i.split())))
    file.close()
    return data

def write_txt(data):
    file = open('database.txt', 'w', encoding='UTF-8')
    for x in range(0, len(data)):
        file.writelines(f'{" ".join(map(str,data[x].values()))}')
        file.writelines('\n')
    file.close()

def write_csv(data):
    data = open(f'database_{datetime.datetime.now()}.csv', 'w')
    for x in range(0, len(data)):
        for y in range(0, len(data[x])):
            data.writelines(f'{data[x][y]};')
        data.writelines('\n')
    data.close()
