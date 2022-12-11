# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
def StrDict(string):
    string = string[:-3].split('+')
    result = {}
    if string[-1].count('x') == 0:
        result["num"] = string.pop()
#        print(result["num"])
    if string[-1][-2] == "x":
        result["x"] = string.pop()[:-3]
#        print(result["x"])
    for i in string:
        temp = i.split("*x**")
        result[temp[1]] = temp[0]
#        print(result)
    return result

def SumDict(dictionaryOne, dictionaryTwo):
    result = list()
    a = int(dictionaryOne.pop("x", "0")) + int(dictionaryTwo.pop("x", "0"))
    if a != 0:
        result.append(f"{a}x")
        result.append("+")
    a = int(dictionaryOne.pop("num", "0")) + int(dictionaryTwo.pop("num", "0"))
    if a != 0:
        result.append(a)
        result.append("+")
    if len(dictionaryOne) > len(dictionaryTwo):
        for i in reversed(dictionaryOne):
            result.insert(0, "+")
            result.insert(0, str(int(dictionaryOne.get(i, "0")) + int(dictionaryTwo.get(i, "0"))) + "*x**" + i)
    else:
        for i in reversed(dictionaryTwo):
            result.insert(0, "+") 
            result.insert(0, str(int(dictionaryOne.get(i, "0")) + int(dictionaryTwo.get(i, "0"))) + "*x**" + i)
      

    result[-1] = " = 0"
    return result

n = open('fffile.txt', 'r')
m = open('ffile.txt', 'r')
ns = n.read()
ms = m.read()
ns = StrDict(ns)
ms = StrDict(ms)
print(*SumDict(ms, ns))


n.close()
m.close()
