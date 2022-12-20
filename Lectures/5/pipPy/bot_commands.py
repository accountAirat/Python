from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hi {update.effective_user.first_name}')


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'{datetime.datetime.now().time()}')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/hi\n/time\n/help')


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    items = msg.split()  # /sum 123 234
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x}+{y}={x+y}')
# async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(f'Hi {update.effective_user.first_name}')