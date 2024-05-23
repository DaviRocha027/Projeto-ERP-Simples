import mysql.connector




mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '123456789',
    database = 'erp'
)

cliente = "Maria"
telefone = "2789875731"
cidade = "Nova Caetano"

mycursos = mydb.cursor()
print('Inserindo dados')
sql = "INSERT INTO cliente (nomeCliente, TelefoneCliente, CidadeCliente) values(%s, %s, %s)"
val = (cliente, telefone, cidade)

mycursos.execute(sql,val)
mydb.commit()
print(mycursos.rowcount, ' dados inseridos')
