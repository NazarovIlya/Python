from telegram import Update
from telegram.ext import CallbackContext
import bot_commands as bc
from logger import *


def sum_command(update: Update, context: CallbackContext):
    msg = update.message.text
    print(msg)
    items = msg.split()
    if len(items) < 3:
        bc.act_instraction(update, command= '/sum', action= 'сложение')
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
        logger(update, context, sum_result)
    

def sub_command(update: Update, context: CallbackContext):
    msg = update.message.text
    print(msg)
    items = msg.split()
    if len(items) < 3:
        bc.act_instraction(update, command= '/sub', action= 'вычитание')
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
        logger(update, context, sub_result)
    
    
def mult_command(update: Update, context: CallbackContext):
    msg = update.message.text
    print(msg)
    items = msg.split()
    if len(items) < 3:
        bc.act_instraction(update, command= '/mult', action= 'умножение')
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
        logger(update, context, mult_result)


def div_command(update: Update, context: CallbackContext):
    msg = update.message.text
    print(msg)
    items = msg.split()
    if len(items) < 3:
        bc.act_instraction(update, command= '/div', action= 'деление')
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
        logger(update, context, div_result)