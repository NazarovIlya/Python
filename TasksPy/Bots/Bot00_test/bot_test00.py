import bot_config as bt
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

token = bt.token
app = Updater(token)

app.dispatcher.add_handler(CommandHandler("hello", hello))
print('Server started.')
app.start_polling()
app.idle()