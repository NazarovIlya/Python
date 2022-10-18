import os
import view
import model


file_path_txt = 'test_phonebook.txt'
file_path_csv = 'test_phonebook.csv'
prompt_list = ['имя', 'фамилию', 'номер телефона', 'описане']
dictionary = {}


def run():
    clear = lambda: os.system('cls')
    clear()
    user_choice = view.choice_phone_base()
    if user_choice == 1:
        phonebook_txt(file_path_txt, prompt_list)
    elif user_choice == 2:  
        phonebook_csv(file_path_csv, prompt_list)
        
        
def phonebook_txt(file_path_txt, prompt_list):
    index = True
    data = model.read_phonebook_from_txt(file_path_txt)
    while index:
        view.view_phonebook(data)
        for prompt in prompt_list:
            view.user_input(prompt)
            model.add_record_to_txt(file_path_txt, prompt)
        model.add_empty_string_to_txt(file_path_txt)
        index = model.is_exit()
    
    
def phonebook_csv(file_path_csv, prompt_list):
    index = True
    data = model.read_phonebook_from_csv(file_path_csv)  
    while index:
        view.view_phonebook(data)
        for prompt in prompt_list:
            view.user_input(prompt)
            model.add_record_to_csv(file_path_csv, prompt)
        model.add_empty_string_to_csv(file_path_csv)
        index = model.is_exit()
