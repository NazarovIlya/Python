import model


def user_input(str):
    print(f'Введите {str}, нового контакта')

def view_phonebook(file_path):
    print(model.read_phonebook_from_file(file_path))
