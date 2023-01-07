def GameArena(list):
    print(*list[0:3])
    print(*list[3:6])
    print(*list[6:9])
    print("")
    return

def Victory(listPlayer):
    winningСombinations = ["1 2 3", "4 5 6", "7 8 9", "1 4 7", "2 5 8", "3 6 9", "1 5 9", "7 5 3"]
    for i in winningСombinations:
        if set(str(i).split()).issubset(listPlayer):
            return True
    return False
def Replace(arena, position, mark):
    arena[position-1] = mark

import random

step = ""
listPlayerOne = []
listPlayerTwo = []
listArena = ["1", "2", "3","4", "5", "6","7", "8", "9"]
print("Крестики: 1    Нолики: 2")
count = random.choice(["Единички", "Нолики"])
i = 0
while i < 9:
    while count == "Крестики" and i < 10:
        GameArena(listArena)
        print("Ходят Крестики, введите номер ячейки")
        step = input()
        if step in listPlayerOne or step in listPlayerTwo:
            print("Уже занято")
        else:
            listArena[int(step)-1] = "X"
            listPlayerOne.append(step)
            if Victory(listPlayerOne):
                print("Победили Крестики!")
                GameArena(listArena)
                exit()
            else:
                count = "Нолики"
                i+=1
                if i == 9:
                    print("Победила дружба!")
    while count == "Нолики" and i < 10:
        GameArena(listArena)
        print("Ходят Нолики, введите номер ячейки")
        step = input()
        if step in listPlayerOne or step in listPlayerTwo:
            print("Уже занято")
        else:
            listArena[int(step)-1] = "O"
            listPlayerTwo.append(step)
            if Victory(listPlayerTwo):
                print("Победили Нолики!")
                GameArena(listArena)
                exit()
            else:
                count = "Крестики"
                i+=1
                if i == 9:
                    print("Победила дружба!")