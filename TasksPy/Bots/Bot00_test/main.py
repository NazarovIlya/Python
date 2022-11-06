import bot_config as bt
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import bot_commands as bc
# import 

TOKEN = bt.TOKEN
upd = Updater(TOKEN)


upd.dispatcher.add_handler(CommandHandler("Start", bc.start_command))
upd.dispatcher.add_handler(CommandHandler("hi", bc.hi_command))

upd.dispatcher.add_handler(CommandHandler("sum", bc.sum_command))
upd.dispatcher.add_handler(CommandHandler("sub", bc.sub_command))
upd.dispatcher.add_handler(CommandHandler("mult", bc.mult_command))
upd.dispatcher.add_handler(CommandHandler("div", bc.div_command))

upd.dispatcher.add_handler(CommandHandler("help", bc.help_command))


upd.start_polling()
print('Server started.')
upd.idle()