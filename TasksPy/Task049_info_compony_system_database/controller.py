import data_base_init


personal_info = [("Иван", "Иванов", "Генеральным директор", 250000, 80000)]
data_base_init.curs.executemany("INSERT INTO personal VALUES(null, ?, ?, ?, ?, ?)", personal_info)
data_base_init.d_base.commit()

for i in data_base_init.curs.execute('SELECT * FROM  personal'):
    print(i)

# data_base_init.curs.execute('DELETE FROM personal WHERE ID=5')
# data_base_init.d_base.commit()

# for i in data_base_init.curs.execute('SELECT * FROM  personal'):
#     print(i)

data_base_init.curs.execute('SELECT * FROM personal LIKE "Олег"')
