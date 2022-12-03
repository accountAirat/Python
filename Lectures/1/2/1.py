#  a запись
#  r чтение
#  w перезапись

colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')
data.writelines(colors)
data.close()

import file as f 

def functions (arg):
    return
def functions (*arg):# неограниченное колличество аргументов 