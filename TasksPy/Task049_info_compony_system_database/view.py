import data_base_init as db


def input_person_info(titles):
    name_list = []
    for i in titles:
        name = input(f'Введите значения для поля {i}:\t')
        if i.isdigit() == True:
            name = int(name)
        name_list.append(name)
    return tuple(name_list)


def input_delete_name(name_list, name_list_en):
    name = ''
    value = ''
    while True:
        name, value = input(f'Введите название({name_list[0]}, {name_list[1]}, {name_list[2]}) и значение колонки для строки, которую(ые) хотите удалить: \t').split()
        if name.isdigit() or value.isdigit():
            print('Ошибка ввода, корректное строковое значение.')
        else:
            if name == name_list[0]:
                name = name_list_en[0]
            elif name == name_list[1]:
                name = name_list_en[1]
            elif name == name_list[2]:
                name = name_list_en[2]
        return name, value


def input_delete_id():
    number_id = 0
    while True:
        number_id = input('Введите значение id для строки, которую хотите удалить: \t')
        if number_id.isdigit():
            number_id = int(number_id)
            return number_id
        else:
            print('Ошибка ввода, ожидается целое число.')


def output_table_to_console():
    for i in db.curs.execute('SELECT * FROM  personal'):
        print(*i)
        

def is_deleted(is_true):
    if is_true == True:
        print('Строка(ки) успешно удалена!')
    else:
        print('Удаление завершилось неудачей.')


