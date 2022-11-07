from telegram import Update
from telegram.ext import CallbackContext
from logger import *


bot_commands = f'/hi - Приветствие.\n'\
        '/sum - Сложение.\n'\
        '/sub - Вычитание.\n'\
        '/mult - Умножение.\n'\
        '/div - Деление.\n'\
        '/help - Помощь.'
        
        
def start_command(update: Update, context: CallbackContext):
    logger(update)
    update.message.reply_text(
        f'Привет, {update.effective_user.full_name}! Рад познакомиться. Я - простой калькулятор.\n'\
        'Команды, которые я понимаю:\n'\
        f'{bot_commands}')
    

def hi_command(update: Update, context: CallbackContext):
    logger(update)
    update.message.reply_text(f'Привет, {update.effective_user.full_name}!')
    
    
def input_error(update: Update, context: CallbackContext) -> None:
        logger(update)
        context.bot.send_message(chat_id=update.effective_chat.id,\
        text=f'Вы должны выбрать одну комманд:\n{bot_commands}')
    
    
def help_command(update: Update, context: CallbackContext):
    logger(update)
    update.message.reply_text(f'Вы должны выбрать одну комманд:\n{bot_commands}')  
    
    
def act_instraction(update: Update, command, action):
    logger(update)
    update.message.reply_text(f'Необходимо ввести команду {command} и не менее двух чисел через пробел, чтобы произвести {action} чисел.\n')
      