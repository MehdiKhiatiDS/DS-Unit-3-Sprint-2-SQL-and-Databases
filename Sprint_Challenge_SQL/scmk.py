import sqlite3

# conn = sqlite3.connect('mehdi_sprint.sqlite3')
# curs = conn.cursor()
# query = 'CREATE TABLE mehdi_sprint (id INTEGER PRIMARY KEY, s TEXT, x INTEGER, y INTEGER);'
# curs.execute(query)   #commented becasue when i rerun it want to create it again and says table already exists!
# comm = conn.commit
# print (curs.execute(query).fetchall())


conn = sqlite3.connect('mehdi_sprint.sqlite3')
curs = conn.cursor()
query = 'INSERT OR IGNORE INTO mehdi_sprint VALUES (1, "g", 3, 9);'
curs.execute(query)
comm = conn.commit
print (curs.execute(query).fetchall())


conn = sqlite3.connect('mehdi_sprint.sqlite3')
curs = conn.cursor()
query = 'INSERT OR IGNORE INTO mehdi_sprint VALUES (2, "v", 5, 7);'
curs.execute(query)
comm = conn.commit
print (curs.execute(query).fetchall())


conn = sqlite3.connect('mehdi_sprint.sqlite3')
curs = conn.cursor()
query = 'INSERT OR IGNORE INTO mehdi_sprint VALUES (3, "f", 8, 7)'
curs.execute(query)
comm = conn.commit
print (curs.execute(query).fetchall())

conn = sqlite3.connect('mehdi_sprint.sqlite3')
curs = conn.cursor()
query = ' SELECT COUNT (*) FROM mehdi_sprint' 
print (curs.execute(query).fetchall())