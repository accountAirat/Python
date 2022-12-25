# from progress.bar import Bar
# import time

# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(1)
#     # Do some work
#     bar.next()
# bar.finish()

# import emoji

# print(emoji.emojize('Python is :thumbs_up:'))

# import matplotlib.pyplot as plt
# import numpy as np

# # Fixing random state for reproducibility
# # np.random.seed(19680801)


# # plt.rcdefaults()
# # fig, ax = plt.subplots()

# # # Example data
# # people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
# # y_pos = np.arange(len(people))
# # performance = 3 + 10 * np.random.rand(len(people))
# # error = np.random.rand(len(people))

# # ax.barh(y_pos, performance, xerr=error, align='center')
# # ax.set_yticks(y_pos, labels=people)
# # ax.invert_yaxis()  # labels read top-to-bottom
# # ax.set_xlabel('Performance')
# # ax.set_title('How fast do you want to go today?')

# list = [1,2,3,2,7]
# plt.plot(list)

# plt.show()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext
from bot_commands import *


app = ApplicationBuilder().token("5893850453:AAESI6Vw72hqsASbfiBIvuKUpzarNr8cqh8").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("sum", sum_command))
print('Server start')

app.run_polling()