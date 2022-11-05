import bot_config as bt
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *

token = bt.token
app = Updater(token)


app.dispatcher.add_handler(CommandHandler("hi", hi_command))

app.dispatcher.add_handler(CommandHandler("sum", sum_command))
app.dispatcher.add_handler(CommandHandler("sub", sub_command))
app.dispatcher.add_handler(CommandHandler("mult", mult_command))
app.dispatcher.add_handler(CommandHandler("div", div_command))

app.dispatcher.add_handler(CommandHandler("help", help_command))


print('Server started.')
app.start_polling()
app.idle()