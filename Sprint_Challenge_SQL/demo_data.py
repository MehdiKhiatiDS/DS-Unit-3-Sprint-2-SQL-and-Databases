import sqlite3

# conn = sqlite3.connect('mehdi_sprint.sqlite3')
# curs = conn.cursor()
# query = 'CREATE TABLE mehdi_sprint (id INTEGER PRIMARY KEY, s TEXT, x INTEGER, y INTEGER);'
# curs.execute(query)   #commented becasue when i rerun it want to create it again and says table already exists!
# # comm = conn.commit()
# print (curs.execute(query).fetchall())


conn = sqlite3.connect('mehdi_sprint.sqlite3')
curs = conn.cursor()
query1 = 'INSERT OR IGNORE INTO demo1 VALUES (1, "g", 3, 9);'
curs.execute(query1)
# comm = conn.commit()
print (curs.execute(query1).fetchall())


conn = sqlite3.connect('mehdi_sprint.sqlite3')
curs = conn.cursor()
query2 = 'INSERT OR IGNORE INTO mehdi_sprint VALUES (2, "v", 5, 7);'
curs.execute(query2)
# comm = conn.commit()
print (curs.execute(query2).fetchall())


conn = sqlite3.connect('mehdi_sprint.sqlite3')
curs = conn.cursor()
query3 = 'INSERT OR IGNORE INTO mehdi_sprint VALUES (3, "f", 8, 7)'
curs.execute(query3)
comm = conn.commit()
print (curs.execute(query3).fetchall())


row_count = ' SELECT COUNT (*) FROM mehdi_sprint' 
print (curs.execute(row_count).fetchall())

row_x_is5 = 'SELECT * FROM  mehdi_sprint  WHERE x >= 5 AND y>5'
print (curs.execute(row_x_is5).fetchall())

row_y_is5 = 'SELECT * FROM  mehdi_sprint  WHERE y >= 5'
print (curs.execute(row_y_is5).fetchall())

distinct_y_value = 'SELECT DISTINCT y FROM mehdi_sprint '
print (curs.execute(distinct_y_value).fetchall())