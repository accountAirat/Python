from datetime import datetime
import json
def search_worker(data, key, value):
    return list(filter(lambda x: x.get(key,) == value, data))
def search_salary(data, salary, range_line):
    return list(filter(lambda x: range_line[0] < int(x.get(salary,0)) < range_line[1], data))
def add_worker(data, form, temp):
    temp.insert(0,int(data[-1].get('id', 1000))+1)
    data.append(formation(form,temp))
    return data
def delete_worker(data,key,id):
    for i in range(0, len(data)-1):
        if data[i].get(key,) == id:
            data.pop(i)
    return data
    #return list(filter(lambda x: x.get(key,) != id, data))
def update_worker(data, form, temp, id):
    temp.insert(0,id)
    data.insert(int(id)-1,(formation(form,temp)))
    return data
def formation(form,line):
    return dict(zip(form,line))
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
        file.write('\n')
    file.close()
def write_csv(data,form):
    name_date = str(datetime.now().date())
    file = open(f'database_{name_date}.csv', 'w')
    for x in range(0, len(data)):    
        for y in form:
            file.writelines(f'{data[x].get(y,"")};')
        file.writelines('\n')
    file.close()
def write_json(data):
    name_date = str(datetime.now().date())
    file = open(f'database_{name_date}.json', 'w')
    for x in data:
        temp = json.dumps(x)
        file.write(temp)
        file.writelines('\n')
    file.close()