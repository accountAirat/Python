from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import random

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    await update.message.reply_text("Привет!")
    await form(update, context)

async def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = open('db.csv', 'a')
    file.write(f'{update.effective_user.first_name};{update.effective_user.id}; {update.message.text}\n')
    file.close()

async def form(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    update.message.chat_id
    update.message.from_user.id, 'Привет')
    






app = ApplicationBuilder().token(
    "5893850453:AAESI6Vw72hqsASbfiBIvuKUpzarNr8cqh8").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, check_step))


print('server start')
app.run_polling()
