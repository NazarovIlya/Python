from telegram import Update
#from telegram.ext import CallbackContext
from datetime import datetime


def logger(update: Update):
    with open('log.csv', 'a+', encoding= 'utf-8') as f:
        f.write('')
    with open('log.csv', 'r+', encoding= 'utf-8') as f:
        data = f.read().splitlines()
        if data == []:
            f.write('DATE; TIME; ID; FULL_NAME; USER_INPUT;\n')
        f.write(f'{datetime.now().strftime("%d-%M-%y")}; '\
            f'{datetime.now().strftime("%H:%M")}; '\
            f'{update.effective_user.id}; '\
            f'{update.effective_user.full_name}; '\
            f'{update.message.text};\n')
        
        
# def param_contr(update: Update):    
#     def log_decorator(func):
#         def wrapper(*args, **kwargs):
#             with open('db.csv', 'a+', encoding= 'utf-8') as f:
#                 f.write('')
#             with open('db.csv', 'r+', encoding= 'utf-8') as f:
#                 data = f.read().splitlines()
#                 if data == []:
#                     f.write('DATE; TIME; ID; FULL_NAME; USER_INPUT; RESULT;\n')
#                 result = func(args, kwargs)   
#                 f.write(f'{datetime.now().strftime("%d-%M-%y")};'\
#                     f'{datetime.now().strftime("%H:%M")};'\
#                     f'{update.effective_user.id};'\
#                     f'{update.effective_user.full_name};'\
#                     f'{update.message.text}; '\
#                     f'{result}\n')
#             #return result 
#         return wrapper
#     return log_decorator