from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from datetime import datetime


def log(update: Update, context: CallbackContext):
    with open('db.csv', 'a', encoding= 'utf-8') as f:
        f.write(f'date: {datetime.now().strftime("%d-%M-%y")},'\
            f'time: {datetime.now().strftime("%H:%M")},'\
            f'id: {update.effective_user.id},'\
            f'full_name: {update.effective_user.full_name},'\
            f'{update.message.text}\n')