import data_base_init as db


def delete_row_by_id(name_id):
    db.curs.execute(f'SELECT FROM personal WHERE ID={name_id}')
    db.d_base.commit()


def delete_row_by_somename_str(name, value):
    db.curs.execute(f'SELECT FROM personal WHERE LIKE {name}={value}')
    db.d_base.commit()


def delete_row_by_id(name_id):
    db.curs.execute(f'DELETE FROM personal WHERE ID={name_id}')
    db.d_base.commit()


def delete_row_by_somename_str(name, value):
    db.curs.execute(f'DELETE FROM personal WHERE LIKE {name}={value}')
    db.d_base.commit()


