data = open('file.txt', 'r', encoding='UTF-8')

for i in data.readlines():
    print(i,  end='')
    print(f"Колличество символов = {len(i)}")
    print(f"Колличество слов = {len(i.split())}")
    print()
data.close()