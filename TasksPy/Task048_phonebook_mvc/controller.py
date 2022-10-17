import view
import model


file_path = 'test_phonebook.txt'
prompt_list = ['имя', 'фамилию', 'номер телефона', 'описане']


def run():
    index = True
    while index:
        view.view_phonebook(file_path)
        for prompt in prompt_list:
            view.user_input(prompt)
            model.add_record(file_path, prompt)
        model.add_empty_string(file_path)
        index = model.is_exit()
