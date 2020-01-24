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



birth_age = "SELECT * FROM  Employee GROUP BY BirthDate ORDER BY BirthDate DESC"
print (curs.execute(birth_age).fetchall())


average_age = 'SELECT AVG(BIrthDate) AS AverageAges FROM Employee'
print (curs.execute(average_age).fetchall())

ten_most_exp_unitprice_suppliers = "SELECT * FROM  Product ORDER BY UnitPrice AND SupplierId DESC LIMIT 10 "
print (curs.execute(ten_most_exp_unitprice_suppliers).fetchall())


largest_cat = 'SELECT DISTINCT CategoryId FROM Product'
print (curs.execute(largest_cat).fetchall())