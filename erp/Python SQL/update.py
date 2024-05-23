import mysql.connector




mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '123456789',
    database = 'erp'
)


cidade = "Pedro Cristovao"
Id = '1'

mycursos = mydb.cursor()
print('Update Cliente')
sql = "UPDATE cliente SET CidadeCliente = %s WHERE Id = %s"
val = (cidade, Id)

mycursos.execute(sql,val)
mydb.commit()
print(mycursos.rowcount, ' dados atualizados')
