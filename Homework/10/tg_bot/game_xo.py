from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import random


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global listPlayerX
    global listPlayerO
    global listArena
    global player
    global i
    global flag_win
    listPlayerX = []
    listPlayerO = []
    listArena = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    player = random.choice(["X", "O"])
    flag_win = False
    i = 0
    message_text = f"Ход {player}"
    await update.message.reply_text("Игра началась!")
    await print_game_arena(update, context, message_text)


async def print_game_arena(update: Update, context: ContextTypes.DEFAULT_TYPE, message_text):
    keyboard = [
        [
            KeyboardButton("/start")
        ],
        [
            KeyboardButton(f"{listArena[0]}"),
            KeyboardButton(f"{listArena[1]}"),
            KeyboardButton(f"{listArena[2]}"),
        ],
        [
            KeyboardButton(f"{listArena[3]}"),
            KeyboardButton(f"{listArena[4]}"),
            KeyboardButton(f"{listArena[5]}"),
        ],
        [
            KeyboardButton(f"{listArena[6]}"),
            KeyboardButton(f"{listArena[7]}"),
            KeyboardButton(f"{listArena[8]}"),
        ],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard)
    await update.message.reply_text(message_text, reply_markup=reply_markup)


async def victory(update: Update, context: ContextTypes.DEFAULT_TYPE, listPlayer):
    global flag_win
    global player
    winningСombinations = ["1 2 3", "4 5 6", "7 8 9",
                           "1 4 7", "2 5 8", "3 6 9", "1 5 9", "7 5 3"]
    for i in winningСombinations:
        if set(str(i).split()).issubset(listPlayer):
            flag_win = True
            message_text = (f"Победили {player}!")
            await print_game_arena(update, context, message_text)
            return True
    return False


async def check_step(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global player
    global i
    global flag_win
    step = update.message.text
    if flag_win:
        await start(update, context)
    elif step == "X" or step == "O":
        await update.message.reply_text("Уже занято!")
        return
    elif 0 > int(step) > 9:
        await update.message.reply_text("Не верный символ!")
        return
    else:
        listArena[int(step)-1] = player
        if player == "X":
            listPlayerX.append(step)
            if await victory(update, context, listPlayerX):
                return
            player = "O"
        else:
            listPlayerO.append(step)
            if await victory(update, context, listPlayerO):
                return
            player = "X"
        message_text = f"Ход {player}"
        await print_game_arena(update, context, message_text)
        i += 1
        if i == 9:
            await update.message.reply_text("Победила дружба!")
            flag_win = True
            return

app = ApplicationBuilder().token(
    "5893850453:AAESI6Vw72hqsASbfiBIvuKUpzarNr8cqh8").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, check_step))


print('server start')
app.run_polling()
