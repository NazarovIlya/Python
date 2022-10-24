import data_base_init as db
import model as m
import view as v


def run_application():
    # personal_info = [("Иван", "Иванов", "Генеральным директор", 250000, 80000)]
    
    personal_titles = db.title_list     # column names in russian
    
    # MAIN
    while True:
            # OUTPUT THE TABLE INTO CONSOLE
        while True:
            choice = input('Хотите ли Вы увидеть таблицу,для выбора нажмите y/n (да/нет):\t')
            if choice == 'y':
                v.output_table_to_console()
                break
            elif choice == 'n':
                break
            else:
                print('Ошибка. Повторите ввод.')
        menu_choice = v.menu()
        if menu_choice == '1':
            v.output_table_to_console()
        else:
            break
                    

    
    
    # personal_info = []
    # person = v.input_person_info(personal_titles)
    # personal_info.append(person)
    
    # INSERT
    # personal_info = v.input_person_info(personal_titles)
    # is_true = m.insert_row(personal_info)
    # v.is_insert(is_true)
    
    
    # DELETE BY ID
    
    # number = v.input_delete_id()
    # is_true = m.delete_row_by_id(number)
    # v.is_deleted(is_true)
    

    # DELETE BY COLUMN NAME
    
    # name_list = db.title_list
    # name_list_en = db.title_list_en
    # name, value = v.input_delete_name(name_list, name_list_en)
    # is_true = m.delete_row_by_somename_str(name, value)
    # v.is_deleted(is_true)