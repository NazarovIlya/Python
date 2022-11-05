from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def hi_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'Hi, {update.effective_user.first_name}!')
    
def help_command(update: Update, context: CallbackContext):
    update.message.reply_text
    (f'/hi\n'\
    '/sum\n'\
    '/sum\n'\
    '/help')

def sum_command(update: Update, context: CallbackContext):
    msg = update.message.text
    print(msg)
    items = msg.split()
    sum_result = 0
    for i in range(1, len(items)):
        sum_result += int(items[i])
    lst = ''
    for i in range(1, len(items) - 1):
        lst += items[i]
        lst += " + "
    lst += items[-1]
    update.message.reply_text(f'{lst} = {sum_result}')
    

def sub_command(update: Update, context: CallbackContext):
    msg = update.message.text
    print(msg)
    items = msg.split()
    sub_result = int(items[1])
    for i in range(1, len(items) - 1):
        sub_result -= int(items[i + 1])
        print(sub_result)
    lst = ''
    for i in range(1, len(items) - 1):
        lst += items[i]
        lst += " - "
    lst += items[-1]
    update.message.reply_text(f'{lst} = {sub_result}')
    
    
def mult_command(update: Update, context: CallbackContext):
    msg = update.message.text
    print(msg)
    items = msg.split()
    mult_result = int(items[1])
    for i in range(1, len(items) - 1):
        mult_result *= int(items[i + 1])
    lst = ''
    for i in range(1, len(items) - 1):
        lst += items[i]
        lst += " * "
    lst += items[-1]
    update.message.reply_text(f'{lst} = {mult_result}')


def div_command(update: Update, context: CallbackContext):
    msg = update.message.text
    print(msg)
    items = msg.split()
    div_result = int(items[1])
    for i in range(1, len(items) - 1):
        div_result /= int(items[i + 1])
    lst = ''
    for i in range(1, len(items) - 1):
        lst += items[i]
        lst += " * "
    lst += items[-1]
    update.message.reply_text(f'{lst} = {div_result}')        