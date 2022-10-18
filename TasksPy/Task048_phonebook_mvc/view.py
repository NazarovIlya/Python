import model

def user_input(str):
    print(f'Введите {str}, нового контакта:\t')

def view_phonebook(data):
    print('Телефонный справочник содержит следующие записи:\t')
    print(data)


def choice_phone_base():
    index = True
    while index:
        print('Нажмите "1", если хотите работать с телефонным справочником .txt версии или "2", если хотите работать с телефонным справочником .csv версии:\t')
        user_choice = int(input())
        if user_choice == 1:
            index = False
            return user_choice
        elif user_choice == 2:
            index = False
            return user_choice          
        else:
            print('Ошибка ввода. Повторите ввод.')
    return user_choice
        
