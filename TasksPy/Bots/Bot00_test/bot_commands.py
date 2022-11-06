from telegram import Update, Bot, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext
from logger import *


bot_commands = f'/hi - Приветствие.\n'\
        '/sum - Сложение.\n'\
        '/sub - Вычитание.\n'\
        '/mult - Умножение.\n'\
        '/div - Деление.\n'\
        '/help - Помощь.'
        
        
def start_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(
        f'Привет, {update.effective_user.full_name}! Рад познакомиться. Я - простой калькулятор.\n'\
        'Команды, которые я понимаю:\n'\
        f'{bot_commands}')
    

def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Привет, {update.effective_user.full_name}!')
    
    
def input_error(update: Update, context: CallbackContext) -> None:
        context.bot.send_message(chat_id=update.effective_chat.id,\
        text=f'Вы должны выбрать одну комманд:\n{bot_commands}')
    
    
def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Вы должны выбрать одну комманд:\n{bot_commands}')  
    
    
def act_instraction(update: Update, command, action):
    update.message.reply_text(f'Необходимо ввести команду {command} и не менее двух чисел через пробел, чтобы произвести {action} чисел.\n')
    

def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    if len(items) < 3:
        act_instraction(update, command= '/sum', action= 'сложение')
    else:
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
    if len(items) < 3:
        act_instraction(update, command= '/sub', action= 'вычитание')
    else:   
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
    if len(items) < 3:
        act_instraction(update, command= '/mult', action= 'умножение')
    else:
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
    if len(items) < 3:
        act_instraction(update, command= '/div', action= 'деление')
    else:
        div_result = float(items[1])
        for i in range(1, len(items) - 1):
            div_result /= float(items[i + 1])
        lst = ''
        for i in range(1, len(items) - 1):
            lst += items[i]
            lst += " * "
        lst += items[-1]
        update.message.reply_text(f'{lst} = {div_result}')        