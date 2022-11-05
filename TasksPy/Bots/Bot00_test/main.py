import bot_config as bt
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *

TOKEN = bt.TOKEN
upd = Updater(TOKEN)


upd.dispatcher.add_handler(CommandHandler("Start", start_command))
upd.dispatcher.add_handler(CommandHandler("hi", hi_command))

upd.dispatcher.add_handler(CommandHandler("sum", sum_command))
upd.dispatcher.add_handler(CommandHandler("sub", sub_command))
upd.dispatcher.add_handler(CommandHandler("mult", mult_command))
upd.dispatcher.add_handler(CommandHandler("div", div_command))

upd.dispatcher.add_handler(CommandHandler("help", help_command))


upd.start_polling()
print('Server started.')
upd.idle()