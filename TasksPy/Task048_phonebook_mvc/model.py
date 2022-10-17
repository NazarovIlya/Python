def read_phonebook_from_file(file_path):
    with open(file_path, 'r', encoding= 'utf-8') as file:
        f = file.read()
    return f


def add_record(file_path, record_str):
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(f'{record_str}: {input()}\n')   


def add_empty_string(file_path):
    with open(file_path, 'a', encoding= 'utf-8') as file:
        file.write('\n')
        
        
def is_exit():
    check_true = input('Введите q для выхода:\t')
    if check_true == 'q':
        return False
    return True
