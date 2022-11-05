from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
from logger import *


def start_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(
        f'Привет, {update.effective_user.full_name}! Рад познакомиться. Я - простой калькулятор.\n'\
        'Команды, которые я понимаю:\n'\
        '/hi - Приветствие.\n'\
        '/sum - Сложение.\n'\
        '/sub - Вычитание.\n'\
        '/mult - Умножение.\n'\
        '/div - Деление.\n'\
        '/help - Помощь.')
    

def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Привет, {update.effective_user.full_name}!')
    
def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(
        f'/hi - Приветствие.\n'\
        '/sum - Сложение.\n'\
        '/sub - Вычитание.\n'\
        '/mult - Умножение.\n'\
        '/div - Деление.\n'\
        '/help - Помощь.')
    
    
def act_instraction(update: Update, command, action):
    update.message.reply_text(f'Необходимо ввести команду {command} и не менее двух чисел через пробел, чтобы произвести {action} чисел.\n')
    

def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    act_instraction(update, command= '/sum', action= 'сложение')
    msg = update.message.text
    print(msg)
    items = msg.split()
    sum_result = 0
    for i in range(1, len(items)):
        sum_result += float(items[i])
    lst = ''
    for i in range(1, len(items) - 1):
        lst += items[i]
        lst += " + "
    lst += items[-1]
    update.message.reply_text(f'{lst} = {sum_result}')
    

def sub_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    sub_result = float(items[1])
    for i in range(1, len(items) - 1):
        sub_result -= float(items[i + 1])
        print(sub_result)
    lst = ''
    for i in range(1, len(items) - 1):
        lst += items[i]
        lst += " - "
    lst += items[-1]
    update.message.reply_text(f'{lst} = {sub_result}')
    
    
def mult_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    mult_result = float(items[1])
    for i in range(1, len(items) - 1):
        mult_result *= float(items[i + 1])
    lst = ''
    for i in range(1, len(items) - 1):
        lst += items[i]
        lst += " * "
    lst += items[-1]
    update.message.reply_text(f'{lst} = {mult_result}')


def div_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    div_result = float(items[1])
    for i in range(1, len(items) - 1):
        div_result /= float(items[i + 1])
    lst = ''
    for i in range(1, len(items) - 1):
        lst += items[i]
        lst += " * "
    lst += items[-1]
    update.message.reply_text(f'{lst} = {div_result}')        