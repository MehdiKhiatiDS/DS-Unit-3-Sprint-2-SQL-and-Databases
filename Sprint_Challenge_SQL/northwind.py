import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()
query = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"
[('Category',), ('Customer',), ('CustomerCustomerDemo',),
('CustomerDemographic',), ('Employee',), ('EmployeeTerritory',), ('Order',),
('OrderDetail',), ('Product',), ('Region',), ('Shipper',), ('Supplier',),
('Territory',)]
conn = conn.commit()

print (curs.execute(query).fetchall())




ten_most_exp_unitprice = "SELECT * FROM  OrderDetail ORDER BY UnitPrice DESC LIMIT 10"
print (curs.execute(ten_most_exp_unitprice).fetchall())







largest_cat = 'SELECT DISTINCT CategoryId FROM Product'
print (curs.execute(largest_cat).fetchall())