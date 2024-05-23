import mysql.connector


mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '123456789',
    database = 'erp'
)

mycursos = mydb.cursor()
print('Consulta tabela')
mycursos.execute('SELECT * FROM cliente')
myresult = mycursos.fetchall()
for line in myresult:
    print('line: ', line)