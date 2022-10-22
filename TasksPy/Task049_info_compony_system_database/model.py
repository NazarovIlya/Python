import data_base_init as db


def delete_row_by_id(name_id):
    db.curs.execute(f'DELETE FROM personal WHERE ID={name_id}')
    db.d_base.commit()



