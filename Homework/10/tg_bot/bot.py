from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext, CallbackQueryHandler 
import datetime


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}')
async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/help')
async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    msg = update.message.text
    items = msg.split()  # /sum 123 234
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x}+{y}={x+y}')
async def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = open('db.csv', 'a')
    file.write(f'{update.effective_user.first_name};{update.effective_user.id}; {update.message.text}\n')
    file.close()

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await hi_command(update, context)
    keyboard = [
        [
            KeyboardButton("/hi"),
            KeyboardButton("/game"),
        ],
        [KeyboardButton("Option 3", callback_data="3")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard)

    await update.message.reply_text("Please choose:", reply_markup=reply_markup)



app = ApplicationBuilder().token("5893850453:AAESI6Vw72hqsASbfiBIvuKUpzarNr8cqh8").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("start", start_command))

print('server start')
app.run_polling()



