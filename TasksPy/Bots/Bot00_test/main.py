from telegram import Update
from telegram.ext import Updater, CommandHandler, TypeHandler
import bot_config as bt
import bot_commands as bc
import simple_calc as sc


def main():
    TOKEN = bt.TOKEN
    upd = Updater(TOKEN)

    upd.dispatcher.add_handler(CommandHandler("Start", bc.start_command))
    upd.dispatcher.add_handler(CommandHandler("hi", bc.hi_command))

    upd.dispatcher.add_handler(CommandHandler("sum", sc.sum_command))
    upd.dispatcher.add_handler(CommandHandler("sub", sc.sub_command))
    upd.dispatcher.add_handler(CommandHandler("mult", sc.mult_command))
    upd.dispatcher.add_handler(CommandHandler("div", sc.div_command))

    upd.dispatcher.add_handler(CommandHandler("help", bc.help_command))
    
    upd.dispatcher.add_handler(TypeHandler(Update, bc.input_error))

    upd.start_polling()
    print('Server started.')
    upd.idle()
    

if __name__ == "__main__":
    main()