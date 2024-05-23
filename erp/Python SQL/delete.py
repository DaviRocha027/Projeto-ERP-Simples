import mysql.connector


mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '123456789',
    database = 'erp'
)

mycursos = mydb.cursor()
print('Delete cliente')
sql = "DELETE FROM cliente WHERE id = '2'"
mycursos.execute(sql)

mydb.commit()

print(mycursos.rowcount, 'gravações deletadas')

