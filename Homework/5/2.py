import random


def PlayerVsPlayer(mode):
    bank = 100
    count = random.choice(["Player1", "Player2"])
    step = 0
    while mode != "menu":
        while count == "Player1" and mode != "menu":
            print(f"Счёт: {bank}")
            print("Ход Игрока № A: ")
            step = int(input())
            if 1 > step or step > 28:
                print("!!!Не верное число!!!")
            else:
                bank = bank - step
            if bank <= 0:
                print("Поздравляю! Игрок A выиграл")
                mode = "menu"
            count = "Player2"
        while count == "Player2" and mode != "menu":
            print(f"Счёт: {bank}")
            print("Ход Игрока № B: ")
            step = int(input())
            if 1 > step or step > 28:
                print("!!!Не верное число!!!")
            else:
                bank = bank - step
            if bank <= 0:
                print("Поздравляю! Игрок B выиграл")
                mode = "menu"
            count = "Player1"
    return mode


def PlayerVsBot(mode):
    bank = 100
    count = random.choice(["Player", "Bot"])
    step = 1
    bot_count = 0
    while mode != "menu":
        while count == "Player" and mode != "menu":
            print(f"Счёт: {bank}")
            print("Ход Игрока: ")
            step = int(input())
            if 1 > step or step > 28:
                print("!!!Не верное число!!!")
            else:
                bank = bank - step
            if bank <= 0:
                print("Поздравляю! Игрок выиграл")
                mode = "menu"
            count = "Bot"
        while count == "Bot" and mode != "menu":
            print(f"Счёт: {bank}")
            print("Ход Бота: ")
            if bank < 29:
                step = bank
            elif bank % 29 == 0:
                step = 1
            else:
                step = bank % 29
            print(step)
            if 0 > step or step > 28:
                print("!!!Не верное число!!!")
            else:
                bank = bank - step
            if bank <= 0:
                print("Поздравляю! Бот выиграл")
                mode = "menu"
            count = "Player"
    return mode


modes = "menu"

while modes != "0":
    print("Выберите режим игры!")
    print("1 Игрок против Игрока")
    print("2 Игрок против Бота")
    print("0 Чтобы выйти")
    modes = input()
    if modes == "1":
        PlayerVsPlayer(modes)
    elif modes == "2":
        PlayerVsBot(modes)
    elif modes == "0":
        print("Пока!")
        exit()
    else:
        print("")
        print("!!!Не верное символ!!!")
