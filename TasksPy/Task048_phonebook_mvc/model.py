def read_phonebook_from_txt(file_path_txt):
    with open(file_path_txt, 'r', encoding= 'utf-8') as file:
        f = file.read()
    return f


def read_phonebook_from_csv(file_path_csv):
    with open(file_path_csv, 'r', encoding= 'utf-8') as file:
        f = file.read().replace(',', '')
    return f


def add_record_to_txt(file_path_txt, record_str):
    with open(file_path_txt, 'a', encoding='utf-8') as file:
        file.write(f'{record_str}: {input()}\n')
        
        
def add_record_to_csv(file_path_csv, record_str):
    with open(file_path_csv, 'a', encoding='utf-8') as file:
        file.write('{}:;{}\n'.format(record_str, input()))  

        
def add_empty_string_to_txt(file_path_txt):
    with open(file_path_txt, 'a', encoding= 'utf-8') as file:
        file.write('\n')
        
def add_empty_string_to_csv(file_path_csv):       
    with open(file_path_csv, 'a', encoding='utf-8') as file:
        file.write('\n')  
        
        
def is_exit():
    check_true = input('Введите q для выхода:\t')
    if check_true.lower() == 'q':
        return False
    return True
