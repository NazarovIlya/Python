import turtle

from numpy import number
import data_base_init as db
import model as m
import view as v


def run_application():
    personal_titles = db.title_list
    #personal_info = [("Иван", "Иванов", "Генеральным директор", 250000, 80000)]
    personal_info = []
    person = v.input_person_info(personal_titles)
    personal_info.append(person)
    #personal_info = v.input_person_info(personal_titles)
    
    db.curs.executemany("INSERT INTO personal VALUES(null, ?, ?, ?, ?, ?)", personal_info)
    db.d_base.commit()
    
    
    v.output_table_to_console()
    number = v.input_delete_id()
    m.delete_row_by_id(number)

    # for i in db.curs.execute('SELECT * FROM  personal'):
    #     print(i)

    # db.curs.execute('SELECT * FROM personal LIKE "Олег"')
