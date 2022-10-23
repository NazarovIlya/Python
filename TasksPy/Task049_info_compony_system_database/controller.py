import data_base_init as db
import model as m
import view as v


def run_application():
    personal_titles = db.title_list
    personal_info = [("Иван", "Иванов", "Генеральным директор", 250000, 80000)]
    # personal_info = []
    # person = v.input_person_info(personal_titles)
    # personal_info.append(person)
    
    #personal_info = v.input_person_info(personal_titles)
    
    # db.curs.executemany("INSERT INTO personal VALUES(null, ?, ?, ?, ?, ?)", personal_info)
    # db.d_base.commit()
    
    
    v.output_table_to_console()
    
    # number = v.input_delete_id()
    # is_true = m.delete_row_by_id(number)
    # v.is_deleted(is_true)

    
    name_list = db.title_list
    name_list_en = db.title_list_en
    name, value = v.input_delete_name(name_list, name_list_en)
    is_true = m.delete_row_by_somename_str(name, value)
    v.is_deleted(is_true)

    # for i in db.curs.execute('SELECT * FROM  personal'):
    #     print(i)

    # db.curs.execute('SELECT * FROM personal LIKE "Олег"')
