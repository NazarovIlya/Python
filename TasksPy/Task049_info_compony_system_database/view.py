import data_base_init as db


def input_person_info(titles):
    name_list = []
    for i in titles:
        name = input(f'Введите значения для поля {i}:\t')
        if i.isdigit() == True:
            name = int(name)
        name_list.append(name)
    return tuple(name_list)


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
        

